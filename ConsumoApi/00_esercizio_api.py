# Importiamo FastAPI per gestire le richieste web web (creazione delle API)
# UploadFile, File, Form servono per gestire il caricamento di file e i dati dai form HTML
# HTTPException serve per restituire errori HTTP standard (es. 400 Bad Request, 500 Internal Error)
from fastapi import FastAPI, UploadFile, File, Form, HTTPException

# FileResponse serve per inviare un file intero all'utente (es. per il download dell'Excel)
# StreamingResponse serve per inviare dati in un flusso continuo (utile per le immagini dei grafici in memoria)
from fastapi.responses import FileResponse, StreamingResponse

import pyodbc as odbc # Libreria per connettersi a database relazionali come SQL Server
import pandas as pd # Ottima per l'analisi e la manipolazione dei dati in forma tabellare (DataFrames)
import matplotlib.pyplot as plt # Motore principale per la generazione dei grafici
import io # Modulo per gestire flussi di input/output in memoria (senza salvare file fisici su disco)
import os # Utile per operazioni sul sistema operativo (se necessarie per i percorsi file)

# Inizializziamo l'applicazione principale. 
# Il parametro 'title' imposta il nome visibile nella documentazione automatica (Swagger UI)
app = FastAPI(title="API Multi-Database e Analisi Dati")

# Costante globale con la stringa di connessione a SQL Server.
# Utilizza l'autenticazione di Windows (Trusted_Connection=yes)
STR_CON = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=Cristian_Pico\\SQLEXPRESS;"
    "DATABASE=ScuolaDb;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

def get_connection():
    """
    Funzione di supporto per evitare di riscrivere il codice di connessione in ogni endpoint.
    Restituisce un oggetto connessione attivo.
    """
    return odbc.connect(STR_CON)

# ==========================================
# ROTTE EREDITATE DA app.txt (LETTURA DATI)
# ==========================================

# @app.get definisce un endpoint in sola lettura. 
# Quando un utente naviga su "http://tuo-server/tabelle", esegue questa funzione.
@app.get("/tabelle")
def lista_tabelle():
    """Ottiene la lista di tutte le tabelle dal database."""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Esecuzione della Stored Procedure presente nel DB
        cursor.execute("EXEC sp_ListaTabelle")
        
        # fetchall() restituisce una lista di tuple. 
        # La list comprehension estrae il primo elemento (l'indice 0) di ogni tupla per avere una lista di stringhe "pulite".
        tabelle = [row[0] for row in cursor.fetchall()]
        
        # Buona pratica: chiudere sempre la connessione per non saturare i pool di SQL Server
        conn.close()
        
        # FastAPI converte automaticamente questo dizionario Python in un JSON di risposta.
        return {"tabelle": tabelle}
    except Exception as e:
        # Se qualcosa va storto, invece di bloccare il server, restituiamo un errore HTTP 500 gestito
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/tabella/{nome_tabella}")
def leggi_tabella(nome_tabella: str):
    """
    Legge il contenuto di una tabella specifica. 
    {nome_tabella} è un parametro dinamico: FastAPI lo passa direttamente alla funzione.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Le parentesi quadre [ ] intorno al nome della tabella prevengono errori di sintassi SQL
        # se il nome della tabella dovesse contenere spazi o caratteri speciali.
        query = f"SELECT * FROM [{nome_tabella}]"
        cursor.execute(query)
        
        # cursor.description contiene i metadati della query.
        # Estraiamo i nomi delle colonne (che si trovano all'indice 0 di ogni elemento della descrizione).
        columns = [col[0] for col in cursor.description]
        
        # Recuperiamo tutte le righe del risultato
        rows = cursor.fetchall()
        conn.close()
        
        # Questa riga unisce (zip) i nomi delle colonne con i valori della rispettiva riga,
        # creando un dizionario dict() per ogni riga. Il risultato è una lista di dizionari perfetti per il JSON.
        result = [dict(zip(columns, row)) for row in rows]
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Modifica la riga degli import di FastAPI se non hai già incluso "Form" e "File"
# from fastapi import FastAPI, UploadFile, File, Form, HTTPException

@app.post("/importa_exceltoSQL")
async def importa_excel(file: UploadFile = File(...), nome_tabella: str = Form(...)):
    """
    Riceve un file Excel tramite upload e inserisce i record all'interno 
    della tabella specificata nel database.
    """
    # 1. Validazione del file: controlliamo che sia effettivamente un file Excel
    if not file.filename.endswith(('.xlsx', '.xls')):
        raise HTTPException(
            status_code=400, 
            detail="Formato file non valido. Sono ammessi solo file .xlsx o .xls."
        )
    
    try:
        # 2. Leggiamo il contenuto del file direttamente dalla memoria
        contents = await file.read()
        df = pd.read_excel(io.BytesIO(contents))
        
        # Verifichiamo che il file non sia vuoto
        if df.empty:
            raise HTTPException(status_code=400, detail="Il file Excel caricato è vuoto.")
        
        # 3. Pulizia dei dati per il database:
        # Pandas gestisce i valori vuoti come 'NaN' o 'NaT', che pyodbc non riesce a tradurre in SQL.
        # Convertiamo il DataFrame in tipo 'object' e sostituiamo i valori nulli con 'None' (che diventerà NULL in SQL).
        df = df.astype(object).where(pd.notnull(df), None)
        
        # Trasformiamo le righe del DataFrame in una lista di liste/tuple pronta per l'inserimento
        records = df.values.tolist()
        
        # 4. Costruzione della query SQL dinamica:
        # Estraiamo i nomi delle colonne dal file Excel e li racchiudiamo in parentesi quadre
        colonne = ", ".join([f"[{col}]" for col in df.columns])
        # Creiamo i segnaposto "?" in base al numero di colonne (es. ?, ?, ?)
        segnaposto = ", ".join(["?" for _ in df.columns])
        
        query = f"INSERT INTO [{nome_tabella}] ({colonne}) VALUES ({segnaposto})"
        
        # 5. Connessione al database ed esecuzione
        conn = get_connection()
        cursor = conn.cursor()
        
        # Ottimizzazione per SQL Server: velocizza drasticamente gli inserimenti multipli di pyodbc
        cursor.fast_executemany = True
        
        # Eseguiamo l'inserimento in blocco di tutti i record
        cursor.executemany(query, records)
        
        # CRUCIALI per le operazioni di scrittura (INSERT/UPDATE): confermiamo la transazione
        conn.commit()
        
        # Chiudiamo la connessione
        conn.close()
        
        return {
            "stato": "Successo",
            "messaggio": f"Importazione completata. Inseriti correttamente {len(records)} record nella tabella '{nome_tabella}'."
        }
        
    except Exception as e:
        # In caso di errore (es. colonne del file Excel che non corrispondono a quelle del DB), restituisce l'errore dettagliato
        raise HTTPException(
            status_code=500, 
            detail=f"Errore durante l'importazione nel database: {str(e)}"
        )
    
# ==========================================
# ROTTA EREDITATA DA "Salvataggio in Excel.txt"
# ==========================================

@app.get("/esporta_excel")
def esporta_excel():
    """
    Genera un file Excel contenente tutte le tabelle del database e ne avvia il download.
    """
    file_name = "Report_ScuolaDb.xlsx"
    
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Recuperiamo dinamicamente tutte le tabelle disponibili
        cursor.execute("EXEC sp_ListaTabelle")
        tabelle = [row[0] for row in cursor.fetchall()]
        
        # Creiamo un oggetto ExcelWriter tramite il motore 'xlsxwriter' per gestire fogli multipli
        write = pd.ExcelWriter(file_name, engine="xlsxwriter")
        
        for tabella in tabelle:
            # Saltiamo le tabelle di sistema interne di SQL Server per non esporre metadati inutili o protetti
            if tabella.lower() in ["sysdiagrams", "sysdiagram"]:
                continue
                
            # Interroghiamo direttamente la tabella e carichiamo il risultato in un DataFrame Pandas
            query = f"SELECT * FROM [{tabella}]"
            df = pd.read_sql(query, conn)
            
            # Gestione dei dati binari (es. immagini salvate nel DB):
            # Se la colonna contiene oggetti binari (bytes), Excel andrebbe in errore durante il salvataggio.
            # Sostituiamo questi valori con una stringa segnaposto "<BINARY DATA>".
            for col in df.columns:
                if df[col].dtype == object:
                    df[col] = df[col].apply(
                        lambda x: "<BINARY DATA>" if isinstance(x, bytes) else x
                    )
            
            # Scriviamo il DataFrame in un foglio Excel.
            # Il nome del foglio non può superare i 31 caratteri (limite intrinseco di Excel), quindi facciamo lo slicing [:31].
            # index=False rimuove la colonna degli indici numerici generata da Pandas (0, 1, 2...).
            df.to_excel(write, sheet_name=tabella[:31], index=False)
            
        # Salviamo fisicamente il file generato
        write.close()
        conn.close()
        
        # Invece di restituire un JSON, restituiamo un FileResponse che informa il browser 
        # dell'utente di scaricare il file Excel appena creato.
        return FileResponse(
            path=file_name, 
            filename=file_name, 
            media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Errore durante la generazione dell'Excel: {str(e)}")


# ==========================================
# ROTTA EREDITATA DA "CharApp.txt" (GRAFICI)
# ==========================================

# Usiamo @app.post perché l'utente ci sta INVIANDO un file (Upload).
@app.post("/genera_grafico")
async def genera_grafico(file: UploadFile = File(...), tipo_grafico: str = Form("Bar Chart")):
    """
    Riceve un file Excel, ne estrae le prime due colonne e genera un grafico al volo.
    L'interfaccia utente (Tkinter) è stata sostituita da input tramite parametri HTTP (File e Form).
    """
    
    # Controllo di validazione sull'estensione del file
    if not file.filename.endswith(('.xlsx', '.xls')):
        # Sostituisce il vecchio messagebox.showerror dell'app desktop
        raise HTTPException(status_code=400, detail="Attenzione controlla il tipo di file. Solo .xlsx o .xls ammessi.")
    
    try:
        # Leggiamo i byte del file caricato in memoria (non lo salviamo su disco)
        contents = await file.read()
        
        # Passiamo i byte direttamente a Pandas usando io.BytesIO (che simula un file in memoria)
        df = pd.read_excel(io.BytesIO(contents))
        
        # Validazione strutturale dei dati
        if df.empty or len(df.columns) < 2:
            raise HTTPException(status_code=400, detail="Il file Excel deve contenere almeno due colonne per generare il grafico.")

        # Inizializziamo l'area di plotting di Matplotlib
        fig, ax = plt.subplots(1, 1, figsize=(6, 4))
        
        # Estraiamo dinamicamente i nomi delle prime due colonne, a prescindere da come si chiamano
        col1 = df.columns[0]
        col2 = df.columns[1]

        # Logica di switch per determinare il tipo di grafico
        if tipo_grafico == "Bar Chart":
            # Per i grafici a barre e linee, forziamo l'asse X a stringa (.astype(str)) 
            # per evitare comportamenti anomali con etichette numeriche
            ax.bar(df[col1].astype(str), df[col2], color="royalblue")
            ax.set_title("Bar Chart")
        elif tipo_grafico == "Line Chart":
            ax.plot(df[col1].astype(str), df[col2], marker="o", color="green")
            ax.set_title("Line Chart")
        elif tipo_grafico == "Pie Chart":
            ax.pie(df[col2], labels=df[col1].astype(str), autopct='%1.1f%%')
            ax.set_title("Pie Chart")
        else:
            raise HTTPException(status_code=400, detail="Tipo di grafico non supportato.")

        # Invece di inserire il grafico in un widget Tkinter (FigureCanvasTkAgg), 
        # lo salviamo in un buffer di byte temporaneo (io.BytesIO).
        buf = io.BytesIO()
        plt.savefig(buf, format="png", bbox_inches='tight')
        
        # Riportiamo il "puntatore" di lettura del buffer all'inizio, altrimenti verrebbe inviato vuoto
        buf.seek(0)
        
        # Liberiamo la RAM chiudendo la figura, operazione essenziale in un ambiente server 
        # che potrebbe ricevere decine di richieste contemporanee.
        plt.close(fig) 

        # Restituiamo il buffer direttamente come un'immagine. Il browser la visualizzerà nativamente.
        return StreamingResponse(buf, media_type="image/png")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Errore durante la generazione del grafico: {str(e)}")
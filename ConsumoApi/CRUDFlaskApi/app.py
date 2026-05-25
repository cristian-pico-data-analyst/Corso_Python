# Importiamo FastAPI, il framework che gestisce le richieste web
from fastapi import FastAPI
# Importiamo la funzione che abbiamo creato nel file database.py per collegarci a SQL Server
from api.Database.db import get_connection

# Inizializziamo l'applicazione. 
# Il parametro 'title' cambia il nome che vedrai nella documentazione automatica
app = FastAPI(title="API Multi-Database")


# --- PRIMA ROTTA: Ottenere la lista di tutte le tabelle ---

# @app.get dice a FastAPI: "Quando qualcuno visita l'indirizzo /tabelle, esegui questa funzione"
@app.get("/tabelle")
def lista_tabelle():
    # 1. Apriamo la connessione al database ScuolaDb
    conn = get_connection()
    # 2. Creiamo un 'cursore', ovvero l'oggetto che esegue materialmente i comandi SQL
    cursor = conn.cursor()

    # 3. Eseguiamo una Stored Procedure presente nel tuo database
    cursor.execute("EXEC sp_ListaTabelle")
    
    # 4. fetchall() recupera tutti i risultati. Poiché ogni riga restituita dal database 
    # è una tupla (es: ("Studenti",), ("Professori",)), usiamo una 'list comprehension' 
    # per estrarre solo il primo elemento (row[0]) e creare una lista pulita di nomi.
    tabelle = [row[0] for row in cursor.fetchall()]

    # 5. Chiudiamo sempre la connessione per non sovraccaricare il server SQL
    conn.close()
    
    # 6. Restituiamo un dizionario Python. FastAPI lo trasformerà automaticamente in JSON.
    return {"tabelle": tabelle}


# --- SECONDA ROTTA: Leggere il contenuto di una tabella specifica ---

# Le parentesi graffe {nome_tabella} indicano un parametro dinamico. 
# Se visiti /tabella/Studenti, la variabile 'nome_tabella' varrà "Studenti"
@app.get("/tabella/{nome_tabella}")
def leggi_tabella(nome_tabella: str):
    conn = get_connection()
    cursor = conn.cursor()

    # Inseriamo il nome della tabella dinamicamente nella query. 
    # Le parentesi quadre [] prevengono errori se il nome della tabella contiene spazi
    query = f"SELECT * FROM [{nome_tabella}]"
    cursor.execute(query)

    # cursor.description contiene le informazioni sulle colonne (metadati).
    # Estraiamo solo il nome di ogni colonna (col[0]) e creiamo una lista.
    columns = [col[0] for col in cursor.description]
    
    # Recuperiamo tutti i dati (le righe) della tabella
    rows = cursor.fetchall()

    conn.close()

    # Questa è la parte più "densa": zip(columns, row) accoppia ogni nome di colonna 
    # al rispettivo valore di quella riga. dict() trasforma queste coppie in un dizionario.
    # Il risultato è una lista in cui ogni elemento è un dizionario (una riga del database).
    result = [dict(zip(columns, row)) for row in rows]
    
    return result
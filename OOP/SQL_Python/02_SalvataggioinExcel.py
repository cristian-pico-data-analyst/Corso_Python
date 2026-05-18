"""
Recuperare automaticamente tutte le tabelle da SQL Server con Python
"""

import pyodbc as odbc
import pandas as pd

# StrConn => per la connessione al database
strCon = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=Cristian_Pico\\SQLEXPRESS;"          # o nome server/IP
    "DATABASE=ScuolaDb;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

try:
    print("⏳ Connessione al server...")
    
    conn = odbc.connect(strCon)
    cursor = conn.cursor()

    print(f"🗃️ Recupero automaticamente delle tabelle\n")
    
    # Esecuzione della store procedure
    cursor.execute("EXEC sp_ListaTabelle")
    tabelle = [row[0] for row in cursor.fetchall()]

    print("🏹 Tabelle trovate:\n")
    for t in tabelle:
        print(f"-> {t}")
    
    # Creazione File Excel
    write = pd.ExcelWriter("Report_ScuolaDb.xlsx", engine = "xlsxwriter") # Crea un oggetto ExcelWriter tramite il motore 'xlsxwriter' per gestire e salvare i dati nel file 'ScuolaDb.xlsx'
    
    # Ciclo per ogni tabella
    for tabella in tabelle:
        print(f"Elaborazione delle tabelle: {tabella}")

        try: 
            query = f"SELECT * FROM [{tabella}]"
            df = pd.read_sql(query, conn)

            # Evita stampa di colonne binarie
            for col in df.columns:  # Passa in rassegna tutte le colonne del DataFrame, una ad una
                if df[col].dtype == object:  # Verifica se la colonna è di tipo "object" (tipo usato da Pandas per stringhe e dati complessi/binari)
                    df[col] = df[col].apply(  # Scorre e applica una trasformazione a ogni singola cella della colonna
                        lambda x: "<BINARY DATA>"  # Sostituisce il contenuto della cella con l'etichetta testuale "<BINARY DATA>"...
                            if isinstance(x, bytes) else x  # ...ma lo fa SOLO se il dato originale è di tipo "bytes" (binario), altrimenti lo lascia intatto (x)
                    )
            
            # Scrittura nel file di Excel
            df.to_excel(write, sheet_name=tabella[:31], index=False)  # Scrive i dati nell'oggetto Excel (write), nomina il foglio come la tabella e omette la colonna degli indici numerici (index=False)
            print(f"\n✅  Salvata nel foglio: {tabella[:31]}")  # Mostra a schermo un messaggio per confermare che la tabella corrente è stata salvata correttamente

        except Exception as e:
            print(f"\n❌ Errore nella tabella {tabella}: {e}")

    write.close() # Chiusura del ciclo
    print("\n📁 File Excel generato: Report_ScuolaDb.xlsx") # Conferma dell'avvenuta creazione del File Excel

except Exception as ex:
    print(f"\nErrore di connessione: {ex}")
except:
    try:
        strCon.close()
    except:
        print("\n⚠️ Impossibile chiudere la connessione")
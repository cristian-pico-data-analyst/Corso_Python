import pyodbc
#import pandas as pd

# ── Autenticazione Windows (Trusted Connection) ──
conn_str_windows = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=Cristian_Pico\\SQLEXPRESS;"          # o nome server/IP
    "DATABASE=ScuolaDb;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

# Inizio del blocco per la connessione al database
try:
    # Segnala all'utente che sta tentando di connettersi
    print(f"\n🥲  Connessione al server...")

    # Stabilisce la connessione al database utilizzando la stringa di connessione predefinita.
    # (Si presume che 'conn_str_windows' sia una variabile definita precedentemente 
    # contenente i parametri come driver, server, database, ecc.)
    conn = pyodbc.connect(conn_str_windows)
    
    # Crea un oggetto "cursore". Il cursore è lo strumento che ci permette di 
    # inviare ed eseguire le query SQL verso il database connesso.
    cursor = conn.cursor()

    # Esegue una semplice query SQL ('SELECT @@SERVERNAME') per chiedere al server il suo nome.
    # .fetchone() recupera la prima riga del risultato restituito dal database.
    # [0] estrae il primo (e unico) elemento di quella riga, ovvero il nome stesso.
    nome_server = cursor.execute('SELECT @@SERVERNAME').fetchone()[0]
    
    # Conferma visivamente all'utente che la connessione ha avuto successo, mostrando il nome del server
    print(f"\n😎 Connesso al server {nome_server}!")

    print("\nRecupera automaticamente tutte le tabelle\n")
    
    #=============== VERSIONE 1 ===============
    # Esegue una query SQL più complessa su più righe.
    # Questa query interroga 'INFORMATION_SCHEMA.TABLES', che è una vista di sistema 
    # contenente i metadati del database, per ottenere i nomi delle tabelle.
    
    # cursor.execute("""                  -- Per leggere la query su più righe si usano le triple virgolette
    #     SELECT TABLE_NAME 
    #     FROM INFORMATION_SCHEMA.TABLES
    #     WHERE TABLE_TYPE='BASE TABLE'   -- Filtra solo le tabelle reali (esclude le "Viste")
    #     ORDER BY TABLE_NAME ASC         -- Ordina i risultati in ordine alfabetico (crescente)
    #     """
    # )
    
    #=============== VERSIONE 2 ===============
    # Esecuzione della stored procedure per ottenere la lista delle tabelle
    cursor.execute("EXEC dbo.sp_ListaTabelle")

    tabelle = [row[0] for row in cursor.fetchall()]
    print("😊 Tabelle trovate")
    for row in cursor.fetchall():
        print(f"-> {row[0]}")
    
    print("⌛ Lettura delle tabelle in corso...")

    for tabella in tabelle:
        print('\n=========================\n')
        print(f'▫️ {tabella}\n')
        print('\n=========================\n')

        try:
            query = f"SELECT * FROM {tabella}"
            cursor.execute(query)

            column = [desc[0] for desc in cursor.description]
            print(f"😊 Colonne trovate:  {column}\n")
            
        except Exception:
            print("\nAttenzione\n")
    

    #=============== VERSIONE 3 - PANDAS ===============
    #df = pd.read_sql("EXEC dbo.sp_ListaTabelle", conn)
    #print(df)

    # .fetchall() estrae tutti i risultati trovati dalla query precedente 
    # e li salva nella variabile 'tabelle' (che diventerà una lista)
    #tabelle = cursor.fetchall()
    #print(f'Le Tabelle sono:\n')
    #for tabella in tabelle:
    #    print(f'▫️ {tabella[0]}')

# Se si verifica qualsiasi tipo di errore nel blocco "try" (es. server spento, credenziali errate),
# il programma salta qui invece di bloccarsi (crash).
except Exception as e:
    # Stampa un messaggio di errore personalizzato
    print("❌ Errore di connessione:")
    # Stampa il dettaglio tecnico dell'errore catturato nella variabile 'e'
    print(e)

finally:
    # Il blocco 'finally' viene eseguito SEMPRE, alla fine di tutto, 
    # indipendentemente dal fatto che ci sia stato un errore o meno.
    try:
        print("\n🧹 Pulizia delle risorse in corso...\n")

        # Controlliamo se il cursore è stato effettivamente creato prima di provare a chiuderlo
        if cursor:
            cursor.close()
            print("\n▫️  Cursore chiuso.\n")

        # Controlliamo se la connessione è stata stabilita prima di provare a chiuderla
        if conn:
            conn.close()
            print("\n🫡  Connessione al server disconnessa con successo.\n")
    except:
        print("Riprova...😒")
        pass

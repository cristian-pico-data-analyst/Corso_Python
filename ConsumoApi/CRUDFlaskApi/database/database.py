import pyodbc as odbc

def get_connection():
    connessione_cristian = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=CRISTIAN_PICO\\SQLEXPRESS;"
        "DATABASE=ScuolaDb;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )

    return odbc.connect(connessione_cristian)

def get_db():
    conn = get_connection()

    try:
        yield conn
    finally:
        conn.close()
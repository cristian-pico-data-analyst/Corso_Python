import pyodbc

# ── Autenticazione Windows (Trusted Connection) ──
conn_str_windows = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=Cristian_Pico\SQLEXPRESS;"          # o nome server/IP
    "DATABASE=ScuolaDb;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

# Connessione
conn = pyodbc.connect(conn_str_windows)
print("✅ Connesso a SQL Server!")

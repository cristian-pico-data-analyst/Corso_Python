from fastapi import FastAPI
from database import get_connection

from database import router as studenti_router

# Unica istanza FastAPI
app = FastAPI(title="API Multi-Database")

# Router ScuolaDb
app.include_router(studenti_router)


# --- API ScuolaDb ---
@app.get("/tabelle")
def lista_tabelle():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("EXEC sp_ListaTabelle")
    tabelle = [row[0] for row in cursor.fetchall()]

    conn.close()
    return {"tabelle": tabelle}


@app.get("/tabella/{nome_tabella}")
def leggi_tabella(nome_tabella: str):
    conn = get_connection()
    cursor = conn.cursor()

    query = f"SELECT * FROM [{nome_tabella}]"
    cursor.execute(query)

    columns = [col[0] for col in cursor.description]
    rows = cursor.fetchall()

    conn.close()

    result = [dict(zip(columns, row)) for row in rows]
    return result
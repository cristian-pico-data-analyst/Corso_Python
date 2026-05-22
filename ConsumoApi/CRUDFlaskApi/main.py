import os
import sys
from fastapi import APIRouter

# Questo calcola il percorso assoluto fino a 'CRUDFlaskAPI'
current_file = os.path.abspath(__file__)  # .../Routers/Studenti_Routers.py
routers_dir = os.path.dirname(current_file)  # .../Routers
crud_flask_api_dir = os.path.dirname(routers_dir)  # .../CRUDFlaskAPI

# Diciamo a Python che la cartella principale da cui cercare è 'CRUDFlaskAPI'
if crud_flask_api_dir not in sys.path:
    sys.path.append(crud_flask_api_dir)

# ORA Python troverà la cartella 'database' senza problemi!
from database.database import get_connection

router = APIRouter()

# EXEC sp_GetAllStudenti - store procedure presente su SQLServer
# Consiglio: evita gli spazi nell'URL, meglio usare 'get-all-studenti' o 'studenti'
@router.get('/studenti')
def get_all_studenti():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('EXEC sp_GetAllStudenti')
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]

    conn.close()
    return [dict(zip(columns, row)) for row in rows]
from fastapi import APIRouter
from ConsumoApi.CRUDFlaskApi.database.database import get_connection


router = APIRouter(prefix="/studenti", tags=["Studenti"])
# EXEC sp_GetAllStudenti - store procedure presente su SQLServer
@router.get('/Get All Studente')
def get_all_studenti():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('EXEC sp_GetAllStudenti')
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]

    conn.close()
    return [dict(zip(columns, row)) for row in rows]

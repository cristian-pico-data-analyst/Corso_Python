from fastapi import FastAPI

app = FastAPI()

studenti ={
    "nome": "Cristian",
    "cognome": "Pico",
    "professione": "Studente"
}

@app.get("/")
def home():
    return (f"Studente: {studenti}")

items = []

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items


# Per avviarlo, nel terminale bisogna scrivere: uvicorn app:app --reload
# Per chiudere, "Ctrl + C" nel terminale

# DA SISTEMARE
#@app.get("/studenti")
#def home(item: str) -> str:
#    if item in studenti:
#        return studenti[item]
#    return {"errore": "oggetto non trovato ❌"}

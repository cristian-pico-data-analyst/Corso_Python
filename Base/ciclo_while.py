# Creo una dictionary
studenti = {
    "Mario": 30,
    "Luca": 30,
    "Simona": 28,
    "Andrea": 25,
    "Melania": 29,
    "Cataline": 27,
    "Giovanni": 31,
    "Giuseppe": 26,
    "Mattia": 32,
    "Francesca": 24
}

# while -> ciclo che si ripete finchè una condizione è vera
nomi = list(studenti.keys())

i = 0
while i < len(nomi):
    nome = nomi[i]
    voto = studenti[nome]
    print(f"Studente: {nome} - Voto: {voto} \n")
    i += 1

"""
    Il while lavora con indici (0,1,2,3,..), mentre il dictionary no.
    Quindi trasforma la chiave in una lista

    Esempio:
    nomi = list(studenti.keys())
"""
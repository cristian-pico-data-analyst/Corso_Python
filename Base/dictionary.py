# Il dictionary è una struttura che salva dati in coppie chiave-valore.

# Creazione di una dictionary con le parentesi {}
persona = {
    "nome":  "Luca", # nome è la chiave, mentre Luca è il valore
    "età": 30, # età è la chiave, mentre 30 è il valore
    "città": "Roma", # città è la chiave, mentre Roma è il valore
    "codice_fiscale": "LCCLCA80A01H501U" # codice_fiscale è la chiave, mentre LCCLCA80A01H501U è il valore
}

# Accedere ai valori del dizionario
print(persona["nome"]) # Output: Luca

# Oppure si può accedere anche con .get() che restituisce "None" se la chiave non esiste
print(persona.get("nome")) # Output: Luca

# Modificare un valore esistente
persona["cognome"] = "Rossi"
print(persona["cognome"]) #Output: Rossi

# Aggiungere una nuova coppia chiave-valore
persona["professione"] = "Ingegnere"

# Ciclo per stampare tutte le chiavi
print(f"------ CHIAVE ------\n")
for key in persona:
    print(f"Chiave: {key}\n")

# Ciclo per stampare tutti i valori
print(f"------ VALORE ------\n")
for value in persona.values():
    print(f"Value: {value}\n")

# Ciclo for per stampare tutti le coppie chiave-valore
print(f"------ CHIAVE E VALORE ------\n")
for key, value in persona.items():
    print(f"Chiave: {key} - Valore: {value}\n")

# Esempio reale (registro studenti)
print(f"------ REGISTRO STUDENTI ------\n")
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


# Calcolare la media dei voti degli studenti
print(f"------ MEDIA STUDENTI ------\n")
media = sum(studenti.values()) / len(studenti)
print(f"La media dei voti è: {media:.2f}\n")

# Calcolare il voto massimo e minimo
print(f"------ VOTO MASSIMO E MINIMO ------\n")
massimo_voto = max(studenti.values())
minimo_voto = min(studenti.values())
print(f"Il valore massimo è {massimo_voto}\n")
print(f"Il valore minimo è {minimo_voto}\n")

# Lista nome e voto studente
for nome, voto in studenti.items():
    print(f"Nome: {nome} - Voto: {voto}\n")

# Esempio 2: Dizionario con lista di voti
print(f"------ LISTA STUDENTI ------\n")
studenti_voti = {}
studenti["Luana"] = [28,30,27]
studenti["Brenda"] = [27,28,29,30,31]
studenti["Melania"] = [25,29,30,24,27,30,24] # Facendo così ho modificato Melania
studenti["Melania"] = [25,29,30,24,27,30,24] # Facendo così ho modificato Melania
for studente, voto in studenti.items():
    print(f"Studente: {studente.upper()} ha un voto di: {voto}\n")

# Studenti sopra la media
print(f"------------ STUDENTI SOPRA/SOTTO LA MEDIA ------------\n")
for nome, voto in studenti.items():
    if voto >= media:
        print(f"I nomi degli studenti sopra la media sono: {nome}.\n")
    else:
        print(f"I nomi degli studenti sotto al media sono: {nome}.\n")

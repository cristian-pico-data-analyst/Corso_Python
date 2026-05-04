# PRIMO PROGETTO

studenti = {}

nome = input("Inserisci il nome dello studente: ")
voti_input = int(input("Inserisci il voto dello studente (esempio: 8, 30, 45, 67, ...): "))

voti = voti_input.split(",") # Esempio la split serve per dividere una stringa in una lista di stringhe, utilizzando un delimitatore
voti = [int(v) for v in voti]

studenti[nome] = voti

for nome, voti in studenti.items():
    print(f"Studente: {nome} - Voti: {voti}")

# Creo una lista di stringhe
studenti = ['Mario', 'Luca', 'Simona', 'Andrea', 'Melania']
voti = [18, 30, 26, 28, 29]

# Stampa della lista classica
print(f"----------- STUDENTI -----------\n")
print(studenti)
print(f"\n")
print(f"----------- VOTI -----------\n")
print(voti)
print(f"\n")

# Stampa della lunghezza della lista
print(f"----------- LUNGHEZZA LISTA STUDENTI -----------\n")
lunghezza = len(studenti)
print(f"La lunghezza è di {lunghezza} elementi\n")
print(f"----------- LUNGHEZZA LISTA VOTI -----------\n")
lunghezza_voti = len(voti)
print(f"La lunghezza della lista voti è di {lunghezza_voti} elementi\n")

# Stampa della lista con ciclo for per studente
print(f"----------- STUDENTI CON CICLO FOR -----------\n")
for studente in studenti:
    print(f"Studente: {studente}\n")

# Stampa della lista con ciclo for per voti
print(f"----------- VOTO CON CICLO FOR -----------\n")
for voto in voti:
    print(f"Voto: {voti}\n")

# Stampare studente e voto insieme
print(f"----------- STUDENTE CON VOTO USANDO IL CICLO FOR -----------\n")
for i in range(len(studenti)):
    print(f"Studente: {studenti[i]} - Voto: {voti[i]}\n")

# Aggiungere un elemento alla lista
print(f"----------- AGGIUNGERE NOME STUDENTE ALLA LISTA -----------\n")
studenti.append(input("Inserisci il nome dello studente: "))
print(f"\n")
print(f"----------- AGGIUNGERE VOTO STUDENTE ALLA LISTA -----------\n")
voti.append(int(input("Inserisci il voto dello studente: ")))
print(f"\n")

# Funzione zip() per unire due liste in una sola lista di tuple
print(f"----------- STUDENTE CON VOTO USANDO LA FUNZIONE ZIP -----------\n")
for studente, voti in zip(studenti, voti):
    print(f"Studente: {studente} - Voto: {voti}\n")

# Stampare in maiuscolo e minuscolo usando un ciclo for
print(f"----------- LISTA STUDENTI IN MAIUSCOLO -----------\n")
for studente in studenti:
    print(" MAIUSCOLO \n")
    print(f"Studente: {studente.upper()}\n") # Stampo il nome dello studente in maiuscolo
    print(" MINUSCOLO \n")
    print(f"Studente: {studente.lower()}\n") # Stampo il nome dello studente in minuscolo



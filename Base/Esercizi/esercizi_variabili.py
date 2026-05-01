# Esercizio 1 - Dichiarare una variabile "nome" e assegnargli il tuo nome. Mandare a schermo.
nome = 'Cristian'
print("--------- 1- NOME ---------\n")
print(f"Mi chiamo {nome}\n")

# Esercizio 2: Dichiarare una variabile "eta" e assegnargli la tua età. Mandare a schermo.
eta = 31
print("--------- 2- ETA ---------\n")
print(f"Ho {eta}\n")

# Esercizio 3: Dichiarare una variabile "pi" e assegnargli il valore di pi greco (3,14159). Mandare a schermo.
pi = 3.14159
print("--------- 3- PI-Greco ---------\n")
print(f"Il valore del PI-GRECO è uguale a {pi}\n")

# Esercizio 4: Creare una variabile "lunghezza" e assegnargli un valore, quindi riassegnare la variabile a 15. Mandare a schermo.
lunghezza = 10
print("--------- 4- LUNGHEZZA ---------\n")
print(f"La lunghezza è di {lunghezza}\n")

# Esercizio 5: Creare una variabile "nome_completo" e assegnargli una stringa contenente il tuo nome e cognome. Mandare a schermo.
cognome = "Pico"
nome_completo = nome + ' ' + cognome
print("--------- 5- NOME COMPLETO ---------\n")
print(f"Mi chiamo {nome_completo}\n")

# Esercizio 6: Creare una variabile "eta_futura" e assegnargli il valore dell'età che avrai tra 10 anni (utilizzando la variabile età già esistente). Mandare a schermo.
eta_futura = eta + 10
print("--------- 6- ETA FUTURA ---------\n")
print(f"Tra 10 anni avrò {eta_futura}\n")

# Esercizio 7: Creare delle variabili "nome", "cognome" ed "anno_di_nascita" ed assegnarle il valore dei valori. Mandare a schermo in un unico print. Sovrascrivere tutte le variabili e rimandare a schermo una seconda volta.
print("--------- 7- NOME COMPLETO E DATA DI NASCITA UTENTE ---------\n")
nome = input("Inserisci nome: ")
cognome = input("Inserisci cognome: ")
anno_nascita = input("Inserisci data di nascita: \n")
print(f"Mi chiamo {nome} {cognome}, e sono nato il {anno_nascita}\n")

# Esercizio 8: Creare una variabile eta_attuale e assegnargli il valore dell'età che hai attualmente, calcolandola in base all'anno corrente. Mandare a schermo `eta_attuale
print("--------- 8- ETA ATTUALE ---------\n")
anno_corrente = int(input("Inserisci anno corrente: "))
anno_nascita = int(input("Inserisci anno di nascit: \n"))
eta_attuale = anno_corrente - anno_nascita
print(f"La mia età ad oggi è di {eta_attuale} anni\n")
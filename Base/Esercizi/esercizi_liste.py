"""
Esercizi sulle liste
"""

# Esercizio 1: Creare una lista vuota e assegnarla a una variabile.
print("--------- LISTA ---------\n")
cibo = []
print(f'Questa lista è vuota {cibo}\n')

# Esercizio 2: Creare una lista di numeri interi da 1 a 5 e assegnarla a una variabile.
print("--------- LISTA NUMERI INTERI ---------\n")
numeri_interi = [1, 2, 3, 4, 5]
for numero_intero in numeri_interi:
    print(f"Questo numero è parte di una lista di numeri interi => {numero_intero}\n")

# Esercizio 3: Accedere all'elemento con indice 2 della lista precedente.
print("--------- ELEMENTO CON INDICE 2 ---------\n")
elemento_scelto = numeri_interi[2] # In python il conteggio parte da 0, quindi inserendo indice 2 il terminale mi stamperà 3
print(f"L'elemento con indice 2 è: {elemento_scelto}\n")

# Esercizio 4: Aggiungere un nuovo elemento "6" alla lista precedente.
print("--------- AGGIUNGO ELEMENTO 6 ---------\n")
numeri_interi.append(6) # il .append() inserisce un valore alla fine della lista che va a richiamare
numeri_interi.append(6)
for numero_intero in numeri_interi:
    print(f"Questo numero è parte di una lista di numeri interi => {numero_intero}\n")

# Esercizio 5: Rimuovere l'elemento con indice 3 dalla lista precedente.
print("--------- ELIMINO UN ELEMENTO DALL' INDICE 3 ---------\n")
numeri_interi.pop(3) # .pop() elimina un elemento dalla posizione/indice
print(f"Questo è la lista {numeri_interi} senza l'elemento all' indice 3\n") # risulterà che ha eliminato il numero 4
# numero_eliminato = numeri_interi.pop(3) # in questo modo visualizzo il numero eliminato dalla posizione 3
# print(f"Questo è il numero eliminato dalla posizione 3 => {numero_eliminato}\n") # infatti il risultato è il numero 4
# ATTENZIONE: questo comando (quello nel commento) deve essere separato da quello precedente (senza commento), sennò elimina nuovamente il valore in posizione 3

# Esercizio 6: Creare una nuova lista che contenga solo i primi tre elementi della lista precedente.
print("--------- NUOVA LISTA ---------\n")
nl_numeri_interi = numeri_interi[0:3]
print(f"Questa è una nuava lista {nl_numeri_interi}, che prendi i valori nelle prime 3 posizioni\n")

# Esercizio 7: Creare una nuova lista che contenga gli elementi con indici dispari della lista precedente.
print("--------- NUOVA LISTA CON INDICI DISPARI ---------\n")
dispari_numeri_interi = numeri_interi[1::2] 
# ATTENZIONE: mi darà solo 2 numeri, perchè la funzione dell'esercizio 5 numeri_interi.pop ha eliminato uno degli indici all'interno
# quindi i nuovi i numeri sono 1,2,3,5,6 rispettivamente nelle posizioni 0,1,2,3,4. Dalla stampa avrò come risultato i numeri [2,5]
# che sono all'interno della posizione 1,3 (che risulteranno essere le posizioni dispari della lista)
print(f"Questa è una nuova lista {dispari_numeri_interi}, prende i valori nelle posizioni dispari\n")

# Esercizio 8: Ordinare la lista precedente in ordine decrescente.
print("--------- LISTA IN ORDINE DECRESCENTE ---------\n")
numeri_interi.sort(reverse=True)
print(f"Ora la lista è in ordine decrescente => {numeri_interi}\n")

# Esercizio 9: Contare quante volte l'elemento "2" appare nella lista precedente.
print("--------- CONTARE ELEMENTO 2 ---------\n")
count_numero = numeri_interi.count(6)
print(f"Il numero 2 è presente => {count_numero}\n")
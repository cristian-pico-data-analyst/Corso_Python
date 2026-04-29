# In questo file useremo gli operatori matematici (+, -, *, /)
# e creeremo delle funzioni
# la funzione \n dopo la riga di testo permette di far saltare una riga

# somma i valori dei due numeri
num1 = 10
num2 = 3
# e poi li stampiamo sommandoli tra di loro
print(num1 + num2)

# chiediamo all'utente di inserire i numeri
num_utente1 = int(input("Inserisci il primo numero: "))
num_utente2 = int(input("Inserisci il secondo numero: "))
# e poi li stampiamo sommandoli tra di loro
print(f"Addizione: {num_utente1 + num_utente2}")
# e poi li stampiamo moltiplicandoli tra di loro
print(f"Moltiplicazione: {num_utente1 * num_utente2}")
# e poi li stampiamo sottraendoli tra di loro
print(f"Sottrazione: {num_utente1 - num_utente2}")
# e poi li stampiamo dividendoli tra di loro
print(f"Divisione: {num_utente1 / num_utente2}")

#OPPURE si può fare così
#la funzione \n dopo la riga di testo permette di far saltare una riga
somma = num_utente1 + num_utente2
sottrazione = num_utente1 - num_utente2
moltiplicazione = num_utente1 * num_utente2
divisione = num_utente1 / num_utente2
modulo = num_utente1 % num_utente2
print(f"-------------------------- SOMMA --------------------------\n") 
print(f"La somma di {num_utente1} + {num_utente2} è {somma}\n")
print(f"-------------------------- SOTTRAZIONE --------------------------\n")
print(f"La sottrazione di {num_utente1} - {num_utente2} è {sottrazione}\n")
print(f"-------------------------- MOLTIPLICAZIONE --------------------------\n")
print(f"La moltiplicazione di {num_utente1} * {num_utente2} è {moltiplicazione}\n")
print(f"-------------------------- DIVISIONE --------------------------\n")
print(f"La divisione di {num_utente1} / {num_utente2} è {divisione}\n")
print("====================== Modulo ============================\n")
print(f"Il modulo di {num1} % {num2} è {modulo}\n")

# Operatori di confronto True/False

print(5>3) #visualizza True, perchè 5 è maggiore di 3
print(5<3) #visualizza False, perchè 5 è minore di 3

#Ora chiediamo all'utente se è Vero o Falso
num_utente1 = int(input("Inserisci il primo numero da controllare: "))
num_utente2 = int(input("Inserisci il secondo numero da controllare: "))

#confronto se è maggiore
print(f"-------------------------- MAGGIORE --------------------------\n") 
maggiore = num_utente1 > num_utente2
print(f"Il numero {num_utente1} è maggiore di {num_utente2}: {maggiore}\n")

#confronto se è minore
print(f"-------------------------- MINORE --------------------------\n")
minore = num_utente1 < num_utente2
print(f"il numero {num_utente1} è minore di {num_utente2}: {minore}\n")

#confronto se è uguale
print(f"-------------------------- UGUALE --------------------------\n") #per l'uguale si usa la funzione IF/ELSE
uguale = "True" if num_utente1 == num_utente2 else "False"
print(f"Il numero {num_utente1} è uguale a {num_utente2}: {uguale}\n")

#confronto se è diverso
print(f"-------------------------- DIVERSO --------------------------\n")
diverso = num_utente1 != num_utente2
print(f"Il numero {num_utente1} è diverso da {num_utente2}: {diverso}\n")


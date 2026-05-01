"""
    IF /ELIF / ELSE (Se / Altrimenti Sé / Altrimenti ) 

    Concetto:
    Le truttutre if / else servono per far prendere decizione al programma
    
    Il compiuter valuta una condizione :
        - se è vera  👉 esegue un blocco 
        - se è falsa 👉 esegue un altro blocco
    
    if (Sé): è il punto di partenza.
            IL computer controlla se una condizione è vara.
            Se lo è, esegue il codice subito sotto
    
    elif (Altrimenti sé): Si usa quando la prima condizione (if) è falsa,
        ma vuoi controllare un'altra prima di arrenderti.
        Puoi usarlo quanti ne vuoi.
    
    else (Altrimenti): è l'utima spiaggia.
        Viene eseguito solo se tutte le condizioni
        precedenti sono risultate false.  
    
    if condizione: 
        codice se vero
    elif condizione:
        codice se vero
    else:
        codice se falso
        
        Spiegazione: 
            == → confronto
            and → entrambe vere
"""
# print("Benvenuto nel programma")

"""
numero1 = int(input("Inserisci un valore diverso da zero: "))
nome = "Catalina"

if numero1 > 0:
    print(f"Ciao {nome}")
else:
    print(f"Scelta sbagliata")
"""
"""
# Login program
nome = "Mario"
pwd  = 1234


username = input("Inserisci tuo nome: ")
password = int(input("Inserisci la password: "))

if username == nome and password == pwd:
    print("Benvenuto nel programma")
elif username != nome:
    print("Nome non trovato nel sistema")
elif username == nome and password != pwd:
    print("password errata")
else:
    print("Accesso negato!")

# Esempio Verificare il voto dello studente
voto = int(input("Inserisci un voto da controllare! "))

if voto >= 90:
    print("Ottimo, hai preso A!")
elif voto >= 80:
    print(f"{voto} Buono")
elif voto >= 70:
    print(f"{voto} Discreto")
elif voto >= 60:
    print(f"{voto} Sufficiente")
else:
    print("puoi fare meglio la prossima volta")
"""

"""
    L'annidamento(in inglese nesting) 
    si verifica quando inserisci un'istruzione (if)
    dentro un'altra istruzione if
    
    if condizione:
        codice
        
        if condizione:
            codice
        else:
    else:
        stampa
    
"""

# Numero Positivo e pari
"""  
numero = 10

if numero > 0:
    print("Il numero positivo")
    
    # Questo if è ANNIDATO dentro il primo
    if numero % 2 == 0:
        print("Ed è anche un numero pari")
    else:
        print("Ma è un numero dispari")
else:
    print("il numero è zero o negativo")
"""
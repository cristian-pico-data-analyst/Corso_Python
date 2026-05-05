# PRIMO PROGETTO
studenti = {} # lista vuota per memorizzare i dati degli studenti

while True: # fin che la condizione è vera, il ciclo continua a ripetersi
    
    # lista delle opzioni del menu, che viene mostrata all'utente ad ogni iterazione del ciclo while
    print("\n\n-------- Registro Studenti -\n\n")
    print("1. Aggiungi studente")
    print("2. Mostra registro")
    print("3. Calcola media voti")
    print("4. Promossi/Bocciati")
    print("5. Esci\n")
    
    # inserimento dell'utente per scegliere un'opzione dal menu
    scelta = input("Scegli un'opzione: ")

    # verifica se la scketa delll'utente è uguale a "1"
    if scelta == "1":
        nome = input("Inserisci il nome dello studente: ")  # chiede all'utente di inserire il nome dello studente e lo memorizza nella variabile "nome"
        
        voti = []  # dichiarazione della lista vuota dei voti 
        
        # Ciclo per chiedere all'utente di inserire 3 voti per lo studente, che vengono memorizzati nella lista "voti"
        for i in range(3):
            voto = int(input(f"Inserisci il voto {i+1} (0-10): "))  # inserimento dell'utente
            
            # verifica se il voto inserito è valido, se il voto è compreso tra 0 e 10, viene aggiunto alla lista "voti",
            # altrimenti viene stampato un messaggio di errore e il ciclo continua a chiedere un voto valido
            if 0 <= voto <= 10:
                voti.append(voto)  # aggiunge il voto valido alla lista "voti"
            else:
                print("Voto non valido. Inserisci un voto tra 0 e 10.")
                continue  # continua a chiedere un voto valido senza aggiungere il voto non valido alla lista "voti"
        
        # aggiunge il nome dello studente e la lista dei voti al dizionario "studenti",
        # dove il nome è la chiave e i voti sono il valore
        studenti[nome] = voti

    
    # elstrimenti se la scelta dell'utente è ugulale a "2"
    elif scelta == "2":
        print("\n-----Registro Studenti-----\n")
        
        # Ciclo per stamare la lista degli studenti e i loro voti, iterando attraverso il dizionario "studenti" con un ciclo for, dove "nome" è la chiave e "voti" è il valore
        for nome, voti in studenti.items():
            print(f"Studente: {nome} - Voti: {voti}")
            
    # elstrimenti se la scelta dell'utente è ugulale a "3"
    elif scelta == "3": 
        print("\n-----Media Voti-----\n")
        
        # verifica se non ci sono studenti nel registro, se la lista "studenti" è vuota, viene stampato un messaggio che indica che nessuno studente è registrato
        if not studenti:
            print("Nessuno studente registrato.")
        else:
            # ciclo per calcolare e stampare la media dei voti di ogni studente, iterando attraverso il dizionario "studenti" con un ciclo for, dove "nome" è la chiave e "voti" è il valore
            for nome, voti in studenti.items():
                media = sum(voti) / len(voti) # calcola la media dei voti dello studente, sommando tutti i voti con la funzione sum() e dividendo per il numero di voti con la funzione len()
                print(f"Studente: {nome} - Media Voti: {media:.2f}")   # 12.3456 -> 12.35
            
    # elstrimenti se la scelta dell'utente è ugulale a "4"
    elif scelta == "4":
        print("\n-----Promossi/Bocciati-----\n")
        
        # verifica se non ci sono studenti nel registro, se la lista "studenti" è vuota, viene stampato un messaggio che indica che nessuno studente è registrato
        if not studenti:
            print("Nessuno studente registrato.")
        else:
            # cicla per determinare se ogni studente è promosso/bocciato in base alla media dei voti, iterando attraverso il dizionario "studenti" con un ciclo for, dove "nome" è la chiave e "voti" è il valore
            for nome, voti in studenti.items():
                media = sum(voti) / len(voti)
                
                # verifica se la media dei voti è maggiore o ugale a 5
            if media >= 5:
                print(f"Studente: {nome} - Promosso (Media: {media:.2f})") 
            else:
                print(f"Studente: {nome} - Bocciato (Media: {media:.2f})")
        
    # elstrimenti se la scelta dell'utente è ugulale a "5"
    elif scelta == "5":
        print("Uscita dal programma.")
        break # esce dal ciclo while, terminando il programma
    else:  # altrimenti lla scelta dell'utente non è valida, viene stampato un messaggio di errore    
        print("Opzione non valida. Riprova.")

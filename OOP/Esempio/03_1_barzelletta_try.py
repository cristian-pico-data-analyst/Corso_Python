def sessione_umoristica():
    try:
        risposta = input("Vuoi sentire una barzelletta? Si o si?? ").strip().lower()
        
        if risposta == "si":
            print("Cosa fa una mucca sul divano? 🐮 Si STRAVACCA! 😂")
        
        elif risposta == "certo":
            print("Cosa fa una mucca sul divano? 🐮 Si STRAVACCA! 😂")

        elif risposta == "no":
            raise ValueError("L'utente ha rifiutato la barzelletta")
        
        elif risposta.isdigit():
            raise TypeError("L'utente ha inserito dei numeri invece di una risposta testuale")
        
        else:
            print("Eppure era una domanda semplice... 😅")
    
    except ValueError:
        print("Non sai cosa ti perdi... 😒")
    
    except TypeError:
        print("Scusa, non parlo il numerese... 😅")
    
    finally:
        print("Grazie per aver partecipato alla sessione di barzellette! 😄")

sessione_umoristica()
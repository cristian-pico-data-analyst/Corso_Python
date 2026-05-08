# Creazione di una classe chiamata Studente, che rappresenta uno studente con alcune proprietà come nome, cognome, email e telefono.
class Studente:

    # Costruttore vuoto
    #def __init__(self): 
    #    pass

    # Costruttore con parametri
    #def __init__(self, nome, cognome, email, telefono): # Proprietà della classe
    #    # Attributi (proprietà) del costruttore della classe
    #    self._nome    = nome # self è un riferimento all'istanza corrente della classe, e viene usato per accedere alle variabili che appartengono alla classe. In questo caso, stiamo creando una variabile di istanza chiamata nome e assegnandole il valore del parametro nome passato al costruttore.
    #    self._cognome = cognome # Stiamo creando una variabile di istanza chiamata cognome e assegnandole il valore del parametro cognome passato al costruttore.
    #    self._email   = email # Stiamo creando una variabile di istanza chiamata email e assegnandole il valore del parametro email passato al costruttore.
    #    self._telefono = telefono # Stiamo creando una variabile di istanza chiamata telefono e assegnandole il valore del parametro telefono passato al costruttore.
#
    ## Costruttore che ci restituisce la stringa
    #def __str__(self):
    #    return f"{self._nome} {self._cognome} {self._email} {self._telefono}"
    

# Inserisci_dati()
    def __inserisci_dati__(self):
        self._nome = input("Inserisci tuo nome: ")
        self._cognome = input("Inserisci il tuo cognome: ")
        self._email = input("Inserisci la tua email: ")
        self._telefono = input("Inserisci il tuo numero di telefono: ")
# Costruttore che ci restituisce la stringa
    def __str__(self):
        return f"{self._nome} {self._cognome} {self._email} {self._telefono}"
    
    def Saluta(self):
        print("Ciao, mi chiamo")

class App_studenti:
    def __init__(self):
        studente = Studente()
        studente.__inserisci_dati__()
        studente.Saluta()
        print(studente)
App_studenti()

#class Stampa:
#       def __init__(self):
#           nome = input("Inserisci il tuo nome: ")
#           cognome = input("Inserisci il tuo cognome ")
#           email = input("Inserisci la tua email: ")
#           telefono = input("Inserisci il tuo numero di telefono: ")
#           
#           studente = Studente(nome, cognome, email, telefono)
#       
#           print(f"Registro studenti: {studente}")
#
#Stampa()


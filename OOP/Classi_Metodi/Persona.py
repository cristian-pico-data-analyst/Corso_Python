class Persona:
    def __init__(self, nome, cognome, email, telefono): # Proprietà della classe
        self.nome = nome # self è un riferimento all'istanza corrente della classe, e viene usato per accedere alle variabili che appartengono alla classe. In questo caso, stiamo creando una variabile di istanza chiamata nome e assegnandole il valore del parametro nome passato al costruttore.
        self.cognome = cognome # Stiamo creando una variabile di istanza chiamata cognome e assegnandole il valore del parametro cognome passato al costruttore.
        self.email = email # Stiamo creando una variabile di istanza chiamata email e assegnandole il valore del parametro email passato al costruttore.
        self.telefono = telefono # Stiamo creando una variabile di istanza chiamata telefono e assegnandole il valore del parametro telefono passato al costruttore.

    

studente = Persona("Cristian", "Rordi", "cristian.rordi@example.com", "3426178345") # Creazione di un'istanza della classe Persona, passando i valori per nome, cognome, email e telefono al costruttore.

print(studente.nome) # Accesso alla proprietà nome dell'istanza studente e stampa del suo valore.
print(studente.cognome) # Accesso alla proprietà cognome dell'istanza   studente e stampa del suo valore.
print(studente.email) # Accesso alla proprietà email dell'istanza studente e stampa del suo valore.
print(studente.telefono) # Accesso alla proprietà telefono dell'istanza studente e stampa del suo valore.
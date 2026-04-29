"""
Variabili e tipi di dati

"""
nome = "Cristian" # è una str (string), quindi insieme di testo
cognome = "Pico" # è una str (string), quindi insieme di testo
eta = 31 # int (integer), quindi un numero
stipendio = 1.500 # float (decimal)
attivo = True # bool (boolean), che restituisce Vero o Falso

# stampa con la concatenazione
print('Ciao mi chiamo ' + nome + ' ' + cognome + ' ed ho ' + str(eta) + ' anni'); 

# Restituire la tipologia di variabile
print('tipo del nome => ' + str(type(nome)) + ' = string') # questo restituisce il tipo della variabile string

print('tipo dell\' età => ' + str(type(eta)) + ' = int') # questo restituisce il tipo della variabile int

print('tipo dello stipendio => ' + str(type(stipendio)) + ' = float') # questo restituisce il tipo della variabile float
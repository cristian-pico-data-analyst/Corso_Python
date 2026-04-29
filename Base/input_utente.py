# Far inserire dati all'utente
# usando la funzione input(), che restituisce sempre testo

# SPIEGAZIONE DEL COMANDO INPUT
nome = input('Come ti chiami? ')
print('Ciao mi chiamo', nome, ', piacere!') 
# prima mi visualizza la domanda "Come ti chiami ?"
# dove poi mi da la possibilità di scrivere il nome, 
# che poi successivamente mi stamperà con il messaggio messo tra parentesi
print(f"{nome}, come stai ?'")
#ed infine posso anche concatenare con la funzione f

# Usiamo la funzione INPUT anche per l'età
eta = int(input("Quanti anni hai ? "))
print(f"Hai {eta} anni. L\'anno prossimo avrò {eta+1} anni ")

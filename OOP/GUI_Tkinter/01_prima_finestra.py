import tkinter as tk

root = tk.Tk()

# Personalizza la finestra (Widget) - Imposto un titolo
root.title("La mia prima applicazione")

# Imposta la dimensione della finestra a 500 pixel di larghezza e 400 pixel di altezza
root.geometry("500x400")

# Imposta la dimensione della finestra a 500 pixel di larghezza e 400 pixel di altezza, 
# e posiziona la finestra a 100 pixel dal bordo sinistro dello schermo e 100 pixel dal bordo superiore dello schermo
root.geometry("500x400+100+100")

# Imposta il colore di sfondo della finestra a un colore beige chiaro utilizzando il codice esadecimale
root.configure(bg="#F5F5DC") 

# DISATTIVATO - Impedisce all'utente di ridimensionare la finestra sia in larghezza che in altezza
#root.resizable(False, False)

# DISATTIVATO - Imposta la dimensione minima della finestra a 300 pixel di larghezza e 200 pixel di altezza
# root.minsize(300, 200) 

root.mainloop()


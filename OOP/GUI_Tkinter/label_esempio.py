import tkinter as tk

root = tk.Tk()
root.title("Hello World!")
root.geometry("500x400")
root.configure(bg="#F5F5DC")

# Creo una label
label = tk.Label(
    root,                                 # Contenitore padre
    text="Ciao a tutti :)",               # Inserisco il messaggio
    font=("Times New Roman", 25, "bold"), # (font, dimensione, stile)
    fg="#ffffff",                       # Colore testo (foreground)
    bg="#9CB388",                       # Colore sfondo
    cursor="hand2"                        # Imposto la tipologia di cursore
).pack(pady=50)

root.mainloop()
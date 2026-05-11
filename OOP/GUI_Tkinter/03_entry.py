import tkinter as tk

root = tk.Tk()

# Titolo della finestra
root.title("Entry form con Tkinter")

# Dimensione della finestra
root.geometry("350x250")

# Colore dello sfondo finestra
root.configure(bg="#0A9142")

# Creazione entry
entry = tk.Entry(
    root,
    width=30,
    font=("Roboto", 15)
)
entry.insert(0, "Inserisci il tuo nome") # Inserisce un testo di defaut all'interno dell'entry
entry.pack(pady=20)

# Metodo che legge i valori inseriti dall'utente
def leggi_testo():
    nome = entry.get() # Legge il testo inserito dall'utente
    print(f"Ti chiami {nome}")

# Crea il bottone Salva
button = tk.Button(
    root,
    text="Salva",
    command=leggi_testo,  # funzione da chiamare al click
) 
button.pack(pady=10)

# AVvia app
root.mainloop()



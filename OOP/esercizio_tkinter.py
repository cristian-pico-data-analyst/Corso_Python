"""
ESERCIZIO E CONSEGNA DA FARE PER LUNEDÌ: 😉
Crea una applicazione usando Tkinter + OOP come abbiamo visto oggi con:
Requisiti:
1️⃣ Finestra con: Titolo, Dimensione fissa, Colore sfondo

2️⃣ Una Label con scritto: "Benvenuto Studente"

3️⃣ Un bottone: Saluta

4️⃣ Quando clicchi il bottone mostra un popup con: "Ciao, benvenuto nel corso Python!"

REGOLE:
❌ NON usare funzioni fuori dalla classe
✔️ tutto deve stare dentro una classe App
"""

import tkinter as tk
from tkinter import messagebox 

class App:

    # CREIAMO I COSTRUTTORE PER L'OGGETTO
    def __init__(self, root):
        self.root = root

    # CREAZIONE DELLA FINESTRA
        self.root.title("Welcome!")
        self.root.geometry("500x400")
        self.root.resizable(False, False) # Rendiamo la dimensione fissa
        self.root.configure(bg="#36362F")

    # CREAZIONE DELLA LABEL
        self.label = tk.Label(
            self.root,
            text="Welcome",
            font=("Courier New", 25, "bold"),
            fg="#ffffff",
            bg="#847242",
            cursor="trek"
        )
        self.label.pack(pady=50)

    # CREAZIONE DEL BOTTONE
        self.btn = tk.Button(
            self.root,
            text = "Hello :D",
            command = self.mostra_popup,
            fg="#ffffff",
            bg="#847242",
            font=("Courier New", 15, "bold"),
            padx=30,
            pady=20,
            relief="flat",
            cursor="dotbox"
        )
        self.btn.pack(pady=50)
    
    # METODO PER MOSTRARE IL MESSAGGIO DI POPUP
    def mostra_popup(self):
        messagebox.showinfo("Hi :D", "Hello, this is part of Python course, and you're welcome!")

# --- Avvio dell'applicazione ---
# QUESTO BLOCCO PREPARA LA CLASSE E INIZIALIZZA IL PROGRAMMA
if __name__ == "__main__":
    finestra_principale = tk.Tk()
    app = App(finestra_principale)
    finestra_principale.mainloop()

"""
ESERCIZIO E CONSEGNA DA FARE PER LUNEDÌ: 😉
Crea una applicazione usando Tkinter + OOP come abbiamo visto oggi con:
Requisiti:
1️⃣ finestra con: Titolo, Dimensione fissa, Colore sfondo

2️⃣ una Label con scritto: Benvenuto Studente

3️⃣ un bottone: Saluta

4️⃣ quando clicchi il bottone mostra un popup con: Ciao, benvenuto nel corso Python!

REGOLE:
❌ NON usare funzioni fuori dalla classe
✔️ tutto deve stare dentro una classe App
"""

import tkinter as tk
from tkinter import messagebox 

class App:
    # Creiamo il costruttore per l'oggetto
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
            text="Benvenuto Studente",
            font=("Times New Roman", 25, "bold"),
            fg="#ffffff",
            bg="#847242",
            cursor="hand2"
        )
        self.label.pack(pady=50)

    # CREAZIONE DEL BOTTONE PARTE 2
        self.btn = tk.Button(
            self.root,
            text = "Saluta",
            command = self.mostra_popup,
            fg="#ffffff",
            bg="#847242",
            font=("Arial", 15, "bold"),
            padx=20,
            pady=10,
            relief="flat",
            cursor="hand2"
        )
        self.btn.pack(pady=50)
    
    # METODO PER IL POPUP
    def mostra_popup(self):
        messagebox.showinfo("Saluto", "Ciao, benvenuto nel corso Python!")

# --- Avvio dell'applicazione ---
# Questo blocco istanzia la classe e fa partire il programma
if __name__ == "__main__":
    finestra_principale = tk.Tk()
    app = App(finestra_principale)
    finestra_principale.mainloop()

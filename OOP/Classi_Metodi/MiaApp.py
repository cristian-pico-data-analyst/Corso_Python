import tkinter as tk
from tkinter import messagebox

# =========================================
# Classe principale della nostra applicazione
# =========================================
class MiaApp:

    # Metodo costruttore
    # Viene eseguito automaticamente
    # quando creiamo l'oggetto della classe
    def __init__(self, root):

        # Salviamo la finestra principale
        self.root = root

        # =========================================
        # CONFIGURAZIONE FINESTRA
        # =========================================

        # Titolo della finestra
        self.root.title("Applicazione OOP con Tkinter")

        # Dimensione finestra
        # larghezza x altezza
        self.root.geometry("500x300")

        # Colore sfondo
        self.root.configure(bg="#1e1e1e")

        # Blocca il ridimensionamento finestra
        # width=False  -> non cambia larghezza
        # height=False -> non cambia altezza
        self.root.resizable(False, False)

        # =========================================
        # LABEL TITOLO
        # =========================================

        # Label = testo mostrato nella finestra
        self.titolo = tk.Label(

            # finestra dove mettere il widget
            root,

            # testo mostrato
            text="Benvenuto nella mia App",

            # font (tipo, dimensione, stile)
            font=("Arial", 18, "bold"),

            # colore testo
            fg="white",

            # colore sfondo
            bg="#1e1e1e"
        )
        # pack() serve per mostrare il widget
        self.titolo.pack(pady=30)

        # =========================================
        # BOTTONE
        # =========================================

        self.btn = tk.Button(

            root,

            # testo bottone
            text="Mostra Messaggio",

            # funzione collegata al click
            command=self.mostra_messaggio,

            # stile bottone
            font=("Arial", 12),

            bg="#4CAF50",
            fg="white",

            padx=15,
            pady=8
        )
        self.btn.pack()

    # =========================================
    # METODO DELLA CLASSE
    # =========================================

    # Questo metodo viene eseguito
    # quando clicchiamo il bottone
    def mostra_messaggio(self):

        messagebox.showinfo(

            # titolo popup
            "Messaggio",

            # messaggio popup
            "Ciao studente 👋\nBenvenuto nel corso Tkinter OOP"
        )


# =========================================
# AVVIO PROGRAMMA
# =========================================

if __name__ == "__main__":

    # Creazione finestra principale
    messaggio = tk.Tk()

    # Creazione oggetto della classe
    app = MiaApp(messaggio)

    # Mantiene la finestra aperta
    messaggio.mainloop()
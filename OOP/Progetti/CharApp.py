import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class CharApp(tk.Tk):
    """
    Classe principale dell'applicazione per la visualizzazione di grafici da file Excel.
    Eredita da tk.Tk per sfruttare i principi della programmazione a oggetti (OOP)
    nella gestione della finestra principale.
    """
    def __init__(self):
        super().__init__()

        # Configurazione base della finestra principale
        self.title("Graphic Application Excel")
        self.geometry("1000x650")

        # Inserisco un'icona gif personalizzata
        icona = tk.PhotoImage(file="C:/Users/crist/Desktop/Corso_Python/OOP/Progetti/laptop.png")
        self.iconphoto(False, icona)

        # Inizializzazione della variabile per il DataFrame (vuoto all'avvio)
        self.df = None 

        # Richiamo il metodo per creare l'interfaccia utente
        self.create_widget()

    def create_widget(self):
        """Definisce e posiziona tutti i widget (pulsanti, etichette, menu) nella finestra."""
        
        # Pulsante per caricare il file Excel
        ttk.Button(
            self,
            text="📂 Carica File Excel",
            command=self.load_excel
        ).pack(pady=10)

        # Variabile Tkinter per memorizzare la selezione corrente del tipo di grafico
        self.char_type = tk.StringVar(value="Bar Chart")

        # Etichetta descrittiva per il menu a tendina
        ttk.Label(self, text="📊 Tipo Grafico: ", font=("Helvetica", 12)).pack()

        # Menu a tendina (Combobox) per selezionare il tipo di grafico
        lista_grafici = ["Bar Chart", "Line Chart", "Pie Chart"]
        ttk.Combobox(
            self,
            textvariable=self.char_type,
            values=lista_grafici,
            state="readonly",
            width=20
        ).pack(pady=10)
        
        # Pulsante per avviare la funzione di generazione del grafico
        self.btn = ttk.Button(self, text="Genera Grafico", command=self.generate_chart)
        self.btn.pack(pady=10)

        # Frame dedicato a contenere il grafico che verrà generato
        self.chart_area = tk.Frame(self)
        self.chart_area.pack(fill="both", expand=True)

    def load_excel(self):
        """Apre una finestra di dialogo per selezionare un file Excel e lo carica tramite pandas."""
        file_path = filedialog.askopenfilename(
            title="Selezione File Excel",
            filetypes=[("Excel files", "*.xlsx", "*.xls")]
        )

        # Se l'utente chiude la finestra di dialogo senza selezionare nulla, interrompe l'esecuzione
        if not file_path:
            return

        try:
            # Lettura del file Excel e assegnazione al DataFrame della classe
            self.df = pd.read_excel(file_path)
            messagebox.showinfo("✅ Successo", "File Excel caricato correttamente.")
            
            # Stampa in console le prime righe del DataFrame per verifica/debug
            print(self.df.head()) 
        except Exception as e:
            # Gestione delle eccezioni per eventuali errori di lettura o formato
            messagebox.showerror("❌ Errore", f"Impossibile caricare il file: {e}")

    def generate_chart(self):
        """Prepara l'area e genera il grafico in base al tipo selezionato (funzione da terminare)."""
        
        # Controllo di sicurezza: verifica che i dati siano stati precedentemente caricati
        if self.df is None:
            messagebox.showwarning("⚠️ Attenzione", "Devi prima caricare un file Excel.")
            return
        
        # Pulizia dell'area del grafico per rimuovere eventuali grafici o widget precedenti
        for widget in self.chart_area.winfo_children():
            widget.destroy()

        # DA CONTINUARE

        # Estrazione dei nomi delle prime quattro colonne dal DataFrame
        col1 = self.df.columns[0]
        col2 = self.df.columns[1]
        col3 = self.df.columns[2]
        col4 = self.df.columns[3]

# Punto di ingresso dell'applicazione
if __name__ == "__main__":
    app = CharApp()
    app.mainloop()
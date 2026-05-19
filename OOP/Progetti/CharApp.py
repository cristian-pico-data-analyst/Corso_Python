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

        # Inserisco un'icona personalizzata (assicurati che il percorso esista)
        try:
            icona = tk.PhotoImage(file="C:/Users/crist/Desktop/Corso_Python/OOP/Progetti/laptop.png")
            self.iconphoto(False, icona)
        except tk.TclError:
            print("Attenzione: Impossibile trovare l'icona specificata. Verrà usata quella di default.")

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
            # Corretto: le estensioni multiple si mettono in una sola stringa separate da spazio
            filetypes=[("Excel files", "*.xlsx *.xls")] 
        )

        # Se l'utente chiude la finestra di dialogo senza selezionare nulla
        if not file_path:
            return "Attenzione controlla il tipo di file"

        try:
            # Lettura del file Excel e assegnazione al DataFrame della classe
            self.df = pd.read_excel(file_path)
            messagebox.showinfo("✅ Successo", "File Excel caricato correttamente.")
            
            # Stampa in console le prime righe del DataFrame per verifica/debug
            print(self.df.head()) 
        except Exception as e:
            # Gestione delle eccezioni per eventuali errori di lettura o formato
            messagebox.showerror("❌ Errore", f"Impossibile caricare il file:\n{e}")

    def generate_chart(self):
        """Prepara l'area e genera il grafico in base al tipo selezionato."""
        
        # Controllo di sicurezza: verifica che i dati siano stati precedentemente caricati
        if self.df is None:
            messagebox.showwarning("⚠️ Attenzione", "Devi prima caricare un file Excel.")
            return
        
        # Pulizia dell'area del grafico per rimuovere eventuali grafici o widget precedenti
        for widget in self.chart_area.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(1,1, figsize=(6, 4))

        # Estrazione dei nomi delle prime due colonne dal DataFrame
        col1 = self.df.columns[0]
        col2 = self.df.columns[1]

        # Corretto: Bisogna usare self.char_type.get() invece di self.df.chart_type.get()
        chart = self.char_type.get()

        if chart == "Bar Chart":
            ax.bar(self.df[col1].astype(str), self.df[col2], color="royalblue")
            ax.set_title("Bar Chart")
        elif chart == "Line Chart":
            ax.plot(self.df[col1].astype(str), self.df[col2], marker="o", color="green")
            ax.set_title("Line Chart")
        elif chart == "Pie Chart":
            ax.pie(self.df[col2], labels=self.df[col1], autopct='%1.1f%%')
            ax.set_title("Pie Chart")

        # Inserimento grafico in Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.chart_area)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

# Punto di ingresso dell'applicazione
if __name__ == "__main__":
    app = CharApp()
    app.mainloop()
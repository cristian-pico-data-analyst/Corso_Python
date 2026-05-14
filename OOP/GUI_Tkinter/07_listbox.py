import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        """Costruttore della classe: inizializza la finestra e l'interfaccia."""
        # ==========================================
        # 1. CONFIGURAZIONE FINESTRA PRINCIPALE
        # ==========================================
        self.root = root
        self.root.title("TO DO LIST!")
        self.root.geometry("600x500")
        self.root.config(bg="#0A2F3C")

        # INSERISCO UNA LABEL
        tk.Label(
            self.root,                               # Contenitore padre
            text="TO DO LIST!",                      # Inserisco il messaggio
            font=("Lora", 20, "bold"),               # (font, dimensione, stile)
            fg="#ffffff",                            # Colore testo (foreground)
            bg="#0A2F3C",                            # Colore sfondo
            cursor="hand2"                           # Imposto la tipologia di cursore
        ).pack(pady=50)

        # ==========================================
        # 2. CREAZIONE INTERFACCIA GRAFICA (UI)
        # ==========================================

        # --- A. Casella di Input (Entry) ---
        # Usiamo self.entry perché ci servirà leggerla/modificarla in altre funzioni
        self.entry = tk.Entry(
            self.root,
            font=("Lora", 10),
            width=25
        )
        self.entry.pack(pady=20)

        # --- B. Sezione Bottoni ---
        frame_btn = tk.Frame(self.root, bg="#0A2F3C")
        frame_btn.pack(pady=10)

        # I comandi ora puntano a self.nome_funzione
        # Bottone AGGIUNGI
        tk.Button(
            frame_btn, 
            text="Aggiungi", 
            command=self.create, 
            font=("Lora", 10), 
            width=10
        ).grid(row=0, column=1, padx=5, pady=5)
        
        # Bottone MOSTRA
        tk.Button(
            frame_btn, 
            text="Mostra", 
            command=self.read, 
            font=("Lora", 10), 
            width=10
        ).grid(row=0, column=2, padx=5, pady=5)
        
        # Bottone AGGIORNA   
        tk.Button(
            frame_btn, 
            text="Aggiorna", 
            command=self.update, 
            font=("Lora", 10), 
            width=10
        ).grid(row=0, column=3, padx=5, pady=5)
        
        # Bottone ELIMINA
        tk.Button(
            frame_btn, 
            text="Elimina", 
            command=self.delete, 
            font=("Lora", 10), 
            width=10
        ).grid(row=0, column=4, padx=5, pady=5)

        # --- C. Sezione Lista e Scrollbar ---
        frame_list = tk.Frame(self.root, bg="#0A2F3C")
        frame_list.pack(pady=20)

        self.scrollbar = tk.Scrollbar(frame_list, orient="vertical")
        
        # Usiamo self.lb per potervi accedere nei metodi CRUD
        self.lb = tk.Listbox(
            frame_list, 
            height=14,
            width=50,
            font=("Lora", 10),
            yscrollcommand=self.scrollbar.set,
            selectmode=tk.SINGLE
        ) 

        self.scrollbar.config(command=self.lb.yview)
        self.lb.pack(side="left")
        self.scrollbar.pack(side="right", fill="y")

        # ==========================================
        # 3. COLLEGAMENTO EVENTI
        # ==========================================
        self.lb.bind("<<ListboxSelect>>", self.carica_in_entry)


    # ==========================================
    # 4. DEFINIZIONE DEI METODI DELLA CLASSE (CRUD)
    # ==========================================

    def create(self):
        """Aggiunge una nuova attività alla lista."""
        testo = self.entry.get().strip()
        if testo:
            self.lb.insert(tk.END, testo)  
            self.entry.delete(0, tk.END)   
        else:
            messagebox.showwarning("ATTENZIONE!", "Inserisci un'attività")

    def read(self):
        """Mostra in un popup l'attività attualmente selezionata."""
        idx = self.lb.curselection()    
        if idx:
            selected_activity = self.lb.get(idx[0])
            messagebox.showinfo("INFO", f"Attività: {selected_activity}")
        else:
            messagebox.showwarning("ATTENZIONE", "Nessuna attività selezionata")

    def update(self):
        """Sostituisce l'attività selezionata con il nuovo testo dell'Entry."""
        idx = self.lb.curselection()
        nuovo_testo = self.entry.get().strip()
        if not idx:
            messagebox.showwarning("ATTENZIONE!", "Seleziona un'attività da aggiornare")
        elif not nuovo_testo:
            messagebox.showwarning("ATTENZIONE!", "Inserisci il nuovo testo per l'attività")
        else:
            self.lb.delete(idx[0])              
            self.lb.insert(idx[0], nuovo_testo) 
            self.entry.delete(0, tk.END)        
        
    def delete(self):
        """Elimina l'attività selezionata dalla lista."""
        idx = self.lb.curselection()    
        if idx:
            self.lb.delete(idx[0])
            self.entry.delete(0, tk.END) 
        else:
            messagebox.showwarning("ATTENZIONE!", "Nessuna attività selezionata")

    def carica_in_entry(self, event):
        """Copia automaticamente il testo dell'attività cliccata nell'Entry."""
        idx = self.lb.curselection()
        if idx:
            testo_selezionato = self.lb.get(idx[0])
            self.entry.delete(0, tk.END)            
            self.entry.insert(0, testo_selezionato) 


# ==========================================
# AVVIO DELL'APPLICAZIONE
# ==========================================
if __name__ == "__main__":
    # 1. Creiamo la finestra principale
    finestra_principale = tk.Tk()
    
    # 2. Creiamo un'istanza della nostra classe passando la finestra
    app = ToDoApp(finestra_principale)
    
    # 3. Avviamo il loop del programma
    finestra_principale.mainloop()
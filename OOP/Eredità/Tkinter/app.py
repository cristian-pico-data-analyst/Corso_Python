# Importazione dei pacchetti
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import random

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class App:
    def __init__(self):
        # Finestra principale
        self.root = tk.Tk()
        self.root.title ("Grafico con Tkinter, Matplotlib e OOP")
        self.root.geometry("800x600")

        # Frame superiore (bottoni)
        top_frame = tk.Frame(self.root)
        top_frame.pack(pady=20)

        # Bottone per generare il grafico
        btn = tk.Button(
            top_frame,
            text="Genera grafico",
            command=self.genera_grafico
        )
        btn.pack()

        # Frame per il grafico
        self.graph_frame = tk.Frame(self.root)
        self.graph_frame.pack(fill="both", expand=True)

    def genera_grafico(self):
        # Cancella il grafico precedente
        for widget in self.graph_frame.winfo_children():
            widget.destroy()
        
        # Esempio di dati o db/json, Excel, CSV, PDF, DOC...
        x = sorted(random.sample(range(1, 1000), 10)) # 10 numeri unici tra 1 e 999, ordinati
        y = [random.randint(10, 1000) for _ in range(10)] # 10 numeri casuali tra 10 e 1000

        # Creazione della figura Matplot
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(x,y, marker='o', linestyle='-')
        ax.set_title("Andamento valori")
        ax.set_xlabel("Etichetta X")
        ax.set_ylabel("Etichetta Y")

        # Grafico Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()

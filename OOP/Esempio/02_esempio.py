import tkinter as tk
from tkinter import ttk, messagebox

class button_esempio:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Esempio con classe")
        
        self.root.geometry("800x750")
        
        self.root.configure(bg="#847242")
        
        self.root.resizable(False, True)
        
        self.root.minsize(350, 500)
        
        buttone = tk.Button(
            self.root,
            text='Cliccami!',
            command=self.saluta
            )
        
        buttone.pack(pady=30)

        self.label = tk.Label(
            self.root,
            text='Benvenuto',
            font=("Arial", 20, 'bold'),
            fg="#ffffff",
            bg="#847242",
            cursor="hand2"
        )
        self.label.pack(pady=50)
      
    def salutaCatalina(self):
        messagebox.showinfo(

            # titolo popup
            "Saluti",

            # messaggio popup
            "Ciao!\n Benvenuto nel corso Python! 😎😎😎"
        )
        
    def saluta(self):
        self.label.config(text = "E' stato un piacere")

    def avvia(self):
        self.root.mainloop()


class esegui():
    app = button_esempio()
    app.avvia()
    
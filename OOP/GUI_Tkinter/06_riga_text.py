import tkinter as tk

root = tk.Tk()

# Crea il Text (larghezza in caratteri, altezza in righe)
txt = tk.Text(root, width=40, height=8, font=("Consolas", 12))
txt.pack(padx=10, pady=10)

# Inserisci testo da codice
txt.insert(tk.END, "Prima riga\nSeconda riga\n")

# Leggi tutto il contenuto
contenuto = txt.get("1.0", tk.END)   # "1.0" = riga 1, colonna 0

# Leggi una riga specifica
riga2 = txt.get("2.0", "2.end")

# Cancella tutto
txt.delete("1.0", tk.END)

# Rendi il testo di sola lettura
txt.config(state=tk.DISABLED)

root.mainloop()
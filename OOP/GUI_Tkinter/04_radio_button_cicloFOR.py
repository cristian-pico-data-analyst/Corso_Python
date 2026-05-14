import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title("Radio Button")
root.geometry("800x600")
root.configure(bg="#ffffff")
root.resizable(True, True)

# Creare una lista di linguaggi
linguaggi={
    ("Python", "Python"),
    ("Java", "Java"),
    ("JavaScript", "JavaS"),
    ("C++", "C++"),
    ("SQL Server", "t-SQL"),
    ("R", "R"),
    ("Machine Learning", "Machine Learning"),
    ("CSS", "C-SHARP"),
    ("HTML", "HTML"),
    ("C#", "C#"),
    ("Delphy", "Delphy"),
}

# Radiobutton — variabile collegata StringVar
var_radio = tk.StringVar(value="Python")

# | ================================= CON CICLO FOR ================================= |
for testo, valore in linguaggi: # ESEMPIO logico: <for "Python", "Python" in linguaggi> -> vado a richiamare la stringa linguaggi preparata precedentemente
    tk.Radiobutton(
        root,
        text = testo,
        font=("Roboto", 10, "bold"),
        variable=var_radio,
        value=valore,
        fg="#7D3FA1",
        bg="#ffffff"
    ).pack(pady=5, padx=5, anchor="w")


# Checkbutton — variabile collegata BooleanVar
var_check = tk.BooleanVar()
check = tk.Checkbutton(root, font="Roboto", text="Accetta termini", variable=var_check, bg="#7D3FA1",fg="#ffffff")
check.pack()

"""
| ================================= SENZA CICLO FOR ================================= |
tk.Radiobutton(root, text="Python", variable=var_radio, value="Python").pack(pady=5)
tk.Radiobutton(root, text="Java",variable=var_radio, value="Java").pack(pady=5)
tk.Radiobutton(root, text="C++",variable=var_radio, value="C++").pack(pady=5)
tk.Radiobutton(root, text="AI",variable=var_radio, value="AI").pack(pady=5)
tk.Radiobutton(root, text="R",variable=var_radio, value="R").pack(pady=5)
tk.Radiobutton(root, text="Machine Learning",variable=var_radio,value="Machine Learning").pack(pady=5)
tk.Radiobutton(root, text="CSS",variable=var_radio, value="CSS").pack(pady=5)
tk.Radiobutton(root, text="HTML",variable=var_radio, value="HTML").pack(pady=5)
tk.Radiobutton(root, text="C#",variable=var_radio, value="C#").pack(pady=5)
"""

# Preparo il costruttore che mi mostrerà il messaggio in una messagebox
def mostra():
    messagebox.showinfo("Selected Button", f"Accetta termini: {var_check.get()}\nLinguaggio: {var_radio.get()}")


tk.Button(root, text="Mostra selezione", command=mostra, bg="#7D3FA1",fg="#ffffff").pack(pady=10)
root.mainloop()
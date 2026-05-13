import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title("Radio Button")
root.geometry("700x400")
root.configure(bg="#ffffff")

# Creare una lista di linguaggi
linguaggi ={
    ("Python", ""),
    ("Java", ""),
    ("C++", ""),
    ("AI", ""),
    ("R", ""),
    ("Machine Learning", ""),
    ("CSS", ""),
    ("HTML", ""),
    ("C#", "")
}

# ciclo for per recuperare il testo e il valore

# Checkbutton — variabile collegata BooleanVar - DA ELIMINARE DOPO AVER FATTO CICLO FOT
var_check = tk.BooleanVar()
check = tk.Checkbutton(root, text="Accetta termini", variable=var_check)
check.pack()

# Radiobutton — variabile collegata StringVar
var_radio = tk.StringVar(value="python")
tk.Radiobutton(root, text="Python", variable=var_radio, value="Python").pack(pady=5)
tk.Radiobutton(root, text="Java",variable=var_radio, value="Java").pack(pady=5)
tk.Radiobutton(root, text="C++",variable=var_radio, value="C++").pack(pady=5)
tk.Radiobutton(root, text="AI",variable=var_radio, value="AI").pack(pady=5)
tk.Radiobutton(root, text="R",variable=var_radio, value="R").pack(pady=5)
tk.Radiobutton(root, text="Machine Learning",variable=var_radio,value="Machine Learning").pack(pady=5)
tk.Radiobutton(root, text="CSS",variable=var_radio, value="CSS").pack(pady=5)
tk.Radiobutton(root, text="HTML",variable=var_radio, value="HTML").pack(pady=5)
tk.Radiobutton(root, text="C#",variable=var_radio, value="C#").pack(pady=5)

def mostra():
    messagebox.showinfo("Selected Button", f"Selezione {var_check.get()}, {var_radio.get()}")


tk.Button(root, text="Mostra selezione", command=mostra).pack(pady=10)
root.mainloop()
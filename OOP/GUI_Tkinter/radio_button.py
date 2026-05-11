import tkinter as tk

root = tk.Tk()

# Checkbutton — variabile collegata BooleanVar
var_check = tk.BooleanVar()
check = tk.Checkbutton(root, text="Accetta termini", variable=var_check)
check.pack()

# Radiobutton — variabile collegata StringVar
var_radio = tk.StringVar(value="python")
tk.Radiobutton(root, text="Python", variable=var_radio, value="Python").pack()
tk.Radiobutton(root, text="Java",   variable=var_radio, value="Java").pack()
tk.Radiobutton(root, text="C++",    variable=var_radio, value="C++").pack()

def mostra():
    print(var_check.get(), var_radio.get())

tk.Button(root, text="Mostra selezione", command=mostra).pack(pady=10)
root.mainloop()
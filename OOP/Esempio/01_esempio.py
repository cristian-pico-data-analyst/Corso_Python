import tkinter as tk

class button_esempio:
    def saluta():
        print("Bottone cliccato!")

    root = tk.Tk()
    root.geometry("300x200")

    btn = tk.Button(
        root,
        text="Clicca qui!",
        command=saluta,          # funzione da chiamare al click
        bg="#2563eb",
        fg="white",
        font=("Arial", 12),
        padx=20,
        pady=8,
        relief="flat",           # stile bordo: flat, raised, sunken
        cursor="hand2"          # cursore al passaggio del mouse
    )
    btn.pack(pady=60)

    root.mainloop()

button_esempio()
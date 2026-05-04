# Creo una nuova lista
print(f"----------- LISTA SPESA -----------\n")
lista_spesa = ["Pane", "Latte", "Uova", "Formaggio"]
for spesa in lista_spesa:
    print(f"Articolo: {spesa}\n")

# Modifica un elemento della lista
print(f"----------- LISTA SPESA CON MODIFICA -----------\n")
lista_spesa[1] = "Yogurt"
for spesa in lista_spesa:
    print(f"Articolo: {spesa}\n")

# Aggiungere alla lista articoli
articoli = []
print(f"----------- AGGIUNGERE ARTICOLI CON CICLO FOR -----------\n")
for i in range(5):
    if i == 0:
        articoli.append(input(("Inserisci il primo articolo: ")))
    else:
        articoli.append(input("Inserisci un altro articolo: "))
print(f"{articoli}\n")

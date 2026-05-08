class ContoBancario:
    def __init__(self, saldo):
        self._saldo = saldo

    def deposito(self, importo):
        self._importo = importo
        if importo > 0: 
            self._saldo += importo
            print(f"Hai depositato {importo} €")
        else:
            print(f"Importo non valido")
    
    def preleva(self, importo):
        if importo < 0:
            print(f"Importo non valido")
        elif importo > self._saldo:
            print(f"Saldo insufficiente")
        else:
            self._saldo -= importo
            print(f"Saldo prelevato {self._saldo} €")

    def mostra_saldo(self):
        print(f"Saldo disponibile: {self._saldo} €")

# --- programma principale ---
print("\n=== CREA TUO CONTO BANCARIO ===")
saldo_iniziale = float(input("\nInserisci il saldo iniziale: ")) # Inserisco il saldo

conto = ContoBancario(saldo_iniziale)

# Lista delle opzioni disponibili
while True:
    print("\n\n---- MENU ----\n\n")
    print("1. Deposita")
    print("2. Preleva")
    print("3. Mostra Saldo")
    print("0. Esci")

    scelta = input("\nScegli un'opzione: ")

    if scelta == "1":
        importo = float(input("\nQuanto vuoi depositare? "))
        conto.deposito(importo)
    
    elif scelta == "2":
        importo = float(input("\nQuanto vuoi prelevare? "))
        conto.preleva(0)
    
    elif scelta == "3":
        conto.mostra_saldo()

    elif scelta == "0":
        print("\nSei uscito dal programma...")
        break

    else:
        print("\nScelta non valida")



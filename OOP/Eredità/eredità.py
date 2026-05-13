"""
    La funzione di ereditarietà permette di:
        - riutilizzare codice
        - specializzare una classe base
        - creare gerarchie
        -ridurre duplicazioni
        - creare componenti riutilizzabili (es. widget Tkinter personalizzati)
"""

class Veicolo:
    def __init__(self, marca, modello):
        self._marca = marca
        self._modello = modello

    # Informazioni
    def info(self):
        return f"{self._marca} {self._modello}"
    
    def Avvia(self):
        return "Il veicolo si avvia... vrooom..."
    
    def Ferma(self):
        return "Il veicolo si ferma!"


#----------------------------------------------------
# Ho creato una classe Veicolo con 2 parametri (marca, modello)
# Ho creato una classe Auto con 1 parametro (porte), ma che eredita i due parametri con di Veicolo con la funzione super

class Auto(Veicolo):
    def __init__(self, marca, modello, porte):
        super().__init__(marca, modello)
        self._porte = porte

    def Avvia(self):
        return f"L'auto {self.info()} si avvia..."
    
class Moto(Veicolo):
    def Avvia(self):
        return f"La moto {self.info()} si avvia..."
    

auto = Auto("Fiat", "500x", 5)
moto = Moto("Yamaha", "R1")

print(auto.info())
print(auto.Avvia())

print(moto.info())
print(moto.Avvia())
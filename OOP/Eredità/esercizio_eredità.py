# CLASSE Alimenti (Classe GENITORE)
class Alimenti:
    def __init__(self, id_prodotto, categoria):
        self._id_prodotto = id_prodotto
        self._categoria = categoria

    def info(self):
        return f"ID: {self._id_prodotto} - CATEGORIA: {self._categoria}"

    def Avvia(self):
        return "Questo prodotto proviene da ..."

# CLASSE DEI PRODOTTI (Classe Genitore: Alimenti -> Classe Figlio: Prodotto)
class Prodotto(Alimenti):
    def __init__(self, id_prodotto, categoria, nome_prodotto, provenienza):
        super().__init__(id_prodotto, categoria)
        self._nome_prodotto = nome_prodotto
        self._provenienza = provenienza
    
    def Aggiungere(self):
        return f"DENOMINAZIONE: {self._nome_prodotto} - PROVENIENZA: {self._provenienza}"

    def Avvia(self):
        return f"Questo prodotto ha le seguenti informazioni \n|{self.info()} {self.Aggiungere()}|\n"

# CLASSE DELLE CONSERVE (Classe Genitore: Prodotto -> Classe Figlio: Conserva)
class Conserva(Prodotto):
    def __init__(self, id_prodotto, categoria, nome_prodotto, provenienza):
        super().__init__(id_prodotto, categoria, nome_prodotto, provenienza)
        self._nome_prodotto = nome_prodotto
        self._provenienza = provenienza
    
    def Aggiungere(self):
        return f"DENOMINAZIONE: {self._nome_prodotto} - PROVENIENZA: {self._provenienza}"
    
    def Avvia(self):
        return f"Queste conserve etichettate \n|{self.info()} - {self.Aggiungere()}| sono ECCELLENTI\n"
    

# INSERISCO LE INFORMAZIONI E STAMPO
#prodotto = Prodotto("ID: 001 -", "CATEGORIA: Frutta -", "DENOMINAZIONE: Mela -", "PROVENIENZA: Trentino Alto-Adige")
#conserva = Conserva("ID: 005 -", "CATEGORIA: Verdura -", "DENOMINAZIONE: Melenzana -", "PROVENIENZA: Campania")
#print(prodotto.info()) # Mi da come risultato solo le informazioni "id_prodotto" e "categoria"
#print(prodotto.Avvia())
#print(conserva.info()) # Mi da come risultato solo le informazioni "id_prodotto" e "categoria"
#print(conserva.Avvia())

# ==============================================================================================

# OPPURE FACCIO INSERIRE TUTTO ALL' UTENTE

# ===================================
# BLOCCO PRINCIPALE: INSERIMENTO DATI
# ===================================

print("------------ NUOVO PRODOTTO -------------\n")
id_p = input("Inserisco l'ID del prodotto: ")
categoria_p = input("Inserisci la categoria: ")
nome_p = input("Inserisci le denominazioni del prodotto: ")
provenienza_p = input("Inserisci la provenienza del prodotto: ")

# Preparo l'oggetto usando le variabili appena inserite dall'utente
prodotto = Prodotto(id_p, categoria_p, nome_p, provenienza_p)

print("------------ NUOVA CONSERVA -------------\n")
id_c = input("Inserisco l'ID della conserva: ")
categoria_c = input("Inserisci la categoria: ")
nome_c = input("Inserisci le denominazioni della conserva: ")
provenienza_c = input("Inserisci la provenienza della conserva: ")

# Preparo l'oggetto usando le variabili appena inserite dall'utente
conserva = Conserva(id_c, categoria_c, nome_c, provenienza_c)

# ==========================================
# STAMPA DEI RISULTATI
# ==========================================
print("\n--- RISULTATO FINALE ---")
print(prodotto.Avvia())
print(conserva.Avvia())

"""
======================== ESEMPIO 1 ========================
    Exception: con "try" / except
    try:
        # codice che potrebbe dare errore
    except:
        # cosa fare se è presente un' errore

======================== ESEMPIO 2 ========================

    Exception: con "try" / except ValueError / except / else
    try:
        # codice che potrebbe dare errore
    except ValueError:
        # cosa fare se c'è un'errore
    except:
        # cosa fare se è presente un' errore
    else:
        # cosa fare se non c'è errore

======================== ESEMPIO 3 ========================

    Exception: con "try" / except FileNotFoundError / finally
    try:
        # codice che potrebbe dare errore
    except FileNotFoundError:
        # cosa fare se c'è un'errore
    finally:
        # cosa fare in ogni caso
   
"""
# =================== Esempio_1: ===================
print("===================== INIZIO PROGRAMMA ESEMPIO 1 =====================\n")

try:
    num1 = int(input("Inserisci il primo numero: "))
    print(f"Hai inserito il primo numero: {num1}")
except:
    print("ERRORE ! Devi inserire un numero.")

print("===================== FINE PROGRAMMA ESEMPIO 1 =====================\n")


# =================== Esempio_2: ===================
print("===================== INIZIO PROGRAMMA ESEMPIO 2 =====================\n")

try:
    num1 = int(input("Inserisci un numero: "))
except ValueError:
    print("ERRORE ! Devi inserire un numero.")
except:
    print("ERRORE ! Devi inserire un numero.")
else:
    print(f"Hai inserito il numero: {num1}")

print("===================== FINE PROGRAMMA ESEMPIO 2 =====================\n")


# =================== Esempio_3: ===================
print("===================== INIZIO PROGRAMMA ESEMPIO 3 =====================\n")

try:
    file = open("rubrica_contatti.xlsx", "r")
except FileNotFoundError:
    print("Il file NON ESISTE")
finally:
    print("Il File ESISTE \nOPERAZIONE TERMINATA")

print("===================== FINE PROGRAMMA ESEMPIO 3 =====================\n")

# =================== ESERCIZIO ===================
# Chiedi un' indice e mostra l'elemento nella lista
numero = [1, 2, 3, 4, 5, 6, 7]

try:
    chiedi = int(input("Inserisci un numero: "))
    elemento_trovato = numero[chiedi]
except ValueError, IndexError:
    print("ERRORE ! Il numero/indice non è presente\n")
else:
      print(f"Hai inserito l'indice: {chiedi}.\n" f"L'elemento corrispondente è: {elemento_trovato}")
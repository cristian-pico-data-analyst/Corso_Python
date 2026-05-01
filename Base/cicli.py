""" Il cicli in python (for / while)

    Un ciclo serve per ripetere un'azzione più volte
    Esempio: Salutare 5 volte
        print("Ciao")
        print("Ciao")
        print("Ciao")
        print("Ciao")
        print("Ciao") 😅😅😅😅😅
    
    Con il ciclio for si usa quante volte ripetere un azione o qualcosa 
    
    
    🔁 DIFFERENZA TRA FOR E WHILE
    | FOR              | WHILE          |
    | ---------------- | -------------- |
    | Sai quante volte | Non sai        |
    | Più sicuro       | Più flessibile |
    | Usa range()      | Usa condizioni |

"""

# Esempio 1:
# for i in range(5): # range(5) -> genera unmeri: 0,1,2,3,4
#     print(f"Riga {i}") # parte da 0 => arriva a 4 (NON include 5)

# Esemipo 2:
# select * from Studenti Where nome in ('mario', 'luca', 'simona', 'andrea', 'melania')
studenti = ['mario', 'luca', 'simona', 'andrea', 'melania'] 
voti = [23, 30, 18, 16, 20]

print("Lista degli studenti\n")
for studente in studenti: 
    print(f"Studente: {studente}\n")  
    
print("Lista studenti con voti\n")
"""
    len(studenti) -> numero elementi
    i             -> indice (0,1,2 ..)
    studenti[i]   -> nome dello studente
    voti[i]       -> il voto dello studente
    
    Attenzione ⚠️
        👉 Le due liste devono avere stessa lunghezza
"""
for i in range(len(studenti)):  
    print(f"Studente: {studenti[i]} - Voto: {voti[i]}")  
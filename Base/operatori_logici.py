"""
 Gli operatori Logici 
 Servono per conbinare condizione 
 Si usano:
    | Opertore | Significativo  |
    |----------|----------------|
    | and      | antrambi vere  |
    | or       | almeno una vera|
    | not      | nega           |
    ----------------------------
"""

# print(True and False)
# print(True or False)
# print(not False) 

a = 12
b = 30
# print(a == b and b != a)


# Melania

num1 = int(input(" inserisci un numero: "))  
num2 = int(input(" inserisci secondo numero: "))  

risultato = (num1 != num2 and num1 >= num2) and (num1 * num2 != 0)
print(num1 * num2 != 0)
print(num1 != num2 and num1 >= num2)
print(risultato)
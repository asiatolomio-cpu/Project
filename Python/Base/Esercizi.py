#Esercizio TIPI di DATI

nome = 'Luca' # stringa(testo)
eta = 34 # intero(numero)
altezza = 1.75 # float(decimale)
studente = True #boolean (booleano)

"""
print(type(nome)) <class 'str'> = stringa
print(type(eta)) <class 'int'> = intero
print(type(altezza)) <class 'float'> = decimale
print(type(studente)) <class 'bool'> = condizione (V/F)
"""

#Esercizio LISTE

# Creazione di una lista di prezzi
"""
lista_prezzi = [5, 25, 10, 40, 34, 66, 100, 53, 52, 88, 99, 102, 77, 365, 1030, 2, 44, 12, 62, 35, 74, 21, 11]
print(lista_prezzi)


#Lunghezza della lista
print(f"La lista contiene {len(lista_prezzi)} elementi.")


lista_prezzi[11] = 2654
print(lista_prezzi)

print("===========================================\n\n")

articoli = []
# Aggiungi alla lista articoli

for i in range(5):
    if i == 0:
        articoli.append(input("Inserisci il primo articolo: "))
    else:
        articoli.append(input("Inserisci un altro articolo: "))

# stampa la lista articoli
print("Lista degli articoli\n")
for articolo in articoli:
    print(f"Articolo: {articolo}")
"""

#Esercizio IF/ELIF/ELSE

# Esercizio 1: Pari/ Dispari con (if else)
# 1 Chiedere all'utente di inserire un numer
# 2 Fare una verifica se il numero inserito è pari o dispari
"""
Numero = int(input('Inserisci un numero: '))

if Numero %2 == 0:
    print("Il numero inserito è pari")
else:
    print("Il numero inserito è dispari")
"""
    
""" 
    Esercizio 2: Verificare se l'utente è maggiorenne o minorenne
"""

"""
eta = int(input("Quanti anni hai? "))

if eta > 18:
    print("Sei maggiorenne")
elif eta == 18:
    print("Sei maggiorenne")
else:
    print("Sei minorenne")
"""    



# per far inserire dati all'utente
# input() restituisce SEMPRE testo inserito dall'utente dalla console


nome = input('Come ti chiami? ') # 1.
print('Ciao! Piacere ', nome) # 3.
# fra parentesi inserisco il testo che viene stampato prima dell'inserimento
# 1.la console mi restituirà quella stringa e 
# 2. mi permetterà l'inserimento
# 3. successivamente ciò che sarà inserito potrà essere richiamato tramite il nome variabile 
"""
    1. Come ti chiami? 
    2. Asia 
    3. Ciao! Piacere  Asia
"""

# print(f'{nome} Come stai?')
# altro tipo di formattazione

eta = int(input('Quanti anni hai? '))
# specifico il tipo della variabile inserendo int e aprendo parentesi
# poi inserisco input e tra parentesi la stringa

print('L\'anno prossimo ne avrò ',(eta+1))
# altro tipo di concatenazione 
# la stringa va fra apici 
# metto la virgola 
# inserisco la variabile
# posso modificare la variabile mettendola fra parentesi e inserendo gli operatori matematici


""" eta = int(input("Quanti anni hai? "))
    print(f"Ho {eta} anni. L\'anno prossimo avrò {eta + 1} anni")
oppure
    eta = int(input('Quanti anni hai?'))
    print(f'Ho {eta} anni, L\'anno scorso avevo {eta - 1} anni')
"""
# altro tipo di formattazione


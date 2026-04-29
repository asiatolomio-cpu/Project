"""
print(num1 + num2) #somma
print(num1 - num2) #differenza
# stessa cosa con * e /
"""
# print("==============\n") è il separatore che mi lascia libera una riga


num1 = int(input('Scegli il primo numero '))
num2 = int(input('Scegli il secondo numero '))

somma = num1 + num2 # a. variabile
moltiplicazione = num1 * num2 # b. variabile
sottrazione = num1 - num2 # c. variabile
divisione = num1 / num2 # d. variabile
potenza = num1 ^ num2 # e. variabile 


print(f'La somma dei 2 numeri è {num1 + num2}')

print(f'La somma di {num1} + {num2} è {somma}') # somma a. variabile 
# prima di inserire fra parentesi graffe la somma, dobbiamo definire la variabile 
# la nominiamo con un termine specifico, in modo da richiamarla nel print

print(f'Il prodotto di {num1} e {num2} è {moltiplicazione}') # moltiplicazione b. variabile
# devo ricordarmi di creare la variabile prima di inserirla 

print(f'La differenza fra {num1} e {num2} è {sottrazione}') # sottrazione c. variabile

print(f'Il quoziente di {num1} diviso {num2} è {divisione}') # divisione d. variabile 

print(f'La potenza di {num1} con esponente {num2} è {potenza}') # potenza e. variabile

"""
    ALTRIMENTI POSSO MANTENERE UNA SOLA VARIABILE
    DEVO CAMBIARLA PERò PER OGNI OPERAZIONE
    lo ritrovo sul file operatori_matematici.py
"""

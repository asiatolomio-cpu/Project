# Asia
try:
    num1=float(input("Inserisci un numero:"))
except ValueError:
    print("Errore! Devi inserire un numero!")
else:
    print("Hai inserito: ", num1)

#Cristian 
# Chiedi un' indice e mostra l'elemento nella lista
numero = [1, 2, 3, 4, 5, 6, 7]

try:
    chiedi = int(input("Inserisci un numero: "))
    elemento_trovato = numero[chiedi]
except ValueError:
    print("ERRORE ! Il numero non è valido\n")
except IndexError:
    print("ERRORE ! Il numero non è indicizzato\n")
else:
      print(f"Hai inserito l' indice: {chiedi}.\n L'elemento corrispondente è: {elemento_trovato}")


# Ana
# Apri un file.csv, se non esiste, mostra un messaggio di errore
import os



try:
    nome_arquivo = open("prodotto.csv","r")
except:
    print("Attenzione: questo file non esiste")
else:
    print("Il file è stato aperto")


# Brenda
# Chiedi 2 numeri e somma. Usa else nella try 
while True:
    try:
        num1 = float(input("Inserisci il primo numero: "))
        num2 = float(input("Inserisci il secondo numero: "))
    
    except ValueError:
        print("Errore! Riprova con dei numeri.")
    
    else:
        
        somma = num1 + num2
        print(f"La somma è: {somma}")
        break


# Giuseppe
# chiedi 3 numeri e calcola la media
while True:
    try:
        num1 = int(input("Inserisci il primo numero"))
        num2 = int(input("Inserisci il secondo numero"))
        num3 = int(input("Inserisci il terzo numero"))
        media = (num1 + num2 + num3)/3
    except ValueError:
        print("Errore! Devi inserire un numero!")
    else:
        print("La media è: ", media)
        break



# Filippo
while True:
    try:
        num1 = float(input("Inserisci un numero: "))






# Mattia
# Mostra un messaggio finale indipendentemente dall'errore
def sessione_umoristica():
    try:
        risposta = input("Vuoi sentire una barzelletta? Si o si?? ").strip().lower()
        
        if risposta == "si":
            print("Cosa fa una mucca sul divano? 🐮 Si STRAVACCA! 😂")
        
        elif risposta == "certo":
            print("Cosa fa una mucca sul divano? 🐮 Si STRAVACCA! 😂")

        elif risposta == "no":
            raise ValueError("L'utente ha rifiutato la barzelletta")
        
        elif risposta.isdigit():
            raise TypeError("L'utente ha inserito dei numeri invece di una risposta testuale")
        
        else:
            print("Eppure era una domanda semplice... 😅")
    
    except ValueError:
        print("Non sai cosa ti perdi... 😒")
    
    except TypeError:
        print("Scusa, non parlo il numerese... 😅")
    
    finally:
        print("Grazie per aver partecipato alla sessione di barzellette! 😄")

sessione_umoristica()

DA FINIREEEEEEEEEEEEEEEEEE
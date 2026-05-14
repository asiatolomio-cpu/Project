# con TRY e EXCEPT andiamo a trattare le EXCEPTIONS 
# struttura base:
#try:
    #codice che potrebbe generare errore
#except:
    # cosa fare in caso di errore


# TRY e EXCEPT
# esempio 1: #try:
                #codice che potrebbe generare errore
             #except:
                # cosa fare in caso di errore
try:
    num1= int(input("Inserisci un numero: "))
    print("Hai inserito: ", num1)
except:
    print("Errore! Devi inserire un numero intero.")
# evita che il programma si blocchi
# inseriamo un msg personalizzato, poi si ferma, ma non si blocca


print("= = = = = = = = FINE PROGRAMMA 1 = = = = = = = = \n")


# TRY, EXCEPT e ELSE
# esempio 2: #try:
                #codice che potrebbe generare errore
             #except:
                # cosa fare in caso di errore
             #else:
                # cosa fare se non c'è un errore
try:
    num1=int(input("Inserisci un numero:"))
except ValueError:
    print("Errore! Devi inserire un numero intero!")
else:
    print("Hai inserito: ", num1)


print("= = = = = = = = FINE PROGRAMMA 2 = = = = = = = = \n")


# TRY, EXCEPT e FINALLY
# esempio 3: #try:
                #codice che potrebbe generare errore
             #except:
                # cosa fare in caso di errore
             #finally:
                # cosa fare in ogni caso
try:
    file = open("Rubrica_Contatti.txt", "r")
    print("Hai inserito: ")
except FileNotFoundError:
    print("Errore! Il file non esiste!")
finally:
    print("Operazione terminata")

print("= = = = = = = = FINE PROGRAMMA 3 = = = = = = = = \n")

# Esercitiamoci con le operazioni, i dati e le funzioni errore


"""
    IF /ELIF / ELSE (Se / Altrimenti Sé / Altrimenti ) 

    Concetto:
    Le strutture if / else servono per far prendere decisione al programma
    
    Il computer valuta una condizione :
        - se è vera  👉 esegue un blocco di istruzioni
        - se è falsa 👉 esegue un altro blocco di istruzioni
    
    if (Se): è il punto di partenza.
            Il computer controlla se una condizione è vera.
            Se lo è, esegue il codice subito sotto
    
    elif (Altrimenti se): Si usa quando la prima condizione (if) è falsa,
        ma vuoi controllare un'altra prima di arrenderti.
        Puoi usarlo quante volte vuoi. 
        Vanno usati in sequenza quando voglio verificare più opzioni una dietro l'altra
        ex. l'elemento X è uguale ad A? ---> NO.
            ok, allora è uguale a B? ---> NO.
            ok, allora a C? ---> NO.
            e così via...
        Viene eseguito tutti in rapida sequenza

    
    else (Altrimenti): è l'ultima spiaggia.
        Viene eseguito solo se tutte le condizioni
        precedenti sono risultate false.  
    
    if condizione: 
        codice se vero
    elif condizione:
        codice se vero
    else:
        codice se falso
        
        Spiegazione: 
            == → confronto (fra 2 valori)
            and → entrambe vere (fra 2 condizioni)
"""
"""
print("Benvenuto nel programma")

numero1 = int(input("Inserisci un valore diverso da zero: "))
risposta = "hai inserito un valore diverso da 0"

if numero1 > 0:
    print(f"Brav* {risposta}")
else:
    print(f"Scelta sbagliata")

"""
"""
# La stessa logica è applicata al Login di un account/programma
# Ricordiamoci che in questo caso abbiamo inserito come tipologia di input int
# Quindi la pwd potrà essere solo un numero 
# Abbiamo fissato le 2 variabili nome e psw per dare le 2 condizioni
nome = "Asia"
pwd  = 1234


username = input("Inserisci tuo nome: ")
password = int(input("Inserisci la password: "))

if username == nome and password == pwd:
    # (Se) 
    # Lo username corrisponde AND la password pure?
    # Ok stampo a schermo:
    print("Benvenuto nel programma")


elif username != nome:
    # (Altrimenti Se) 
    # Lo username è diverso da quello corretto (lo abbiamo impostato come variabile all'inizio)?
    # Allora stamperò a schermo:
    print("Nome non trovato nel sistema")
elif username == nome and password != pwd:
     # (Altrimenti Se) 
     # Lo username è corretto a la password è diversa da quella corretta?
     # Allora stamperò a schermo:
    print("Password errata")
else:
    # Per tutte le altre opzioni (errate)
    # Stamperà a schermo:
    print("Accesso negato!")

"""

"""
# Esempio assegnare un voto ad uno studente
voto = int(input("Inserisci un voto da assegnare! "))

if voto >= 90:
    print("Ottimo, hai preso A!")
elif voto >= 80:
    print(f"{voto} Buono")
elif voto >= 70:
    print(f"{voto} Discreto")
elif voto >= 60:
    print(f"{voto} Sufficiente")
else:
    print("puoi fare meglio la prossima volta")
"""

"""
    L'annidamento(in inglese nesting) 
    si verifica quando inserisci un'istruzione (if)
    dentro un'altra istruzione if
    
    if condizione:
        codice
        
        if condizione:
            codice
        else:
    else:
        stampa
    

"""

# Numero Positivo e pari
numero = int(input("Inserisci un numero "))

if numero > 0:
    print("Il numero è positivo")
    
    # Questo if è ANNIDATO dentro il primo
    if numero % 2 == 0:
        # condizione '%2' vuol dire è divisibile per 2
        print("Ed è anche un numero pari")
    else:
        print("Ma è un numero dispari")
elif numero < 0:

    print("il numero è negativo")
    if numero % 2 == 0:
        print("Ed è anche pari")
    else:
        print("Ma è un numero dispari")
else:
    print("Il numero che hai inserito non è ne positivo ne negativo, ne tantomeno pari o dispari")

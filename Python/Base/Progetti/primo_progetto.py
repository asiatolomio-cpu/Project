""" 
studenti = {} # dichiaro una lista vuota nominata 'studenti'

while True: # imposto un ciclo facendo stampare a schermo le opzioni valide
    print("\n\n----- Registro Studenti-----\n\n")
    print("1. Aggiungi studente")
    print("2. Mostra registro")
    print("3. Calcola Media dei voti")
    print("4. Promossi / Bocciati")
    print("5. Esci\n")

    scelta = input("Scegli un'opzione: ") 
    # stampo a schermo la prima variabile che avrà come valore l'immissione da parte dell'utente

    if scelta == "1":
    # se sceglie 1 allora introduco la chiave della lista come 'nome'
    # come valore della chiave c'è invece l'immissione dell'utente
        nome = input("Inserisci il nome dello studente: ")

        voti = []
        # dichiaro una nuova lista vuota chiamata 'voti'
    elif scelta == "5":
    # se invece 
        print("Uscita dal programma")
        break
    else:
        print("Opzione non valida")
"""
"""
studenti = {}

while True:
    print("\n\n----- Registro Studenti-----\n\n")
    print("1. Aggiungi studente")
    print("2. Mostra registro")
    print("3. Calcola Media dei voti")
    print("4. Promossi / Bocciati")
    print("5. Esci\n")

    scelta = input("Scegli un'opzione: ")

    if scelta == "1":
        nome = input("Inserisci il nome dello studente: ")

        voti = []

        for i in range(3):
            voto =int(input(f"Inserisci il voto {i+1} (0-10): "))
            voti.append(voto)

        studenti[nome] = voti
   
    elif scelta == "5":
        print("Uscita dal programma")
        break
    else:
        print("Opzione non valida")
"""
"""
studenti = {}

while True:
    print("\n\n----- Registro Studenti-----\n\n")
    print("1. Aggiungi studente")
    print("2. Mostra registro")
    print("3. Calcola Media dei voti")
    print("4. Promossi / Bocciati")
    print("5. Esci\n")

    scelta = input("Scegli un'opzione: ")

    if scelta == "1":
        nome = input("Inserisci il nome dello studente: ")

        voti = []

        for i in range(3):
            voto =int(input(f"Inserisci il voto {i+1} (0-10): "))
            voti.append(voto)

        studenti[nome] = voti
    
    elif scelta == "2":
        print("\n ----- Registro Studenti -----\n")

        for nome, voti in studenti.items():
            print(f"Studente: {nome} - Voti: {voti}")
            print("\n - - - - - - - - - - - \n")
   
    elif scelta == "5":
        print("Uscita dal programma")
        break
    else:
        print("Opzione non valida")
"""
"""
studenti = {}

while True:
    print("\n\n----- Registro Studenti-----\n\n")
    print("1. Aggiungi studente")
    print("2. Mostra registro")
    print("3. Calcola Media dei voti")
    print("4. Promossi / Bocciati")
    print("5. Esci\n")

    scelta = input("Scegli un'opzione: ")

    if scelta == "1":
        nome = input("Inserisci il nome dello studente: ")

        voti = []

        for i in range(3):
            voto =int(input(f"Inserisci il voto {i+1} (0-10): "))
            voti.append(voto)

        studenti[nome] = voti
    
    elif scelta == "2":
        print("\n ----- Registro Studenti -----\n")

        for nome, voti in studenti.items():
            print(f"Studente: {nome} - Voti: {voti}")

    elif scelta == "3":
        for nome, voti in studenti.items():
            media = sum(voti) / len(voti)
            print(f"Studente: {nome} - Media voti: {media:.2f}")
   
    elif scelta == "5":
        print("Uscita dal programma")
        break
    else:
        print("Opzione non valida")
"""

studenti = {}

while True:
    print("\n\n----- Registro Studenti-----\n\n")
    print("1. Aggiungi studente")
    print("2. Mostra registro")
    print("3. Calcola Media dei voti")
    print("4. Promossi / Bocciati")
    print("5. Esci\n")

    scelta = input("Scegli un'opzione: ")

    if scelta == "1":
        nome = input("Inserisci il nome dello studente: ")

        voti = []

        for i in range(3):
            voto =int(input(f"Inserisci il voto {i+1} (0-10): "))
            if 1<= voto <=10:
                voti.append(voto)
            else:
                print("Voto non valido. Inserisci un voto da 1 a 10")
                continue
                   
                

        studenti[nome] = voti
    
    elif scelta == "2":
        print("\n ----- Registro Studenti -----\n")

        for nome, voti in studenti.items():
            print(f"Studente: {nome.upper()} - Voti: {voti}")

    elif scelta == "3":
        for nome, voti in studenti.items():
            media = sum(voti) / len(voti)
            print(f"Studente: {nome.upper()} - Media voti: {media:.2f}")
        
    elif scelta == "4":
         for nome, voti in studenti.items():
            if media > 6:
                print(f"Studente: {nome.upper()} - Media voti: {media:.2f} - Studente PROMOSSO")
            else:
                print(f"Studente: {nome.upper()} - Media voti: {media:.2f} - studente BOCCIATO")
   
    elif scelta == "5":
        print("Uscita dal programma")
        break
    else:
        print("Opzione non valida")



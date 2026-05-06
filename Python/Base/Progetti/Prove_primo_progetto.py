"""
studenti = {
    "Mario" : 7,9,4
    "Luca" : 3,9,10
    "Simona" : 2,8,7
    "Andrea" : 5,7,9
    "Melania" : 2,3,9
    "Catalina" : 6,8,6
    "Giovanni" : 3,4,9
    "Giuseppe" : 4,7,8
    "Mattia": 9,5,7
    "Francesca" : 4,8,6
}
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
   
    elif scelta == "5":
        print("Uscita dal programma")
        break
    else:
        print("Opzione non valida")
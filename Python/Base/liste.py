# la lista in python si dichiara con le parentesi quadre []
# una lista può contenere qualsiasi tipo di dato (stringa, numero, booleano, ecc..)
# una lista può essere vuota o contenere elementi

# Esempio 1: lista di stringhe
# studenti = []

# Esempio 2: lista di numeri e stringhe
studenti = ['mario', 'luca', 'simona', 'andrea', 'melania']
voti = [18, 19, 22, 16, 20]


# stampa della lista classica
print(studenti)
print(voti)

# stampa della lista con ciclo for
for studente in studenti:
    print(f"Studente: {studente}")


for voto in voti:
    print(f"Voto: {voto}")
    
    
for i in range(len(studenti)): #
    print(f"Studente: {studenti[i]} - Voto: {voti[i]}")



# Aggiungere un elemento alla lista
#studenti.append(input("Inserisci il nome dello studente: "))
#voti.append(int(input("Inserisci il voto dello studente: ")))


# Esempio 3: Zip() -> unisce due liste in una sola lista di tuple
for studente, voti in zip(studenti, voti): 
    print(f"Studente: {studente.upper()} - Voto: {voti}")

# Esempio 4: Stampare in maiuscolo la lista degli studenti
"""
print("Lista studenti in maiuscolo\n")
for studente in studenti:
    print("===============Maiuscolo=====================")
    print(f"Studente: {studente.upper()}\n")
    
    print("==============Minuscolo=====================")
    print(f"Studente: {studente.lower()}\n")
    
"""
      
#               0         1        2         3
lista_spesa = ["pane", "latte", "uova", "formaggio"]
for spesa in lista_spesa:
    print(f"Articolo: {spesa}")
print("============================================\n")
    
    
# Esempio 5: Modificare un elemento della lista
lista_spesa[1] = " yogurt "
# indico in quale posizione voglio fare la sostiuzione fra parentesi [] e il valore fra ""
for spesa in lista_spesa:
    print(f"Articolo: {spesa}")
    
    
    
    

    
# listaStudenti = ("mario", "luca", "simona", "andrea", "melania") # tupla (non modificabile)nu
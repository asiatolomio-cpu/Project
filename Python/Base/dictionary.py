# I dictionary (dizionario) è una struttura che salva dati in coppie chiave-valore.

# Creazione di un dizionario
persona = {
    "nome": "Luca", # chiave: nome, valore: Luca
    "cognome": "Salvato", # chiave: cognome, valore: Salvato
    "età": 30, # chiave: età, valore: 30
    "città": "Roma", # chiave: città, valore: Roma
    "codice_fiscale": "LCCLCA80A01H501U", # chiave: codice_fiscale, valore: LCCLCA80A01H501U
    "professione": "Ingegnere" # chiave: professione, valore: Ingegnere
}

# Accedere ai valori del dizionario
# Chiedo che mi venga restituita la chiave 'nome' del dizionario chiamato 'persona'
# Output: Luca poiche io ho richiesto il valore della chiave e non la sua dicitura
print(persona["nome"])    

# Più sicuro è usare il metodo 'get()' che restituisce None se la chiave non esiste 
# se non uso 'get()' invece si può generare un errore
# Output: LCCLCA80A01H501U
print(persona.get("codice_fiscale")) 

# Voglio modificare un valore esistente
# specifico prima il dizionario, poi la chiave e inserisco il nuovo valore usando il simbolo "="
persona["cognome"] = "Rossi"
print(persona["cognome"]) 
# Output: Rossi e non più Salvato

# Voglio aggiungere una nuova coppia chiave-valore
# specifico prima il dizionario, poi la nuova chiave e come per la modifica inserisco il nuovo valore
persona["professione"] = "Ingegnere"

print("\n================================================\n")

# Ciclo for per stampare tutte le chiavi 
print("Chiavi del dizionario:")
# generalmente le chiavi vengono definite dalla variabile 'key'
for key in persona:
    print(f"Chiave: {key}")
    
# Ciclo for per stampare tutti i valori
print("\nValori del dizionario:")
# generalmente i valori vengono definiti dalla variabile 'value'
# mentre poi devo specificare il dizionario seguito dal punto e dalla lista 'values' selezionando tutto con '()'
for value in persona.values():
    print(f"Valore: {value}")
    
# Ciclo for per stampare tutte le coppie chiave-valore
print("\nCoppie chiave-valore del dizionario:")
for key, value in persona.items():
    # uso items per la corrispondenza (poichè sono coppie)
    print(f"Chiave: {key} - Valore: {value}")

# Esempio reale (Registro studenti)
studenti = {
    "Mario" : 36,
    "Luca" : 30,
    "Simona" : 28,
    "Andrea" : 25,
    "Melania" : 29,
    "Catalina" : 27,
    "Giovanni" : 31,
    "Giuseppe" : 26,
    "Mattia": 32,
    "Francesca" : 24
}

# :.2f (è usato per formattare i numeri in virgola mobile)
media = 23.456789
print(f"La media è: {media:.2f}") 
# il 2 indica il numero di cifre decimali che voglio tenere 

# Calcolare la media dei voti degli studenti
media = sum(studenti.values()) / len(studenti)

# Calcolare il voto massimo e minimo
massimo_voto = max(studenti.values())
minimo_voto = min(studenti.values())


print(f"La media dei voti è: {media}")
print(f"Il valore massimo è {massimo_voto}")
print(f"Il valore minimo è {minimo_voto}")

print("\n================================================\n")
# Lista degli studenti (sopra/sotto) la media
print("Studenti sopra la media:")

for nome, voto in studenti.items():
    if voto >= media:
        print(f"{nome} ha voti sopra la media")
    else:
        print(f"{nome} ha voti sotto la media")

print(f"Ecco gli studenti e i loro voti")

for nome, voto in studenti.items():
    print(f"Nome : {nome} - Voto: {voto}")
    #uso di nuovo 'items' per scrivere le coppie di key and values
    
    
# Esempio 2: Dizionario con lista di voti
studenti_voti = {}

studenti["luana"] = [28, 30, 27]
studenti["Brenda"]= [27, 28, 30, 27, 28]
studenti["melania"]= [25, 29, 30, 24, 27, 30, 24]
# per ogni studente sono andata a specificare più voti 
# ho abbinato la values a più voti, come se fossero uno solo 
# ho aggiunto più studenti alla stessa lista

for studente, voto in studenti.items():
    print(f"Studente : {studente.upper()} ha un voto di: {voto}")
    # scrivendo la variabile e successivamente '.upper' ho stampato a schermo il nome dello studente tutto in maiuscolo


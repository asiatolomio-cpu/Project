
class Persona: 
    # metodo 'override', con parametri  
    # 'def' significa funzione o metodo  
    def __init__(self, nome, cognome, email, telefono): 
        self.nome = nome 
        self.cognome = cognome
        self.email = email
        self.telefono = telefono 
        # sono variabili appartenenti all'oggetto
        # self significa 'questo' e serve per identificare l'oggetto a cui appartiene la variabile
    
    def __str__(self):
        return f"{self.nome}, {self.cognome}, {self.email}, {self.telefono}"
    # inserisco questa stringa per rendere leggibile il risultato di ritorno di ciò che ho chiesto di fare al programma
    # __str__ è un metodo speciale di python
    # return da l'input di 'restituisci questo  testo' (in questo caso testo)
    
studente = Persona("Alessio", "Pippo", "p.alessio@email.com", "3478576968")
# è un modo per inserire i dati di uno studente, in questo caso
# creo un tuple con all'interno delle parentesi tonde i dati
# ho fatto combaciare poi la variabile 'studente' con i parametri di 'Persona'
print(studente)




# NON FUNZIONA. PERCHè????


"""
class Studenti:
    def __init__(self, nome, cognome, email,telefono):
       
        self._nome   = nome
        self._cognome= cognome
        self._email = email
        self._telefono = telefono

    def __inserisci__(self):
        self._nome = "Moussa"
        self._cognomecognome = "Salisou"
        self._email = "ms@email.com"
        self._telefono = "345678900998"

        print(f"{self._nome} {self._cognome} {self._email} {self._telefono}")  
"""

"""
class App_Studenti:
    def __init__(self):
        studente = Studenti ()
        studente.inserisci_dati()
        print(f"Registro Studenti: {studente} ")

App_Studenti()
"""
"""
class Stampa:
    def __init__(self):
        nome = input("Inserisci il tuo nome: ")
        cognome = input ("Inserisci il tuo cognome: ")
        email = input("Inserisci la tua email: ")
        telefono = input("Inserisci il tuo numero di telefono: ")

        # definisco il modo in cui voglio che venga reso, ossia 'studente'
        # appartenente alla classe Studenti
        # che specifica gli attributi
        studente = Studenti(nome, cognome, email, telefono)

        # vado a stampare la dicitura 'Registro Studenti'
        # poi mi restituirà poi ciò che ho scritto fra parentesi graffe
        # {qui dentro metto la variabile definita precedentemente}
        print(f"Registro Studenti: {studente} ")

Stampa()"""

"""class Persona:

    # costruttore vuoto
    def __init__(self): # public Persona (){} ossia (accessibile ovunque) 
       pass

studente = Persona()
# viste che non ho specificato i parametri posso lasciare le parentesi vuote
# se li avessi impostati (come successivamente) allora mi darebbe msg di errore
"""

class Persona: 
    # metodo 'override', con parametri    
    def __init__(self, nome, cognome, email, telefono): # 'def' significa funzione o metodo
        self.nome = nome 
        self.cognome = cognome
        self.email = email
        self.telefono = telefono
    
studente = Persona ('Alessio', 'Pippo', 'p.alessio@email.com', '3478576968')

print(studente)

class Studenti:
    def __init__(self, nome, cognome, email,telefono):
        # attributi o proprietà del costruttore della classe
        self._nome   = nome
        self._cognome= cognome
        self._email = email
        self._telefono = telefono

    def __str__(self):
        return f"{self._nome} {self._cognome} {self._email} {self._telefono}"   
    


    """def __add__(self):
        self._nome = "Moussa"
        self._cognome = "Salisou"
        self._email = "ms@email.com"
        self._telefono = "345678900998".    che cazzo ho fatto???????"""



class App_Studenti:
    def __init__(self):
        studente = Studenti ()
        studente.inserisci_dati()
        print(f"Registro Studenti: {studente} ")

App_Studenti()


"""class Stampa:
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
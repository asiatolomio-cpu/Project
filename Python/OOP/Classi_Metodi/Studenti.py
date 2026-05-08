class Studenti:
    def __init__(self, nome="", cognome="", email="",telefono=""):
        # attributi o proprietà del costruttore della classe
        self._nome   = nome
        self._cognome= cognome
        self._email = email
        self._telefono = telefono

    def __init__(self):
        self._nome = input("Inserisci il tuo nome: ")
        self._cognome = input ("Inserisci il tuo cognome: ")
        self._email = input("Inserisci la tua email: ")
        self._telefono = input("Inserisci il tuo numero di telefono: ")    

    def __str__(self):
        return f"{self._nome} {self._cognome} {self._email} {self._telefono}"   
    
    def Saluta(self):
        print("Ciao!")

    def __

class App_Studenti:
    def __init__(self):
        studente = Studenti ()
        studente.inserisci_dati()
        print(studente)

App_Studenti()
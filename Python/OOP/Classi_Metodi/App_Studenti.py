class Studenti:
    def __init__(self):
        # attributi o proprietà del costruttore della classe
        self._nome = ""
        self._cognome = ""
        self._email = ""
        self._telefono = ""
        # inserisco la classe Studenti senza attributi tra parentesi
        # vado a definire gli attributi (come 'nome', 'cognome' ecc.) ma lascio dopo l'uguale la stringa vuota ("")
        # uso questa maniera perchè poi definisco un metodo di inserimento dati tramite input
         
    def inserisci_dati(self):
        self._nome = input("Inserisci il nome: ")
        self._cognome = input("Inserisci il cognome: ")
        self._email = input("Inserisci email: ")
        self._telefono = input("Inserisci telefono: ")

    def __str__(self):
        return f"{self._nome} {self._cognome} {self._email} {self._telefono}"
    # definisco che voglio avere i dati di ritorno in forma leggibile

class App_Studenti:
    def __init__(self):
        # inizializzo la classe App_Studenti con attributi vuoti
        studente = Studenti ()
        # imposto la variabile 'studente' come appartenente alla classe 'Studenti' definita in precedenza
        # creo perciò un oggetto 'studente' della classe 'Studenti'
        studente.inserisci_dati()
        # faccio in modo che l'inserimento tramite input sia abbinato alla variabile 'studente'
        # quindi 'punto' su 'studente' e gli faccio fare il metodo 'inserisci_dati' definito in precedenza

        print(studente)
        # infine stampo lo studente appena inserito

App_Studenti()
# ho creato un oggetto della classe App_Studenti()
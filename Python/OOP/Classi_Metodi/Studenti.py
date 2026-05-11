class Studenti:
    def __init__(self):
        self._nome = input("Inserisci il tuo nome: ")
        self._cognome = input ("Inserisci il tuo cognome: ")
        self._email = input("Inserisci la tua email: ")
        self._telefono = input("Inserisci il tuo numero di telefono: ")  

    def __str__(self):
        return f"{self._nome} {self._cognome} {self._email} {self._telefono}" 
    
    def mostra_dati(self):
        print(f"{self._nome}, {self._cognome}, {self._email}, {self._telefono}")
        #oppure:
""" def mostra_dati(self):
        print(f"{self._nome},{self._cognome},{self._email}")
        print("Nome: ", self._nome)
        print("Cognome: ", self._cognome)
        print("Email: ", self._email)
        print("Telefono: ", self._telefono)
    il doppio underscore identifica un metodo python innato del codice, se lo andassi ad inserire "a caso" confonderebbe il programma 
"""
studente1 = Studenti()

"""
nota bene:
1 - non ho inserito i parametri nell'__init__ ma solo self
2 - li ho specificati successivamente
3 - in input ho inserito un solo attributo, ciò che voglio sia stampato a schermo
4 - ho inserito una variabile (studente1), altrimenti a chi attribuisco i parametri che saranno inseriti tramite input?
5 - ho indicato che la varibile 'studente1' appartiene a 'Studenti' come classe, senza specificare alcun attributo ma segnando le parentesi
"""
print(studente1)
studente1.mostra_dati
    



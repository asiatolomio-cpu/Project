class Persona:
    def __init__(self, nome, cognome):
        self._nome = nome
        self._cognome = cognome

    def saluta(self):
        print("Ciao sono " + self._nome)


class Insegnante(Persona):
    def __init__(self, nome, cognome, materia):
        super().__init__(nome, cognome)
        self._materia = materia
    
    def saluta(self):
        print("Buongiorno studenti, sono l'insegnante " + self._nome +" "+ self._cognome + " insegno " + self._materia)

    def vota(self):
        print("Bravo, hai preso un bel voto")


persona1 = Persona("Luca", "Giurato")
persona2 = Insegnante("Alessandra", "Semenzato", "Italiano")

print(persona1.saluta())
print(persona2.saluta())


        

    
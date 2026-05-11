# self => rapresenta l'oggetto stesso
# serve per accedere ai dati dell'oggetto
# va sempre inserito, altrimenti il programma non 'punterebbe' a nulla
class Persona:
    # Construttore della classe con parametri
    def __init__(self, nome, eta): 
        self.nome = nome 
        self.eta = eta   
    
    # Funzione o Metodo
    def saluta(self):    
        print(f"Ciao, mi chiamo {self.nome}, ho {self.eta} anni")
# Metodo:
# ho definito cosa fa, 'saluta'
# ho definito come, inserendo il 'print'
# ho definito quali parametri coinvolge, inserendo i parametri fra {}

p1 = Persona("Carlo", 35)
p2 = Persona("Vanessa", 32)
# p1 p2 in questo caso sono delle variabili (posso chiamarl e come voglio)
# inserisco fra parentesi gli argomenti richiesti dalla classe

p1.saluta()
p2.saluta()
# ho inserito prima la variabile con il punto
# poi ho deciso cosa 'fargli fare' tramite il metodo
# avendo definito il metodo in precedenza non devo inserire null'altro
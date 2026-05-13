# EREDITA' permette:
# riutilizzare codice
# specializzare classi base
# creare gerarchie logiche
# ridurre duplicazioni (riduciamo il tempo di produzione)
# creare componenti riutilizzabili (come widget Tkinter personalizzati)

class Veicolo:
    # inserisco un costruttore vuoto, poi lo popolo
    def __init__(self, marca, modello):
        # inserisco 2 parametri, di tipo universale
        self._marca = marca
        self._modello= modello

    # informazioni, metodo che mi restituisce i parametri del veicolo in una stringa
    def info(self):
        return f"{self._marca} {self._modello}"
    
    def avvia(self):
        return f"WROOOM! Il veicolo {self.info()} si avvia!"
    
    def ferma(self):
        return f"STOP! Si è fermato..."
    


# faccio sì che la seguente classe abbia le stesse caratteristiche di quella precedente
# quindi creo la classe figlia
# metto fra parentesi i parametri della classe, in questo caso metto direttamente 'Veicolo':
class Auto(Veicolo):
    # devo cmq inserire l'inizializzazione con i vari parametri
    def __init__(self,marca,modello,porte):
        # vado a segnalare che la classe padre è la classe 'Veicolo'
        # uso perciò 'super().' è come un fare override della classe
        # devo sempre specificare ogni parametro da capo (usa copia e incolla)
        # NON devo specificare il 'self'
        super().__init__(marca, modello)
        # devo inizializzare anche il parametro mancante
        self._porte = porte

    def avvia(self):
        # uso lo stesso metodo ma in modo differente
        # posso quindi cambiare il msg
        # inserisco all'interno il metodo info
        # proprio perchè la classe figlia eredita dal padre
        return f"L'auto {self.info()} si avvia"
    


class Moto(Veicolo):
    def avvia(self):
        return f"La moto {self.info()} si avvia"
    
    

auto = Auto("Golf", "Serie 6", "5 porte")

moto = Moto("Kawasaki", "Ninja")

print(auto.info())
print(auto.avvia())

print(moto.info())
print(moto.avvia())



    




    

        

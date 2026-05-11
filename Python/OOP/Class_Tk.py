import tkinter as tk


class App:
# creo una nuova classe chiamata App
    def __init__(self, root):

        self.root = root
        # salvo la finestra principale dentro la classe

        # creo il pulsante grafico
        self.button = tk.Button(
            root,
            # metto il bottone dentro la finestra principale
            text="Cliccami",
            # mostro il testo sul bottone
            command=self.saluta
            # quando il bottone viene cliccato indico che 'saluta' 
            # non aggiungo le parentesi perchè non voglio che venga eseguito subito 
            # perchè non l'ho ancora definito, passo solo il riferimento alla funzione
        )

        self.button.pack(pady=20)
        # pack() serve per mostrare il bottone nella finestra
        # specifico che lo spazio verticale è di 20 pixel 

    def saluta(self):
        # definisco il metodo 'saluta' già citato prima 
        print("Ciao Studente")
        # quando il bottone viene cliccato verrà stampato 


root = tk.Tk()
# creo la finestra principale (graficamente parlando) dell'app

app = App(root)
# mi esegue in automatico '__init__' iniziale
# ossia creo l'oggetto App
# creando il bottone e inserendolo nella finestra

root.mainloop()
# indispensabile ed obbligatorio 
# mantiene la finestra aperta e sta in attesa degli eventi

"""
NOTA BENE:
1 - la sequenza di scrittura non corrisponde alla sequenza degli eventi
2 - abbiamo una parte di progettazione
3 - abbiamo una parte di definizione
4 - infine abbiamo la parte di creazione e avvio
5 - l'ordine di scrittura è preparatorio a quello di esecuzione
"""
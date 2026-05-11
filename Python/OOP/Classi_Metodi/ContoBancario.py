class ContoBancario:
    def __init__(self, saldo):
        self._saldo = saldo
        # creo la classe ContoBancario con unico attributo saldo
        
    def versamento(self, importo):
        # definisco il metodo 'versamento' con le condizioni
        if importo > 0:
            # se l'importo è maggiore di zero
            self._saldo += importo
            # allora lo sommerà al saldo
            print(f"Hai depositato questo importo {importo}")
        else:
             # se invece l'importo è uguale o minore di zero mi segnalerà:
            print(f"Importo non valido")

    def prelievo(self, importo):
        # definisco il metodo 'prelievo' con le condizioni
        if importo < 0:
            # se l'importo è minore di zero, mi segnalerà:
            print(f"Importo NON valido")
        elif importo > self._saldo:
            # se l'importo è maggiore del saldo disponibile, allora mi segnalerà:
            print(f"Saldo insufficiente")
        else: 
            # se l'importo è valido allora lo sottrarrà dal saldo
            self._saldo -=importo
            print(f"Importo prelevato {importo} €")


# - - - Programma principale - - -
print("/n=== CREA il TUO CONTO BANCARIO ===")
saldo_iniziale = float(input("Inserisci il tuo saldo iniziale: "))
# senza un saldo iniziale non potrò effettuare tutte le operazioni descritte

conto = ContoBancario(saldo_iniziale)
# creo un oggetto della classe ContoBancario usando saldo_iniziale come valore iniziale
# salvo quell’oggetto nella variabile conto

while True:
    # creo un ciclo 'WHILE':
    print("\n\n----- MENU'-----\n\n")
    print("1. Deposita")
    print("2. Preleva")
    print("3. Mostra Saldo")
    print("0. Esci\n")

    scelta = input("Scegli un'opzione: ")
    # definisco la variabile scelta, che sarà l'input per le opzioni

    if scelta == "1":
        importo = float(input("Quanto vuoi versare? "))
        # indico che l'importo potrà essere in numeri decimali con 'float'
        # definisco che l'importo è un input
        conto.versamento(importo)
        # indico che la variabile 'conto' effettuerà il metodo 'versamento'
        print(f"Il tuo nuovo saldo è {saldo_iniziale+importo} €")
        saldo_finale = saldo_iniziale+importo
        # introduco la variabile saldo_finale
    
    elif scelta == "2":
        importo = float(input("Quanto vuoi prelevare? "))
         # indico che l'importo potrà essere in numeri decimali con 'float'
        # definisco che l'importo è un input
        conto.prelievo(importo)
        # indico che la variabile 'conto' effettuerà il metodo 'prelievo'
        print(f"Il tuo nuovo saldo è {saldo_finale-importo} €")

    elif scelta == "3":
        # conto.mostra_saldo() se volessi usare questa formula, dovrei prima definire il metodo
        print(f"Il tuo saldo è {saldo_finale}")
        
    elif scelta == "0":
        print(f"Grazie e arrivederci")
        break
   
    else:
        print("Opzione non valida")






    """def mostra_saldo(self):
        print(f"Saldo attuale: {self._saldo} €")

    def __init__

conto = ContoBancario(250000)"""



 
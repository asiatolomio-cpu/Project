class ContoBancario:
    def __init__(self, saldo):
        self._saldo = saldo
        
    def versamento(self, importo):
        if importo > 0:
            self._saldo += importo
            print(f"Hai depositato questo importo {importo}")
        else:
            print(f"Importo non valido")

    def prelievo(self, importo):
        if importo < 0:
            print(f"Importo NON valido")
        elif importo > self.saldo:
            print(f"Saldo insufficiente")
        else: 
            self.saldo -=importo
            print(f"Importo prelevato {self._saldo} €")


# - - - Programma principale - - -
print("/n=== CREA il TUO CONTO BANCARIO ===")
saldo_iniziale = float(input("Inserisci il tuo saldo iniziale: "))

conto = ContoBancario(saldo_iniziale)

while True:
    print("\n\n----- MENU'-----\n\n")
    print("1. Deposita")
    print("2. Preleva")
    print("3. Mostra Saldo")
    print("0. Esci\n")

    scelta = input("Scegli un'opzione: ")

    if scelta == "1":
        importo = float(input("Quanto vuoi versare? "))
        conto.versamento(importo)
    
    elif scelta == "2":
        importo = float(input("Quanto vuoi prelevare?"))
        conto.prelievo(importo)

    elif scelta == "3":
        conto.mostra_saldo()
        
    elif scelta == "0":
        print(f"Grazie e arrivederci")
        break
   
    else:
        print("Opzione non valida")






    """def mostra_saldo(self):
        print(f"Saldo attuale: {self._saldo} €")

    def __init__

conto = ContoBancario(250000)"""



 
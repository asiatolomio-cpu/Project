# variabili e tipi di dati
# Python è case sensitive

nome = "Alice" # str (string) insieme di testo
cognome = "Bianchi" #str
eta = 36 # int (intero) numero intero
stipendio = 1.500 # float (decimale) numero con la virgola
attivo = True # boole (boolean) v / f
email = 'a.bianchi@email.com'

# al posto di scrivere tutto, stampo con la concatenazione
# uso il + per inserire le variabili senza riscriverle

# anche se nella dichiarazione del tipo per la variabile eta
# per far sì di stamparla, devo convertirla (temporaneamente) in string
# perchè una stringa non può essere concatenata ad un intero
print('Ciao mi chiamo ' + str(nome) + ' e ho ' + str(eta) + ' anni');
"""
altrimenti posso cambiare la tipologia della variabile eta 
nome = 'Alice'
eta = '36'
"""

print('Ciao mi chiamo ' + nome + ' e ho ' + str(eta) + ' anni');


print('tipo del nome => ' + str(type(nome)) + '= string')
# questo restituisce il tipo della variabile
# abbiamo inserito STR prima di chiedere il tipo della variabile perchè è preceduto da una stringa

print('tipo di eta =>' + str(type(eta)) + '= intero (1234567890)')
# a maggior ragione inserisco STR perchè la tipologia della variabile sarebbe int e quindi incompatibile con str

print('tipo dell\'età =>' + str(type(eta)) + '= intero (1234567890)') 
# se la stringa contiene un apostrofo lo faccio anticipare dal backslash 
# in modo da comunicare che è un carattere speciale

print(f'Ciao mi chiamo {nome} {cognome} e ho {eta} anni, la mia email {email}' )
# inserendo f all'inizio dell'argomento del print 
# seguito dall'apice e inserendo ciò che voglio stampare 
# (devo ricordarmi di inserire l'apice anche alla fine stringa)
# indico che tutto ciò che segue la f è in formato stringa
# evita che io debba inserire la concatenazione
# è una formattazione 





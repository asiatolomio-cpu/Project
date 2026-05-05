""" I cicli in python vengono introdotti  con
    FOR e  WHILE

    Un ciclo serve per ripetere un'azione più volte
    Esempio: Salutare 5 volte
        print("Ciao")
        print("Ciao")
        print("Ciao")
        print("Ciao")
        print("Ciao") 😅😅😅😅😅
    
    Con il ciclo for si usa quante volte ripetere un azione o qualcosa 
    
    
    🔁 DIFFERENZA TRA FOR E WHILE
    | FOR              | WHILE          |
    | ---------------- | -------------- |
    | Sai quante volte | Non sai        |
    | Più sicuro       | Più flessibile |
    | Usa range()      | Usa condizioni |

"""

"""
# Esempio 1: voglio inserire il numero delle righe in sequenza
print("Ordiniamo le righe")
for i in range(5):
     # range(contiene 5 elementi, gli ho indicato quante volte ripetere la generazione della riga da stampare) 
     # genera numeri: 0,1,2,3,4
     # se voglio aumentare il numero di righe fra parentesi dovrò cambiare il numero
    print(f"Riga {i}") 
    il 'print' dopo il 'for' va sempre indentato 
    # stamperà a schermo le righe da 0 a 4 (in totale 5 elementi: 0,1,2,3,4)
    # il range se non indicato diversamente parte sempre da 0 
"""



# Esempio 2:
# select * from Studenti Where nome in ('mario', 'luca', 'simona', 'andrea', 'melania')
# così ho selezionato una lista di nomi definita, per valori e per numero di elementi
# ho specificato in ordine il voto di ognuno, non un voto di più ne uno di meno
studenti = ['Mario', 'Luca', 'Simona', 'Andrea', 'Melania'] 
voti = [23, 30, 18, 16, 20]

"""
# con il codice seguente stamperò il nome dello studente, preso in ordine dalla lista 'studenti'
print("Lista degli studenti\n")
for studente in studenti: 
    # ho introdotto una variabile chiamata 'studente' che sarà ognuno degli elementi della lista 'studenti'
    print(f"Nome: {studente}\n")  
"""


print("Lista studenti con voti\n")
    # sarà la nostra intestazione della lista che potrà verrà specificata sotto

for i in range(len(studenti)):  
    # len(studenti) -> numero elementi
    # lo devo specificare perchè il range deve sempre avere un argomento fra parentesi
    print(f"Studente: {studenti[i]} - Voto: {voti[i]}")  
    # i -> indice (0,1,2 ..) per specificare la posizione da cui deve partire (ossia 0)
    # studenti[i] -> nome dello studente, specifico che le posizioni vanno abbinate 
    # voti[i] -> il voto dello studente, specifico come devono essere abbinate

  #Attenzione ⚠️
      #  👉 Le due liste devono avere stessa lunghezza
# Ho un dizionario chiave-valore nominato studenti
# finora l'ho stampato tutto 
# ma posso usare anche WHILE per stampare a schermo

studenti = {
    "mario" : 36,
    "luca" : 30,
    "simona" : 28,
    "andrea" : 25,
    "melania" : 29,
    "catalina" : 27,
    "giovanni" : 31,
    "giuseppe" : 26,
    "mattia": 32,
    "francesca" : 24
}
#  WHILE lavora con indici (0,1,2,3..), mentre il dizionario no.
# Quindi trasformiamo la chiave in lista
# Definisco la lista 'nomi' e la lista 'voti'
# specificando appunto che è una lista con '= list'
# come argomento inserisco il nome del dizionario 
# quale sia la chiave e quali siano i valori

nomi = list(studenti.keys())
voti = list(studenti.values())

i = 0
# inizializzo il ciclo a 0

# inserisco il WHILE
# il ciclo si ripete finché la condizione è vera
# in questo caso la condizione è: 
while i < len(nomi): 
    # ossia 'finche l'indice è minore della lunghezza della lista nomi'
    nome = nomi[i]
    # la variabile è 'nome', dalla lista 'nomi' definisco che indicizzo  
    voto = studenti[nome]
    # la variabile è 'voto' che avrà l'abbinamento dal dizionario 'studenti' e dalla chiave 'nome'
    print(f"Studente: {nome} - Voto: {voto}")
    i += 1 
    # indico che l'indice si incrementa di 1 alla volta 
    # ossia andrà a nominare singolarmente tutti gli elementi della lista
    

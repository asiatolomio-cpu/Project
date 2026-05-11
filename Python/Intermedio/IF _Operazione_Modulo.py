# qual è la risposta? num = 25
# L’operatore % calcola il resto della divisione
if num % 5 == 0:
    # prima condizione: il resto della divisione per 5 è 0?
    # 25:5 = 5, non ha resto --> quindi 0 == 0? --> Sì!!! Passiamo alla seconda condizione
    if num % 2 == 0:
        # seconda condizione: il resto della divisione per 2 è 0?
        # 25:2 = 12, con resto 1 --> quindi 1 == 0? --> NO!! Quindi la risposta è 'Python'
        print("Java")
    else:
        # poichè 1 non è uguale a 0 allora la risposta rientra nella seconda condizione e la risposta è 'Python'
        print("Python")
else:
    print("C++")
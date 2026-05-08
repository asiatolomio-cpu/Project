import matplotlib.pyplot as plt
import numpy as np

# Creiamo una lista competenze
labels = np.array(['Coding', 'Teoria', 'Progetto', 'Data Analyst', 'Reverse engineering', 'Sviluppo', 'Testing', 'Documentazione']) # crea un array di etichette per le competenze elencate

# Valori per uno studente
stats = np.array([8, 7, 9, 6, 5, 8, 7, 6]) # valori di competenza per uno studente in ciascuna delle competenze elencate in "labels"
"""
    LOGICA
    np.linspace(0, 2*np.pi, len(labels): crea un array di angoli equidistanti tra 0 e 2*pi, con un numero di elementi pari al numero di etichette nelle competenze
    endpoint=False: esclude il punto finale 2*pi dall'array di angoli, in modo che le etichette siano posizionate in modo circolare senza sovrapporsi
    .tolist(): converte l'array di angoli in una lista, che può essere utilizzata per posizionare le etichette in un grafico radar o a ragnatela
"""
angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist() # crea un array di angoli per posizionare le etichette in modo circolare
angles += angles[:1] # aggiunge il primo angolo alla fine dell'array di angoli per chiudere il grafico radar
stats = np.concatenate((stats, [stats[0]])) # aggiunge il primo valore di competenza alla fine dell'array di valori per chiudere il grafico radar

""" IMPOSTAZIONE GRAFICO RADAR """
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True)) # crea una figura di dimensioni 8x8 pollici e un subplot con coordinate polari per il grafico radar
ax.plot(angles, stats, color='red', linewidth=2, linestyle='solid') # traccia una linea che collega i punti del grafico radar, con colore rosso, spessore di 2 e stile solido
ax.fill(angles, stats, color='red', alpha=0.20) # riempie l'area sotto la linea del grafico radar con colore rosso e trasparenza del 20%
ax.set_xticks(angles[:-1]) # imposta le posizioni delle etichette sui punti del grafico radar, escludendo l'ultimo punto che è una ripetizione del primo
ax.set_xticklabels(labels) # imposta le etichette delle competenze sui punti del grafico radar
ax.set_title('Competenze dello Studente') # aggiunge un titolo al grafico radar

plt.show() # visualizza il grafico radar creato







"""
    np.linspace(0, 2*np.pi, len(labels): Divide il cerchio in pari uguali.
        Se hai 5 competenze,  crea 5 angoli (0°. 72°, 144, 216°, 288°)
    
    0, 2*np.pi: Corrisponde a 360° 
        
    endpoint=False: Dice a python di non finire aseettamente a 360°,
    perché 360° conincide con 0°


angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
# Chiude il cerchio
stats = np.concatenate((stats, [stats[0]]))
angles = np.concatenate((angles, [angles[0]]))

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

ax.fill( stats, color='red', alpha=0.25)
ax.plot( stats, color='red', linewidth=2)

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_yticklabels(labels)

plt.title('Profilo competenze: Alessio', size=15, color='green', y=1.1)

plt.show()
"""
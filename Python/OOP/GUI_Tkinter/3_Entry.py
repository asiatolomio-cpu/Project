import tkinter as tk
from openpyxl import Workbook, load_workbook
import os

root = tk.Tk()

# titolo della finestra
root.title("Entry Form con Tkinter")

# dimensione della finestra
root.geometry("550x550")

# colore sfondo della finestra
root.configure(bg="#0A9142")

# creazione dell'entry
entry = tk.Entry(
    root,
    width=30,
    font=("Roboto", 16)
)

# creazione della label con il msg di cosa l'utente inserirà
Label = tk.Label(
        root,
        text="Inserisci il tuo nome",
        font=("Roboto",20,"bold"),
        fg="#0A9142",
        bg="black",
        cursor="hand1"
        )

Label.pack(pady=50)


# immaginiamo di avere un modulo da inserire
# con 0 indichiamo che la stringa che segue ha valore di default
# entry.insert(0, "Inserisci il tuo nome")

entry.pack(pady=20)

# metodo che legge i valori inseriti dall'utente
def legge_testo():
    # la 'get()' recupera il testo inserito dall'utente
    nome = entry.get()

    # andiamo a stampare
    print(f"Ti chiami {nome}")

# il widget di tipo bottone che viene da Tkinter
# tk.Button().pack()
# sarebbe la shortcut per creare il bottone salva:
button = tk.Button(
    root,
    text="Salva",
    command= legge_testo
)

button.pack(pady=20)


# avvio applicazione
root.mainloop()
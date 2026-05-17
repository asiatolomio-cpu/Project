import tkinter as tk
from tkinter import messagebox

# creazione finestra principale
root = tk.Tk()


root.title("Todo-List")
root.geometry("600x500")
root.configure(bg="blue")


tk.Label(
        root,
        text ="Compila la tua TO-DO-LIST!",
        font = ("Oswald", 30, "italic"),
        bg = "blue",
        fg = "white"# colore del testo
    ).pack(pady=20)

# Entry, dove l''utente inserirà testo/input
entry = tk.Entry(
    root,
    font=("Oswald", 14),
    width=25)

# mostra la entry nella finestra
entry.pack(pady=10)

# funzione per aggiungere una voce alla lista, oppure per avvisare che non si è scritto nulla
# fa parte delle funzioni CRUD (Create, Read, Update, Delete)
def aggiungi():
    # legge il testo scritto nella entry
    # strip rimuove gli spazio iniziali/finali
    testo = entry.get().strip()

    # controlla che il testo non sia vuoto
    if testo:
        # se il testo è vero ossia non nullo
        # allora lo inserisce nella Listbo
        lb.insert(tk.END, testo)

        # svuota la entry 
        entry.delete(0,tk.END)
    else:
        # mostra popup di avviso 
        messagebox.showwarning("Attenzione", "Inserisci un'attività")

def mostra():
    # restituisce l'indice dell'elemento selezionato
    idx = lb.curselection()
    if idx:
        # se esiste una selezione
        # mostra il teso selezoinato
        messagebox.showwarning("Attività selezionata", lb.get(idx[0]))
    else: 
        # se la selezione non esiste 
        # mostra il messaggio
        messagebox.showinfo("Info", "Nessuna attività selezionata")

def rimuovi():
    # legge l'elemento selezionato
    idx = lb.curselection()
    if idx:
        # se la selezione è valida
        # cancella quanto selezionato
        lb.delete(idx[0])
    else:
        # se la selezione non esiste 
        # mostra il messaggio
        messagebox.showwarning("Attenzione", "Nessuna attività selezionata")

def modifica():
    # legge la selezione corrente
    idx = lb.curselection()
    # legge il nuovo testo della entry
    # elimina gli spazi (prima/dopo)
    nuovo_testo = entry.get().strip()
    if not idx:
       # controlla che un elemento sia selezionato
       messagebox.showwarning("Errore", "Nessuna attività selezionata per la modifica")
       return
    
    if not nuovo_testo:
        # controlla che il nuovo testo esista
        messagebox.showwarning("Errore", "Inserisci il nuovo testo")
        return
        
    lb.delete(idx[0])
    # elimina il vecchio elemento
        
    lb.insert(idx[0], nuovo_testo)
    # inserisce il nuovo testo

    entry.delete(0,tk.END)
    #pulisce la entry

def cerca_in_entry():
    idx = lb.curselection()
    if idx:
        entry.delete(0, tk.END)
        entry.insert(idx[0], lb.get(idx[0]))
    


# Frame bottone con listbox 
frame_btn = tk.Frame(root)
frame_btn.pack(padx=10)


tk.Button(frame_btn, 
          text="Aggiungi",
          width=12,
          #font=("Oswald", 12),
         command=aggiungi).grid(row=0,column=0, padx=5,pady=5)

tk.Button(frame_btn, 
          text="Mostra",
          width=12,
          #font=("Oswald", 12),
         command=mostra).grid(row=0,column=1, padx=5,pady=5)

tk.Button(frame_btn, 
          text="Elimina",
          width=12,
          #font=("Oswald", 12),
         command=rimuovi).grid(row=0,column=2, padx=5,pady=5)

tk.Button(frame_btn,
          text="Modifica",
          width=12,
          #font=("Oswald", 12),
          command=modifica).grid(row=0,column=3, padx=5,pady=5)

frame_lists = tk.Frame(root)
frame_lists.pack(padx=10, pady=5)


# decido come fare la scrollbar, in questo caso verticale
scrollbar = tk.Scrollbar(frame_lists, orient="vertical")

# introduco una label per la lista 
lb = tk.Listbox(frame_lists, 
                height=12, 
                width=30,
                font=("Oswald", 14),
                yscrollcommand=scrollbar.set)
# selectmode=tk.SINGLE)  # o tk.MULTIPLE per selezioni multiple

scrollbar.config(command=lb.yview)

lb.pack(side="left")
scrollbar.pack(side="right", fill="y")
lb.bind("<<ListboxSelect>>", cerca_in_entry)


root.mainloop()


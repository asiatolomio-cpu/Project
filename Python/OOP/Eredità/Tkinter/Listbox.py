import tkinter as tk
from tkinter import messagebox
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

# Entry
entry = tk.Entry(
    root,
    font=("Oswald", 14),
    width=25)

entry.pack(pady=10)

# funzione per aggiungere una voce alla lista, oppure per avvisare che non si è scritto nulla
# fa parte delle funzioni CRUD (Create, Read, Update, Delete)
def aggiungi():
    testo = entry.get().strip()
    if testo:
        # se il tempo è vero ossia non nullo
        lb.insert(tk.END, testo)
        entry.delete(0,tk.END)
    else:
        messagebox.showwarning("Attenzione", "Inserisci un'attività")

def mostra():
    idx = lb.curselection()
    if idx:
        messagebox.showwarning("Attenzione", "Seleziona un'attività", lb.get(idx[0]))
    else: 
        messagebox.showinfo("Info: nessuna attività selezionata")

def rimuovi():
    idx = lb.curselection()
    if idx:
        lb.delete(idx[0])
    else:
        messagebox.showwarning("Attenzione", "Nessuna attività selezionata")

def modifica():
    idx = lb.curselection()
    nuovo_testo = entry.get().strip()
    if not idx:
       messagebox.showwarning("Errore", "Nessuna attività selezionata per la modifica")
       return
    
    if not nuovo_testo:
        messagebox.showwarning("Errore", "Inserisci il nuovo testo")
        return
        
    lb.delete(idx[0])
    lb.insert(idx[0], nuovo_testo)
    entry.delete(0,tk.END)

def cerca_in_entry():
    idx = lb.curselection()
    if idx:
        entry.delete(0, tk.END)
        entry.insert(idx[0], lb.get(idx[0]))
    


# Frame con listbox 
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


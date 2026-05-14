import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title("Scegliamo un linguaggio di programmazione")

root.geometry("800x600")

root.minsize(350,500)

root.geometry("800x600+200+200")

root.configure(bg="#bdd2f0")

root.resizable(True, True)

# Checkbutton — variabile collegata BooleanVar
# le opzioni sono 'premuto' e 'non premuto'
var_check = tk.BooleanVar()
check = tk.Checkbutton(
    root,
    fg="white",
    text="Accetta termini",
    variable=var_check,
    background="#072E2D",
    selectcolor="#072E2D"
    )
check.pack(pady=10)

# dove punta di default la variabile del radiobutton
var_radio = tk.StringVar(value="python")

# creiamo una lista di Linguaggi 
# selezione = list(linguaggi.keys())
# ritorno = list(linguaggi.values())


# ciclo for per recuperare chiave e valore
# radiobutton con il ciclo per collegare la lista di linguaggi
# abbiamo dichiarato che la variabile è in formato stringa
linguaggi =["Python","python",
             "Java", "java",
             "Javascript", "js",
             "C++","cpp",
             "SQL Server","t-server",
             "HTML","html",
             "XML","xml",
             "GoLang","golang",
             "MicroPython","micropython",
             "Turbo Pascal","turbopascal",
             "Pascal","pascal",
             "Assembly","assembly",
             "MongoDB","mongodb",
             "Delphy","delphy",
             "Js","js"]
for testo , valore in linguaggi:
    tk.Radiobutton(
        root, 
        fg="white",
        text=testo, 
        value=valore,
        background="#bdd2f0",
        variable=var_radio, 
        selectcolor="#072E2D").pack(anchor="w", padx=20)


def mostra():
    messagebox.showinfo("Selezione", 
                        f"Accetta termini:{var_check.get()}\n"
                        f"Linguaggio scelto:{var_radio.get()}")

tk.Button(root, text="Mostra selezione", command=mostra).pack(pady=10)
root.mainloop()
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
check = tk.Checkbutton(root, text="Accetta termini", variable=var_check)
check.pack()

# creiamo una lista di Linguaggi 
linguaggi = {"Python": "python",
             "Java": "java",
             "C++":"cpp",
             "SQL":"sql server",
             "HTML":"html",
             "XML":"xml",
             "GoLang":"golang",
             "MicroPython":"micropython",
             "Turbo Pascal":"turbopascal",
             "Pascal":"pascal",
             "Assembly":"assembly",
             "MongoDB":"mongodb",
             "Delphy":"delphy",
             "Js":"js"}

selezione = list(linguaggi.keys())
ritorno = list(linguaggi.values())

# ciclo for per recuperare chiave e valore

# Radiobutton — variabile collegata StringVar
var_radio = tk.StringVar(value="python")
tk.Radiobutton(root, text="Python", variable=var_radio, value="python").pack()
tk.Radiobutton(root, text="Java",   variable=var_radio, value="java").pack()
tk.Radiobutton(root, text="C++",    variable=var_radio, value="cpp").pack()
tk.Radiobutton(root, text="HTML",    variable=var_radio, value="html").pack()
tk.Radiobutton(root, text="GoLang",    variable=var_radio, value="golang").pack()
tk.Radiobutton(root, text="TurboPascal",    variable=var_radio, value="turbo").pack()
tk.Radiobutton(root, text="MicroPython",    variable=var_radio, value="micropython").pack()


def mostra():
    messagebox.showinfo(var_check.get(), var_radio.get())

tk.Button(root, text="Mostra selezione", command=mostra).pack(pady=10)
root.mainloop()
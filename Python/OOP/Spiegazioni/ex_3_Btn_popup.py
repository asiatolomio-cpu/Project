""" CONSEGNA
Crea una applicazione usando Tkinter + OOP come abbiamo visto oggi con:
Requisiti:
1️⃣ finestra con:
titolo
dimensione fissa
colore sfondo
2️⃣ una Label con scritto:

Benvenuto Studente
3️⃣ un bottone:

Saluta
4️⃣ quando clicchi il bottone:
mostra un popup con:

Ciao, benvenuto nel corso Python!

REGOLE

❌ NON usare funzioni fuori dalla classe
✔ tutto deve stare

 dentro una classe App
💡 AIUTO
       Ricorda:
       
           class App:
e:

command=self.nome_metodo
"""
import tkinter as tk
from tkinter import messagebox

class Nuova_App:
    def __init__(self,root):
        self.root = root

        self.root.title("Benvenuto nella tua nuova app")

        self.root.geometry("1800x10000")

        self.root.configure(bg="#f54927")

        self.root.resizable(True,True)

        self.titolo = tk.Label(
            root,
            text="Benvenuto Studente",
            font=("Aptos", 24, "bold"),
            fg="white",
            bg="#1447E6"
        )

        self.titolo.pack(pady=245)

        self.bottone = tk.Button(
            root,
            text="Ciao!",
            command=self.mostra_popup,
            font=("Aptos",24, "italic bold"),
            bg="#1447E6",
            fg="black",
            padx= 135,
            pady= 65
        )

        self.bottone.pack()

    def mostra_popup(self):
        messagebox.showinfo(
            "Ti saluto",
            "Ciao, benvenuto nel corso Python!"
        )

root = tk.Tk()

app= Nuova_App(root)

root.mainloop()
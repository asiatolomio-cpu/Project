import tkinter as tk
from tkinter import messagebox

class button_esempio:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Esempio con classe")

        button = tk.Button(
            self.root,
            text = "Cliccami!",
            command = self.saluta
        )

        button.pack(pady=30)

        self.label = tk.Label(
        self.root,
        text="Benvenuto",
        font=("Arial",20,"bold"),
        fg="#ffffff",
        bg="#847274",
        cursor="hand2"
        )

        self.label.pack(pady=50)

    def salutaAsia(self):
        messagebox.showinfo(
            "Ciao!"
            "Ciao, benvenuto nel corso Python!")
        
    def saluta(self):
        self.label.configure(
        text="E' stato un piacere"
        )

    def avvia(self):
        self.root.mainloop()

class esegui():
    app = button_esempio()
    app.avvia()
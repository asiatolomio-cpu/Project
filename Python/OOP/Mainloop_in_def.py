import tkinter as tk

class button_esempio:
    def __init__(self):
        self.root = tk.Tk
        self.root.title("Esempio con classe")

        button = tk.Button(
            self.root,
            text = "Cliccami!",
            command = self.salutaAsia
        )

        button.pack(pady=30)

    def salutaAsia(self):
        print("Ciao!")

    def avvia(self):
        self.root.mainloop()

class esegui():
    app = button_esempio()
    app.avvia()
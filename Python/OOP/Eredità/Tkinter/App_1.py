# Importiamo i pacchetti di librerie che ci servono
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# importiamo per grafica e canvas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class App:
    def __init__(self):
        # finestra principale
        self.root = tk.Tk()
        self.root.title("Grafico con Tkinter + Matplotlib + OOP")
        self.root.geometry("800x600")

        # impostiamo il frame superiore(bottone)
        top_frame = tk.Frame(self.root)
        top_frame.pack(pady=20)

        # impostiamo il bottone per generare il grafico
        btn = tk.Button(
            top_frame,
            text="Genera grafico",
            command=self.genera_grafico
        )
        btn.pack()

        # impostiamo il frame per il grafico
        self.graph_frame = tk.Frame(self.root)
        self.graph_frame.pack(
            fill= "both",
            expand= True
        )

    def genera_grafico(self):
        # cancelliamo il grafico precedente (se esiste)
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        # inseriamo dei dati di esempio (fake o db, json, excel, cvs, pdf, docx, xml ecc...)
        x = [1,2,3,4,5,7,12,13,17,24,31,56]
        y =[10,20,25,30,55,71,76,78,83,89,97,100]

        # creiamo la figur tramite Matplotlib
        fig, ax = plt.subplots(figsize=(6,4))
        ax.plot(
            x,
            y,
            marker= "o",
            color="blue" )
        ax.set_title("Andamento Valori")
        ax.set_xlabel("Etichetta X")
        ax.set_ylabel("Etichetta Y")

        # inseriamo graficamente tramite Tkinter
        canvas = FigureCanvasTkAgg(
            fig,
            master=self.graph_frame
        )
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
        
    def run(self):
        self.root.mainloop()

if __name__== "__main__":
    app = App()
    app.run()


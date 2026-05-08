import tkinter as tk

root = tk.Tk()

# Titolo della finestra
root.title("Imparo ad usare Tkinter")

# Dimensioni: larghezza x altezza (in stringa)
root.geometry("800x600")

# Dimensioni minime 
root.minsize(350,500)

# Dimensioni per la modifica alle dimensioni da cursore 
# Parte dalle dimensioni minime, passa alle standard, mentre qui sotto segno le massime
# Non come valore assoluto ma come 'aggiunte'
root.geometry("800x600+200+200")

# Colore di sfondo ('bg' sta per background)
# Se non abbiamo il cursore per scegliere posso andare su https://htmlcolorcodes.com/ per indicare il codice
root.configure(bg="#77a9ef")

# Decido il ridimensionamento mettendo False e True (il primo è la larghezza, il secondo l'altezza)
# True lo abilita
# False lo impedisce
root.resizable(True, True)




tk.Label().pack(pady=20)
# padx/pady è il padding interno orizzontale/verticale
# width/height sono le dimensioni in caratteri/pixel
# label = widget non modificabile (è una costante)


# Imposto la label 
tk.Label(
    root,
    text ="Ciao, Tkinter!",
    font = ("Arial", 50, "italic"),
    bg = "#77a9ef",
    fg = "#000000",# colore del testo
    cursor = "hand2" 
).pack(pady=50)

root.mainloop()

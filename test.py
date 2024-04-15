import tkinter 
import sqlite3

base1 = sqlite3.connect('bases_dades/objectes')

items = base1.cursor()

ventana = tkinter.Tk()

label_texto = tkinter.Label(ventana, text = items.execute("select * from items"), font=("Arial",18), fg="#07cf00", bg="#000000")
label_texto.pack(padx=20,pady=10)

ventana.mainloop()
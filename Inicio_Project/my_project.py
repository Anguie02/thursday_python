#Improtamos tkinte
from tkinter import *
#Creamos la ventana principal(un objeto) a partir de la clase TK
window = Tk()
#Agregamos un titulo y definimos las dimenciones de la ventana
window.title("Ferretería El Tornillo Feliz ")
window.geometry("600x400")
#Añadimos un icono
window.iconbitmap("tornillo.ico")
#Añadimos la clase Label
caja_dni = Label(window, text="DNI", bg="sky blue")
caja_dni.place(x=10,y=10,width=100, height=30)

window.mainloop()
from tkinter import *
import os.path

class Programa:
    def __init__(self):
        self.title="Master en python"
        self.icon = "./images/facebook_icon-icons.com_59205.ico"
        self.icon_alt = "./21 - Tkinter/images/facebook_icon-icons.com_59205.ico"
        self.size ="770x470"
        self.resizable=False

    def cargar(self):
        ruta_ico = os.path.abspath(self.icon)        
        ventana = Tk()
        self.ventana = ventana
        text = Label(self.ventana, text=ruta_ico)
        text.pack()
        if os.path.isfile(ruta_ico):
            ventana.iconbitmap(self.icon)
        else:
            ventana.iconbitmap(self.icon_alt)

        ventana.title(self.title)
        ventana.geometry(self.size)
        if self.resizable:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)
        #arrancar y mostrat ventana hasta que se cierre        
    
    def addTexto(self):
        text = Label(self.ventana, text="Hola desde metodo")
        text.pack()
    
    def mostrar(self):
        self.ventana.mainloop()

programa = Programa()

programa.cargar()
programa.addTexto()
programa.mostrar()
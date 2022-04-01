
import tkinter as tk
from tkinter import *
from Templates import welcome
import tkinter as tk
import Gestor_App.preguntas as preguntas
    
class Ventana(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        #self.geometry("800x500")
        self.title("Juego de Preguntas")
        self.img_welcome = tk.PhotoImage(file="Img/welcome.gif")
        self.config(bg="black")
        #self.resizable(width=False, height=False)
        self.lista=preguntas.choose_question(preguntas.preguntas)
        self.switch_frame(welcome.welcome)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self,self.img_welcome,self.lista)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid(padx=100,pady=50)
        

import tkinter as tk
from tkinter import ttk
from tkinter import *
from Templates import JuegoApp
import Gestor_App.preguntas as preguntas

class Question_frame(ttk.Frame):
    def __init__(self,container,lista,master,p):
        super().__init__(container)
        self.lista=lista
        self.master=master
        self.p=p
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.__create_widgets()

    def __create_widgets(self):
        frame1=tk.Frame(self, background="black",width=700,height=500)
        frame1.grid(sticky="ew",padx=150,pady=50)
        lista_preguntas=self.lista
        pregunta=lista_preguntas[0]
        opcionA=lista_preguntas[1]
        opcionB=lista_preguntas[2]
        opcionC=lista_preguntas[3]
        opcionD=lista_preguntas[4]
        correcta=lista_preguntas[5]
        tk.Label(frame1, text=pregunta,
                               font=("Monaco",12),fg="white",bg="black",relief= "solid",justify= LEFT).grid(row=0,column=0,columnspan=2,pady=50)
        tk.Button(frame1, text=opcionA,command=lambda: self.verificar(pregunta,opcionA,correcta,self.p),width=25).grid(row=1,column=0)
        tk.Button(frame1, text=opcionB,command=lambda: self.verificar(pregunta,opcionB,correcta,self.p),width=25).grid(row=2,column=0)
        tk.Button(frame1, text=opcionC,command=lambda: self.verificar(pregunta,opcionC,correcta,self.p),width=25).grid(row=1,column=1)
        tk.Button(frame1, text=opcionD,command=lambda: self.verificar(pregunta,opcionD,correcta,self.p),width=25).grid(row=2,column=1)

        for widget in self.winfo_children():
            widget.grid(padx=5, pady=5)
    def verificar(master,pregunta,opcion,correcta,p):
        listass=[]
        listass.append(pregunta)
        listass.append(opcion)
        listass.append(correcta)
        if p=="1":
            preguntas.puntuacion(listass)
            JuegoApp.preguntaOne.verificar(master)
        elif p=="2":
            preguntas.puntuacion(listass)
            JuegoApp.preguntaTwo.verificar(master)
        elif p=="3":
            preguntas.puntuacion(listass)
            JuegoApp.preguntathree.verificar(master)
        elif p=="4":
            preguntas.puntuacion(listass)
            JuegoApp.preguntaFour.verificar(master)
        else:
            preguntas.puntuacion(listass)
            JuegoApp.preguntaFive.verificar(master)

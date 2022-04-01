from doctest import master
import tkinter as tk
from tkinter import *
import Gestor_App.preguntas as preguntas
import Templates.index as index
from Templates import JuegoApp
import DataBase.DB as DB
from Templates import welcome

class bases(tk.Frame):
    def __init__(self, master,img_welcome,lista):
        tk.Frame.__init__(self, master)
        frame_bases=tk.Frame(self, background="black",width=700,height=500)
        frame_bases.grid(sticky='news')
        tk.Label(frame_bases, text="Historial de Resultados",
                               font=("Monaco",12),fg="white",bg="black",relief= "solid",justify= LEFT).grid(row=0,column=0,columnspan=4)
        tk.Label(frame_bases, text="Nombre Jugador",
                               font=("Monaco",12),fg="white",bg="black",relief= "solid",justify= LEFT).grid(row=1,column=0,padx=3)
        tk.Label(frame_bases, text="Juegos",
                               font=("Monaco",12),fg="white",bg="black",relief= "solid",justify= LEFT).grid(row=1,column=1,padx=3)
        tk.Label(frame_bases, text="Tiempo",
                               font=("Monaco",12),fg="white",bg="black",relief= "solid",justify= LEFT).grid(row=1,column=2,padx=3)
        tk.Label(frame_bases, text="Cantidad \nrespuestas \ncorrectas",
                               font=("Monaco",12),fg="white",bg="black",relief= "solid",justify= LEFT).grid(row=1,column=3,padx=3)
        l=DB.mostrar_db()
        for i in range(0,len(l)):
            ind=2+i
            jugador=l[i][0]
            juegos=l[i][1]
            t=l[i][2]
            cant=l[i][3]
            tk.Label(frame_bases, text=jugador,
                               font=("Monaco",12),fg="white",bg="black",relief= "solid",justify= LEFT).grid(row=ind,column=0)
            tk.Label(frame_bases, text=juegos,
                               font=("Monaco",12),fg="white",bg="black",relief= "solid",justify= LEFT).grid(row=ind,column=1)
            tk.Label(frame_bases, text=t,
                               font=("Monaco",12),fg="white",bg="black",relief= "solid",justify= LEFT).grid(row=ind,column=2)
            tk.Label(frame_bases, text=cant,
                               font=("Monaco",12),fg="white",bg="black",relief= "solid",justify= LEFT).grid(row=ind,column=3)
            tk.Button(frame_bases, text="Volver a jugar",
                                     command=lambda: [master.switch_frame(JuegoApp.Game),preguntas.borrar()]).grid(row=6,column=0,columnspan=2, pady=15)
            tk.Button(frame_bases, text="Salir",
                                     command=lambda: self.volver()).grid(row=6,column=2,columnspan=2, pady=15)
    def volver(self) :
        self.master.quit()
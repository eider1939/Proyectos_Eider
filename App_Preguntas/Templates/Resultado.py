
import tkinter as tk
from tkinter import *
import Gestor_App.preguntas as preguntas
import Templates.JuegoApp as JuegoApp
import DataBase.DB as DB
from Templates import Db_resultados
from datetime import datetime

class Final(tk.Frame):
    def __init__(self, master,img_welcome,lista):
        tk.Frame.__init__(self, master)
        frame_Respuesta=tk.Frame(self, background="black",width=700,height=500)
        frame_Respuesta.grid(sticky='news')
        tk.Label(frame_Respuesta, text="Resultados",
                               font=("Monaco",12),fg="white",bg="black",relief= "solid",justify= LEFT).grid(row=0,column=0,columnspan=4)
        tk.Label(frame_Respuesta, text="Preguntas",
                               font=("Monaco",12),fg="white",bg="black",relief= "solid",justify= LEFT).grid(row=1,column=0,padx=3)
        tk.Label(frame_Respuesta, text="Respuesta",
                               font=("Monaco",12),fg="white",bg="black",relief= "solid",justify= LEFT).grid(row=1,column=1,padx=3)
        tk.Label(frame_Respuesta, text="Opcion \nCorrecta",
                               font=("Monaco",12),fg="white",bg="black",relief= "solid",justify= LEFT).grid(row=1,column=2,padx=3)
        tk.Label(frame_Respuesta, text="Puntuacion",
                               font=("Monaco",12),fg="white",bg="black",relief= "solid",justify= LEFT).grid(row=1,column=3,padx=3)
        resultados=preguntas.l
        opciones=preguntas.opcion1
        puntaje_final=0
        for i in range(0,len(opciones)):
            ind=2+i
            pregunta=opciones[i][0]
            opc=opciones[i][1]
            corr=opciones[i][2]
            tk.Label(frame_Respuesta, text=pregunta,
                               font=("Monaco",12),fg="white",bg="black",relief= "solid",justify= LEFT).grid(row=ind,column=0)
            tk.Label(frame_Respuesta, text=opc,
                               font=("Monaco",12),fg="white",bg="black",relief= "solid",justify= LEFT).grid(row=ind,column=1)
            tk.Label(frame_Respuesta, text=corr,
                               font=("Monaco",12),fg="white",bg="black",relief= "solid",justify= LEFT).grid(row=ind,column=2)
            if resultados[i]=="1":
                tk.Label(frame_Respuesta, text="1",
                               font=("Monaco",14),fg="green",bg="black",relief= "solid",justify= LEFT).grid(row=ind,column=3)
                puntaje_final+=1
            
            else:
                tk.Label(frame_Respuesta, text="0",
                               font=("Monaco",14),fg="red",bg="black",relief= "solid",justify= LEFT).grid(row=ind,column=3)
        
        tk.Label(frame_Respuesta, text="Puntuacion Final",
                               font=("Monaco",18),fg="white",bg="black",relief= "solid",justify= LEFT).grid(row=7,column=0,columnspan=2,pady=30)

        tk.Label(frame_Respuesta, text=str(puntaje_final),
                               font=("Monaco",18),fg="white",bg="black",relief= "solid",justify= LEFT).grid(row=7,column=3,columnspan=2,pady=30)
        tk.Label(frame_Respuesta, text="Tiempo",
                               font=("Monaco",18),fg="white",bg="black",relief= "solid",justify= LEFT).grid(row=8,column=0,columnspan=2,pady=20)
        ti=JuegoApp.tiempo_total
        tk.Label(frame_Respuesta, text=str(ti),
                               font=("Monaco",18),fg="white",bg="black",relief= "solid",justify= LEFT).grid(row=8,column=2,columnspan=2,pady=20)
        tk.Button(frame_Respuesta, text="Acomulados",
                  command=lambda: [DB.valores(),master.switch_frame(Db_resultados.bases)]).grid(row=9,column=0,columnspan=4, pady=10)
            
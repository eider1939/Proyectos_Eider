import tkinter as tk
from tkinter import *
from Templates import welcome
import Gestor_App.preguntas as preguntas
from Templates import Resultado
from Templates import preguntas_page
from Templates import time
import DataBase.DB as DB

time_inicio=0
time_final=0
tiempo_total=0

class Game(tk.Frame):
    def __init__(self, master,img_welcome,lista):
        tk.Frame.__init__(self, master,)
        tk.Frame.configure(self,bg='black')
        frame_info=tk.Frame(self, background="black",width=800,height=500)
        frame_info.grid(sticky="ew")
        tk.Label(frame_info, text="                  Elige un Jugador             ",
                               font=("Monaco",12),fg="white",bg="black",relief= "solid",justify= LEFT).grid(row=0,column=0,pady=50,sticky="sw")
        tk.Button(self, text="Player A",
                  command=lambda: [master.switch_frame(Games),DB.registrarse("Player A")]).grid(row=1,column=0,pady=10)
        tk.Button(self, text="Player B",
                  command=lambda: [master.switch_frame(Games),DB.registrarse("Player B")]).grid(row=2,column=0,pady=10)
        tk.Button(self, text="Go back to welcome",
                  command=lambda: master.switch_frame(welcome.welcome)).grid(row=3,column=0, pady=10)

class Games(tk.Frame):
    def __init__(self, master,img_welcome,lista):
        tk.Frame.__init__(self, master,)
        tk.Frame.configure(self,bg='black')
        frame_info=tk.Frame(self, background="black",width=700,height=500)
        frame_info.grid(sticky="ew")
        tk.Label(frame_info, text='''INFORMACIÓN:\nEl juego conciste en respoder una serie de preguntas \nde cultura general, se debera responder 5 pregutas \nestas son genredas aleatoriamente, al final se dara el \npuntutaje y el tiempo utilizado para responder\n\n''',
                               font=("Monaco",12),fg="white",bg="black",relief= "solid",justify= LEFT).grid(row=0,column=0,pady=50)
        tk.Button(self, text="Go back to welcome",
                  command=lambda: master.switch_frame(welcome.welcome)).grid(row=1,column=0)
        tk.Button(self, text="INICIAR",
                  command=lambda: master.switch_frame(preguntaOne)).grid(row=2,column=0,pady=10)

class preguntaOne(tk.Frame):
    def __init__(self, master,img_welcome,lista):
        tk.Frame.__init__(self, master,)
        #tk.Frame.configure(self,bg='black')
        frame_info=tk.Frame(self, background="black",width=700,height=500)
        frame_info.grid(sticky="ew",columnspan=2)
        global time_inicio
        time_inicio=time.start()
        formato=preguntas_page.Question_frame(frame_info,lista[0],master,"1")
        formato.pack()
    def verificar(self):
       self.master.switch_frame(preguntaTwo)

class preguntaTwo(tk.Frame):
    def __init__(self, master,img_welcome,lista):
        tk.Frame.__init__(self, master,)
        #tk.Frame.configure(self,bg='blue')
        frame_info=tk.Frame(self, background="black",width=700,height=500)
        frame_info.grid(sticky="ew",columnspan=2)
        formato=preguntas_page.Question_frame(frame_info,lista[1],master,"2")
        formato.pack()
    
    def verificar(self):
       self.master.switch_frame(preguntathree)

class preguntathree(tk.Frame):
    def __init__(self, master,img_welcome,lista):
        tk.Frame.__init__(self, master,)
        #tk.Frame.configure(self,bg='blue')
        frame_info=tk.Frame(self, background="black",width=700,height=500)
        frame_info.grid(sticky="ew",columnspan=2)

        formato=preguntas_page.Question_frame(frame_info,lista[2],master,"3")
        formato.pack()
    
    def verificar(self):
       self.master.switch_frame(preguntaFour)


class preguntaFour(tk.Frame):
    def __init__(self, master,img_welcome,lista):
        tk.Frame.__init__(self, master,)
        tk.Frame.configure(self,bg='blue')
        frame_info=tk.Frame(self, background="black",width=700,height=500)
        frame_info.grid(sticky="ew",columnspan=2)
        formato=preguntas_page.Question_frame(frame_info,lista[3],master,"4")
        formato.pack()
    
    def verificar(self):
       self.master.switch_frame(preguntaFive)

class preguntaFive(tk.Frame):
    def __init__(self, master,img_welcome,lista):
        tk.Frame.__init__(self, master,)
        tk.Frame.configure(self,bg='blue')
        frame_info=tk.Frame(self, background="black",width=700,height=500)
        frame_info.grid(sticky="ew",columnspan=2)
        formato=preguntas_page.Question_frame(frame_info,lista[4],master,"5")
        formato.pack()
        global time_final
        time_final=time.stop()
        global tiempo_total
        tiempo_total=time.tiempo(time_inicio,time_final)
    def verificar(self):
       self.master.switch_frame(Resultado.Final)
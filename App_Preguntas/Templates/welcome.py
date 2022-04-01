
import tkinter as tk
from tkinter import *
from turtle import heading
from Templates import JuegoApp

class welcome(tk.Frame):
    def __init__(self, master,img_welcome,lista):
        tk.Frame.__init__(self, master)
        frame_welcome=tk.Frame(self, background="black",width=700,height=500)
        frame_welcome.grid(sticky='news')
        photo1 = tk.Label(frame_welcome, image=img_welcome)
        photo1.grid(row=0, column=0,columnspan=2,sticky='news')
        Button(frame_welcome, text="Play",command=lambda: master.switch_frame(JuegoApp.Game)).grid(row=1, column=0,columnspan=2,padx=60,sticky='e')
        
        tk.Label(frame_welcome, text="Aplicaion creada por: \nEider Alejandro Peña Dagua",
                               font=("Monaco",12),fg="white",bg="black",relief= "solid",justify= LEFT).grid(row=2,column=1)




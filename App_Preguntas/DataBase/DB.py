from datetime import date
from time import time
from tkinter import ttk,messagebox
import sqlite3
import Gestor_App.preguntas as preguntas
import Templates.JuegoApp as JuegoApp
from datetime import datetime
nombre=" "
def registrarse(Name):
    global nombre
    nombre = Name
    conn = sqlite3.connect('usuariosBD.sqlite')
    cur= conn.cursor()
    #cur.execute('DROP TABLE IF EXISTS usuarios')
    cur.execute('CREATE TABLE if not exists usuarios (name VARCHAR(128), juegos INTEGER(100), tiempo datetime, correctas INTEGER(128))') 
    cur.execute("SELECT * FROM usuarios WHERE name=?", (nombre,))
    r = cur.fetchall()
    if r:
        pass
    else:
        cur.execute('INSERT INTO usuarios (name,juegos,tiempo,correctas) VALUES (?,?,?,?)', (Name,0,"00:00:00",0))
        conn.commit()
    cur.close()

def valores():
    tiempo=JuegoApp.tiempo_total
    opciones=preguntas.l
    correctas=0
    for i in opciones:
        if i=="1":
            correctas+=1
    conn = sqlite3.connect('usuariosBD.sqlite')
    cur= conn.cursor()
    cur.execute("SELECT juegos,time(tiempo),correctas FROM usuarios WHERE name=?", (nombre,))
    rows = cur.fetchall()
    jue=0
    tim=""
    corr=0
    for row in rows:
        jue=row[0]
        tim=row[1]
        corr=row[2]
    fecha_dt = datetime.strptime(tim, '%H:%M:%S')
    suma=fecha_dt + tiempo
    if nombre=="Player A":
        sql_update_query = """Update usuarios set juegos = ?,tiempo=?, correctas=? where name=?"""
        data = (jue+1,str(suma.strftime("%H:%M:%S")),correctas+corr,nombre)
        cur.execute(sql_update_query, data)
        conn.commit()
    else:
        sql_update_query = """Update usuarios set juegos = ?,tiempo=?, correctas=? where name=?"""
        data = (jue+1,str(suma.strftime("%H:%M:%S")),correctas+corr,nombre)
        cur.execute(sql_update_query, data)
        conn.commit()
    cur.close()

def mostrar_db():
    db_lista=[]
    conn = sqlite3.connect('usuariosBD.sqlite')
    cur= conn.cursor()
    cur.execute("SELECT * FROM usuarios")
    rows = cur.fetchall()
    for i in range(0,len(rows)):
        db_lista.append(rows[i])
    cur.close()
    return db_lista
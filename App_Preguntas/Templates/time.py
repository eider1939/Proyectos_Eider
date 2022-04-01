import  time
from datetime import datetime
def start():
    inicio_de_tiempo = datetime.now()
    return inicio_de_tiempo
def stop():
    tiempo_final = datetime.now()
    return tiempo_final
def tiempo(inicio,final):
    tiempo_transcurrido = final - inicio
    return tiempo_transcurrido

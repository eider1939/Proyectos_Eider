import random
 
preguntas = [
    ["¿Cuál es el río más largo del mundo?","Nilo","Misisipi","congüe","Amazonas","Amazonas"],
    ["¿Cuál es el país con más habitantes del mundo?","China","India","Estados unidos","Indonecia","China"],
    ["¿Cuál es el edificio más alto del mundo?","Torre de Shanghái","Burj Khalifa","Merdeka 118","Abraj Al Bait","Burj Khalifa"],
    ["¿Dónde está Transilvania?","Bulgaria","Hungria","Moldavia","Rumania","Rumania"],
    ["¿Cuál es el país con menos habitantes del mundo?","La Ciudad del Vaticano","Tuvalu","Nauru","Monaco","La Ciudad del Vaticano"],
    [" ¿En qué año cayó el muro de Berlín?","1986","1989","1990","1988","1989"],
    ["¿Cuántos años duró la Primera Guerra Mundial?","5","3","4","6","4"],
    [" ¿Cuántos años duró la Segunda Guerra Mundial?","5","6","7","4","6"],
    [" ¿Cuándo empezó la Revolución Rusa?","1917","1918","1910","1915","1917"],
    ["¿Cuál es el océano más grande del mundo?","Atlántico","Pacífico","Indico","Artico","Pacífico"],
    ["¿Cuándo llegó Cristóbal Colón a América?","El 12 de octubre de 1492","El 12 de junio de 1493","El 2 de octubre de 1941","El 1 de enero de 1493.","El 12 de octubre de 1492"],
    ["¿Cómo se llama la capital de Mongolia?","Bangkok","Ulan Bator","Manila","Yakarta","Ulan Bator"],
    ["¿Qué cantidad de huesos en el cuerpo humano \nal nacer?","206","300","250","230","300"],
    ["¿Quién pintó “la última cena”?","Leonardo da Vinci","Donatello","Vincent van Gogh","Miguel Ángel","Leonardo da Vinci"],
    ["¿En qué se especializa la cartografía?","Cartas","Mapas","Jeroglíficos","Papiros","Mapas"],
    ["Si 50 es el 100%, ¿cuánto es el 90%?","46","40","35","45","45"],
    ["¿En qué lugar del cuerpo se produce la insulina?","Higado","páncreas","Estomago","Vesicula","páncreas"],
    ["¿De qué estilo arquitectónico es la \nCatedral de Notre Dame en París?","Barroca","Gótico","victoriana","Neoclásica","Gótico"],
    ["¿Quién escribió “Hamlet”?","William Shakespeare","Anne Hathaway","León Tolstói","Miguel de Cervantes","William Shakespeare"],
    ["¿Quién escribió “Crimen y castigo”?","William Shakespeare","León Tolstói","Franz Kafka","Fiódor Dostoyevski","Fiódor Dostoyevski"],
    ["El triángulo que tiene sus tres lados \niguales ¿Cómo se llama?","Escaleno","Rectangulo","Equilátero","Isóceles","Equilátero"],
    ["¿Cuál es la capital de Dinamarca?","Copenhague","Oslo","Estocolmo","Helsinki","Copenhague"],
    ["¿Cuál es el país con más camellos salvajes?","Irán","Australia","Egipto","Libia","Australia"],
    ["¿Cuántos corazones tienen los pulpos?","3","4","2","1","3"],
    ["¿En qué año viajó al espacio el primer ser humano?","1961","1960","1965","1958","1961"],
    ["¿Cuál es el “País del Sol Naciente”?","China","Australia","Japon","Filipinas","Japon"],
    ["¿Cuánto te da si sumas los números 1-100 \nconsecutivamente (1 + 2 + 3 + 4 + 5…)?","5050","5500","5250","5555","5050"],
    ["¿Qué formula es esta? S = π x R²","Diámetro de un círculo","Superficie de un círculo","Volumen de un cilindro","Superficie de un paralelogramo","Superficie de un círculo"],
    ["¿Cuántas válvulas tiene el corazón humano?","Dos","Tres","Cuatro","Seis","Cuatro"],
    ["¿De dónde es originario el croissant?","Austria","Francia","Belgica","Holanda","Austria"]
]

def choose_question(ask):
  preguntas_juego=[]
  for i in range(0,10):
    p=random.choice(ask)
    if p not in preguntas_juego:
      preguntas_juego.append(p)
  return preguntas_juego

l=[]
opcion1=[]
def puntuacion(opcion):
  opcion1.append(opcion)
  if opcion[1]==opcion[2]:
    l.append("1")
  else:
    l.append("0")

def borrar():
  global l
  l=[]
  global opcion1
  opcion1=[]
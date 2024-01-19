import random
import time

baraja = [
    '2 ' + chr(3), '3 ' + chr(3), '4 ' + chr(3) , '5 ' + chr(3), '6 ' + chr(3), '7 ' + chr(3), '8 ' + chr(3),
    '9 ' + chr(3), '10 ' + chr(3), 'J ' + chr(3), 'Q ' + chr(3), 'K ' + chr(3), 'A ' + chr(3),
    '2 ' + chr(4), '3 ' + chr(4), '4 ' + chr(4), '5 ' + chr(4), '6 ' + chr(4), '7 ' + chr(4), '8 ' + chr(4),
    '9 ' + chr(4), '10 ' + chr(4), 'J ' + chr(4), 'Q ' + chr(4), 'K ' + chr(4), 'A ' + chr(4),
    '2 ' + chr(6), '3 ' + chr(6), '4 ' + chr(6), '5 ' + chr(6), '6 ' + chr(6), '7 ' + chr(6), '8 ' + chr(6),
    '9 ' + chr(6), '10 ' + chr(6), 'J ' + chr(6), 'Q ' + chr(6), 'K ' + chr(6), 'A ' + chr(6),
    '2 ' + chr(5), '3 ' + chr(5), '4 ' + chr(5), '5 ' + chr(5), '6 ' + chr(5), '7 ' + chr(5), '8 ' + chr(5),
    '9 ' + chr(5), '10 ' + chr(5), 'J ' + chr(5), 'Q ' + chr(5), 'K ' + chr(5), 'A ' + chr(5)
]
baraja1=baraja

cartas_jugador1=[]

def floop(numero_cartas1):
    return random.sample(baraja1, numero_cartas1)

def apostar():
    apuesta=int(input("Cuanto deseas apostar?"))
    botet(apuesta)

def botet(algo):
    bote=0
    bote+=algo
    print("El bote es:", bote)

def ciega():
    ciega_pequeña=int(input("Ingrese la ciega pequeña:"))
    ciega_grande=ciega_pequeña*2
    apuesta_ciega=int(input("Que deseas apostar ahora:"))
    while apuesta_ciega<ciega_grande:
        print("Es una apuesta muy pequeña prueba con una mas grande")
        apuesta_ciega=int(input("Cuantos quieres apostar?"))
    botet(apuesta_ciega)
def repartir_cartas(numero_cartas):
    return random.sample(baraja, numero_cartas)
    

def pregunta():
    n=input("Que quieres hacer ahora? (apostar/retirarse)")
    if n=="apostar" or n=="Apostar":
        apostar()
    if n=="Retirarse" or n=="retirarse":
        exit()

def repartir(cartas):
    mano_jugador=repartir_cartas(52)
    n=0
    while n<cartas:
        print(mano_jugador[n])
        cartas_jugador1.append(mano_jugador[n])
        n=n+1


#def ciega():
 #   ciega_pequeña=int(input("Ingrese la ciega pequeña"))
  #  ciega_grande=ciega_pequeña*2


#print("Tu mano:") 
#repartir(2)
ciega()
#pregunta()
#print("El flop es:")
#repartir(3)

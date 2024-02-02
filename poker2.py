import random
import time
import bot
import prueba

prueba.baraja()
bote = 0
max_credito=500

cartas_jugador1=[]


def cartas_jugador():
    random.shuffle(baraja)

def repartir(n):
    cartas_jugador()
    i=0
    while i<n:
        print(baraja[i])
        cartas_jugador1.append(baraja[i])
        baraja.pop(i)
        i=i+1

def flop(n):
    cartas_jugador()
    i=0
    while i<n:
        print(baraja[i])
        cartas_jugador1.append(baraja[i])
        bot.cartasbot.append(baraja[i])
        i=i+1

def apostar():
    apuesta=int(input("Cuanto deseas apostar?"))
    global max_credito
    botet(apuesta)
    max_credito-=apuesta

def botet(algo):
    global bote
    bote+=algo
    print("El bote es:", bote)

ciega_pequeña=int(input("Ingrese la ciega pequeña:"))
ciega_grande=ciega_pequeña*2
sumaciega=ciega_grande+ciega_pequeña
print("La ciega grande es:", ciega_grande)
botet(sumaciega)
def ciega():
    apuesta_ciega=int(input("Que deseas apostar ahora:"))
    while apuesta_ciega<ciega_grande:
        print("Es una apuesta muy pequeña prueba con una mas grande")
        apuesta_ciega=int(input("Cuantos quieres apostar?"))
    botet(apuesta_ciega)

    

def pregunta():
    n=input("Que quieres hacer ahora? (apostar/retirarse)")
    if n=="apostar" or n=="Apostar":
        apostar()
    if n=="Retirarse" or n=="retirarse":
        exit()


def botap(algo):
    bot = random.randint(1,10)
    if 9>bot>=1:
        print("El bot a decidido apostar")
        dudi= random.randrange(ciega_grande, algo)
        print("El bot ha apostado:", dudi)
        botet(dudi)
    else:
        print("El bot ha decidido retirarse, Has ganado:")
        botet(0)
        exit()
    




print("Tu mano:") 
repartir(2)
print("  ")
bot.repartir(2)
print("El flop es:")
flop(3)
print(" ".join(cartas_jugador1))
print(" ".join(bot.cartasbot))
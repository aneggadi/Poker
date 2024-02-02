import random
import time
import bot

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
bote = 0
max_credito=int(input("Con cuanto dinero quieres jugasr?:"))

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
        time.sleep(1)
        i=i+1

def flop(n):
    cartas_jugador()
    i=0
    while i<n:
        print(baraja[i])
        cartas_jugador1.append(baraja[i])
        bot.cartasbot.append(baraja[i])
        time.sleep(1)
        i=i+1

def apostar():
    apuesta=int(input("Cuanto deseas apostar?"))
    global max_credito
    botet(apuesta)
    max_credito-=apuesta

def botet(algo):
    global bote
    bote+=algo
    time.sleep(1)
    print("El bote es:", bote)

ciega_pequeña=int(input("Ingrese la ciega pequeña:"))
ciega_grande=ciega_pequeña*2
sumaciega=ciega_grande+ciega_pequeña
time.sleep(1)
print("La ciega grande es:", ciega_grande)
botet(sumaciega)
def ciega():
    apuesta_ciega=int(input("Cuanto deseas apostar?:"))
    while apuesta_ciega<ciega_grande:
        print("Es una apuesta muy pequeña prueba con una mas grande")
        ciega()
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
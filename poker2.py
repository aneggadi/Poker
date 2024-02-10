import random
import time
import bot

#creamos una baraja
baraja1 = [
    '2 ' + chr(3), '3 ' + chr(3), '4 ' + chr(3) , '5 ' + chr(3), '6 ' + chr(3), '7 ' + chr(3), '8 ' + chr(3),
    '9 ' + chr(3), '10 ' + chr(3), 'J ' + chr(3), 'Q ' + chr(3), 'K ' + chr(3), 'A ' + chr(3),
    '2 ' + chr(4), '3 ' + chr(4), '4 ' + chr(4), '5 ' + chr(4), '6 ' + chr(4), '7 ' + chr(4), '8 ' + chr(4),
    '9 ' + chr(4), '10 ' + chr(4), 'J ' + chr(4), 'Q ' + chr(4), 'K ' + chr(4), 'A ' + chr(4),
    '2 ' + chr(6), '3 ' + chr(6), '4 ' + chr(6), '5 ' + chr(6), '6 ' + chr(6), '7 ' + chr(6), '8 ' + chr(6),
    '9 ' + chr(6), '10 ' + chr(6), 'J ' + chr(6), 'Q ' + chr(6), 'K ' + chr(6), 'A ' + chr(6),
    '2 ' + chr(5), '3 ' + chr(5), '4 ' + chr(5), '5 ' + chr(5), '6 ' + chr(5), '7 ' + chr(5), '8 ' + chr(5),
    '9 ' + chr(5), '10 ' + chr(5), 'J ' + chr(5), 'Q ' + chr(5), 'K ' + chr(5), 'A ' + chr(5)
]
def ns():
    global baraja
    baraja=baraja1
bote = 0
#funcion del credito inicial
def credito():
    global max_credito
    max_credito=int(input("Con cuanto dinero quieres empezar jugando?"))
max_creditbot=random.randrange(500,1000)
time.sleep(0.5)

#cartas vacias para agregar las cartas 
cartas_jugador1=[]

#funcion para cunado el bot se retire
def salirvictoria():
    global bote
    print("has ganado la partida y con ello has ganado", bote)
    exit()

#funcion para cuando te retires
def salirderrota():
    global bote
    print("has perdido la partida y con ello has perdido", bote)
    exit()

#funcion para saber si se agota el credito y si se agota preguntar si quieres aumetntarlo o retirarte 
def menos_del_max():
    global max_credito
    if max_credito<0:
        que_paso=input("Tu credito se ha agotado que desea hacer? aumentar el credito a retirarse (aumentar/retirarse)")
        if que_paso=="aumentar":
            aumentarcreditos=int(input("cuanto quieres aumentar tu credito?"))
            max_credito+=aumentarcreditos
        if que_paso=="retirarse":
            salirderrota()

#funcion para saber si el bot se ha quedado sin presupuesto y entonces se retira
def menos_creditos_bot():
    global max_creditbot
    if max_creditbot<0:
        print("El bot no tiene mas dinero")
        salirvictoria()

#mezcla la baraja
def shuffle():
    random.shuffle(baraja)

#funcion que reparte al jugador añade las cartas repartidas a tus cartas y elimina esas cartas de la baraja
def repartir(n):
    shuffle()
    i=0
    while i<n:
        print(baraja[i])
        cartas_jugador1.append(baraja[i])
        baraja.pop(i)
        time.sleep(1)
        i=i+1

#repartimos el flop que se mete dentro de tus y las del bot y se eliminan de la baraja
def flop(n):
    shuffle()
    i=0
    while i<n:
        print(baraja[i])
        cartas_jugador1.append(baraja[i])
        bot.cartasbot.append(baraja[i])
        baraja.pop(i)
        time.sleep(1)
        i=i+1

#haces la apuesta se añade al bote compara si sigues teniendo dinero y cuando tu haces la apuestsa el bot tambien hace otra
def apostar():
    global max_credito
    global max_creditbot
    apuesta=int(input("Cuanto deseas apostar?"))
    botet(apuesta)
    max_credito-=apuesta
    menos_del_max()
    time.sleep(1)
    botap(max_creditbot)

#funcion para que se guarde las cantidades apostadas en el bote
def botet(algo):
    global bote
    bote+=algo
    time.sleep(1)
    print("El bote es:", bote)

#la ciega que es la primera apuestsa que se hace 
def ciega():
    global ciega_grande
    global max_credito
    ciega_pequeña=int(input("Ingrese la ciega pequeña:"))
    ciega_grande=ciega_pequeña*2
    sumaciega=ciega_grande+ciega_pequeña
    max_credito-=ciega_pequeña
    time.sleep(1)
    print("La ciega grande es:", ciega_grande)
    botet(sumaciega)

#posticega es la apuesta justo despues de la ciega ya que tiene que ser siempre mayor o igual que la ciega grande
def postciega():
    global max_credito
    apuesta_ciega=int(input("Cuanto deseas apostar?:"))
    if apuesta_ciega<ciega_grande:
        print("Es una apuesta muy pequeña prueba con una mas grande")
        ciega()
    else:
        botet(apuesta_ciega)
        max_credito-=apuesta_ciega
        menos_del_max()

    
#funcion para saber si deseas apostar o retirarse y si apuestas llama de nuevo a la funcion apostar
def pregunta():
    n=input("Que quieres hacer ahora? (apostar/retirarse)")
    if n=="apostar" or n=="Apostar":
        apostar()
    if n=="Retirarse" or n=="retirarse":
        salirderrota()

#esta esla funcion de la apuesta del bot (el bot tiene una posibilidad de 1 entre 10 de retirarse)
def botap(algo):
    global max_creditbot
    global ciega_grande
    bot = random.randint(1,10)
    if 9>=bot>=1:
        print("El bot a decidido apostar")
        dudi = random.randrange(ciega_grande, algo)
        print("El bot ha apostado:", dudi)
        botet(dudi)
        max_creditbot-=dudi
        max_creditbot-=ciega_grande
    else:
        print("El bot ha decidido retirarse, Has ganado:")
        salirvictoria()
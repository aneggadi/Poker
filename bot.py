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
cartasbot=[]


def cartas_bot():
    random.shuffle(baraja)

def repartir(n):
    cartas_bot()
    i=0
    while i<n:
        print(baraja[i])
        cartasbot.append(baraja[i])
        baraja.pop(i)
        i=i+1

#def repartir_bot(cartas):
    #mano_bot=cartas_bot()
    #n=0
    #while n<cartas:
    #    print(mano_bot[n])
     #   cartasbot.append(mano_bot[n])
      #  time.sleep(1)
       # n=n+1
        #baraja.pop(n)





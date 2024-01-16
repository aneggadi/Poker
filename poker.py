import random
import time

# Baraja de cartas
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
baraja1 = baraja
 
# Función para repartir cartas
def repartir_cartas(numero_cartas):
    return random.sample(baraja, numero_cartas)
 
# Ejemplo de repartición de cartas
mano_jugador = repartir_cartas(5)
n=0
flop=0
print("Tu mano:")
while n<2:
    print(mano_jugador[n])
    time.sleep(1)
    n=n+1
time.sleep(1)
ciega_pequeña=int(input("Cuanto va a ser la ciega pequeña ciegas pequeña?"))
ciega_grande=ciega_pequeña*2
retirarse=input("Que desea hacer ahora? (Apostar/Retirarse)")
if retirarse=="Retirarse":
    print("Su apuesta ha terminado")
    exit()
else:
    if retirarse=="Apostar":
        ap=int(input("Cuantosquieres apostar?"))
        while ap<ciega_grande:
            print("Es una apuesta muy pequeña prueba con una mas grande")
            ap=int(input("Cuantosquieres apostar?"))
time.sleep(1)
print("El flop es:")
while flop<3:
    print(mano_jugador[flop])
    flop=flop+1
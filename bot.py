import random
import time 
import poker2

poker2.baraja
cartasbot=[]


def repartir(n):
    i=0
    while i<n:
        cartasbot.append(poker2.baraja[i])
        poker2.baraja.pop(i)
        i=i+1

import random
import time 
import poker2

#Definimos la var cartasbot como una lista para despues añadir elementos
cartasbot=[]

#Funcion para repartir las cartas del bot y eliminarlas de la baraja
def repartir(n):
    i=0
    while i<n:
        cartasbot.append(poker2.baraja[i])
        poker2.baraja.pop(i)
        i=i+1
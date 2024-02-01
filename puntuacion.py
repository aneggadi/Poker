import poker2

def cartas(n,tipo):
    for m in range (4):
        if poker2.cartas_jugador1[m] == n:
            tipo+=1
    if tipo==5:
        #ordenar lista de menor a mayor
        min=poker2.cartas_jugador1[0]
        min1=min+1
        min2=min1+1
        min3=min2+1
        min4=min3+1
        if poker2.cartas_jugador1[0]==10 and poker2.cartas_jugador1[1]==11 and poker2.cartas_jugador1[2]==12 and poker2.cartas_jugador1[3]==13 and poker2.cartas_jugador1[4]==11:
            valor=99
        elif min1==poker2.cartas_jugador1[1] and min2==poker2.cartas_jugador1[2] and min3==poker2.cartas_jugador1[3] and min4==poker2.cartas_jugador1[4]:
            valor=98
            val_max=min4
        else:
            valor=95      #asignar valor a color
            val_max=min4
            val_max2=min3
            val_max3=min2
            val_max4=min1
            val_max5=min
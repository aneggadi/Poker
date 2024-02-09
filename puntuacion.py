import poker2
import bot

def numjugador(numcartas):
    global dos; global tres; global cuatro; global cinco; global seis; global siete; global ocho; global nueve; global diez; global jota; global reina; global rey; global ass
    dos=0; tres=0; cuatro=0; cinco=0; seis=0; siete=0; ocho=0; nueve=0; diez=0; jota=0; reina=0; rey=0; ass=0
    for i in range(numcartas):
        if poker2.cartas_jugador1[i]=='2 ' + chr(3) or poker2.cartas_jugador1[i]=='2 ' + chr(4) or poker2.cartas_jugador1[i]=='2 ' + chr(5) or poker2.cartas_jugador1[i]=='2 ' + chr(6):
            dos+=1
        elif poker2.cartas_jugador1[i]=='3 ' + chr(3) or poker2.cartas_jugador1[i]=='3 ' + chr(4) or poker2.cartas_jugador1[i]=='3 ' + chr(5) or poker2.cartas_jugador1[i]=='3 ' + chr(6):
            tres+=1
        elif poker2.cartas_jugador1[i]=='4 ' + chr(3) or poker2.cartas_jugador1[i]=='4 ' + chr(4) or poker2.cartas_jugador1[i]=='4 ' + chr(5) or poker2.cartas_jugador1[i]=='4 ' + chr(6):
            cuatro+=1
        elif poker2.cartas_jugador1[i]=='5 ' + chr(3) or poker2.cartas_jugador1[i]=='5 ' + chr(4) or poker2.cartas_jugador1[i]=='5 ' + chr(5) or poker2.cartas_jugador1[i]=='5 ' + chr(6):
            cinco+=1
        elif poker2.cartas_jugador1[i]=='6 ' + chr(3) or poker2.cartas_jugador1[i]=='6 ' + chr(4) or poker2.cartas_jugador1[i]=='6 ' + chr(5) or poker2.cartas_jugador1[i]=='6 ' + chr(6):
            seis+=1
        elif poker2.cartas_jugador1[i]=='7 ' + chr(3) or poker2.cartas_jugador1[i]=='7 ' + chr(4) or poker2.cartas_jugador1[i]=='7 ' + chr(5) or poker2.cartas_jugador1[i]=='7 ' + chr(6):
            siete+=1
        elif poker2.cartas_jugador1[i]=='8 ' + chr(3) or poker2.cartas_jugador1[i]=='8 ' + chr(4) or poker2.cartas_jugador1[i]=='8 ' + chr(5) or poker2.cartas_jugador1[i]=='8 ' + chr(6):
            ocho+=1
        elif poker2.cartas_jugador1[i]=='9 ' + chr(3) or poker2.cartas_jugador1[i]=='9 ' + chr(4) or poker2.cartas_jugador1[i]=='9 ' + chr(5) or poker2.cartas_jugador1[i]=='9 ' + chr(6):
            nueve+=1
        elif poker2.cartas_jugador1[i]=='10 ' + chr(3) or poker2.cartas_jugador1[i]=='10 ' + chr(4) or poker2.cartas_jugador1[i]=='10 ' + chr(5) or poker2.cartas_jugador1[i]=='10 ' + chr(6):
            diez+=1
        elif poker2.cartas_jugador1[i]=='J ' + chr(3) or poker2.cartas_jugador1[i]=='J ' + chr(4) or poker2.cartas_jugador1[i]=='J ' + chr(5) or poker2.cartas_jugador1[i]=='J ' + chr(6):
            jota+=1
        elif poker2.cartas_jugador1[i]=='Q ' + chr(3) or poker2.cartas_jugador1[i]=='Q ' + chr(4) or poker2.cartas_jugador1[i]=='Q ' + chr(5) or poker2.cartas_jugador1[i]=='Q ' + chr(6):
            reina+=1
        elif poker2.cartas_jugador1[i]=='K ' + chr(3) or poker2.cartas_jugador1[i]=='K ' + chr(4) or poker2.cartas_jugador1[i]=='K ' + chr(5) or poker2.cartas_jugador1[i]=='K ' + chr(6):
            rey+=1
        elif poker2.cartas_jugador1[i]=='A ' + chr(3) or poker2.cartas_jugador1[i]=='A ' + chr(4) or poker2.cartas_jugador1[i]=='A ' + chr(5) or poker2.cartas_jugador1[i]=='A ' + chr(6):
            ass+=1

def numbot(cartasrepartidas):
    global dos; global tres; global cuatro; global cinco; global seis; global siete; global ocho; global nueve; global diez; global jota; global reina; global rey; global ass
    dos=0; tres=0; cuatro=0; cinco=0; seis=0; siete=0; ocho=0; nueve=0; diez=0; jota=0; reina=0; rey=0; ass=0
    for i in range(cartasrepartidas):
        if bot.cartasbot[i]=='2 ' + chr(3) or bot.cartasbot[i]=='2 ' + chr(4) or bot.cartasbot[i]=='2 ' + chr(5) or bot.cartasbot[i]=='2 ' + chr(6):
            dos+=1
        elif bot.cartasbot[i]=='3 ' + chr(3) or bot.cartasbot[i]=='3 ' + chr(4) or bot.cartasbot[i]=='3 ' + chr(5) or bot.cartasbot[i]=='3 ' + chr(6):
            tres+=1
        elif bot.cartasbot[i]=='4 ' + chr(3) or bot.cartasbot[i]=='4 ' + chr(4) or bot.cartasbot[i]=='4 ' + chr(5) or bot.cartasbot[i]=='4 ' + chr(6):
            cuatro+=1
        elif bot.cartasbot[i]=='5 ' + chr(3) or bot.cartasbot[i]=='5 ' + chr(4) or bot.cartasbot[i]=='5 ' + chr(5) or bot.cartasbot[i]=='5 ' + chr(6):
            cinco+=1
        elif bot.cartasbot[i]=='6 ' + chr(3) or bot.cartasbot[i]=='6 ' + chr(4) or bot.cartasbot[i]=='6 ' + chr(5) or bot.cartasbot[i]=='6 ' + chr(6):
            seis+=1
        elif bot.cartasbot[i]=='7 ' + chr(3) or bot.cartasbot[i]=='7 ' + chr(4) or bot.cartasbot[i]=='7 ' + chr(5) or bot.cartasbot[i]=='7 ' + chr(6):
            siete+=1
        elif bot.cartasbot[i]=='8 ' + chr(3) or bot.cartasbot[i]=='8 ' + chr(4) or bot.cartasbot[i]=='8 ' + chr(5) or bot.cartasbot[i]=='8 ' + chr(6):
            ocho+=1
        if bot.cartasbot[i]=='9 ' + chr(3) or bot.cartasbot[i]=='9 ' + chr(4) or bot.cartasbot[i]=='9 ' + chr(5) or bot.cartasbot[i]=='9 ' + chr(6):
            nueve+=1
        if bot.cartasbot[i]=='10 ' + chr(3) or bot.cartasbot[i]=='10 ' + chr(4) or bot.cartasbot[i]=='10 ' + chr(5) or bot.cartasbot[i]=='10 ' + chr(6):
            diez+=1
        if bot.cartasbot[i]=='J ' + chr(3) or bot.cartasbot[i]=='J ' + chr(4) or bot.cartasbot[i]=='J ' + chr(5) or bot.cartasbot[i]=='J ' + chr(6):
            jota+=1
        if bot.cartasbot[i]=='Q ' + chr(3) or bot.cartasbot[i]=='Q ' + chr(4) or bot.cartasbot[i]=='Q ' + chr(5) or bot.cartasbot[i]=='Q ' + chr(6):
            reina+=1
        if bot.cartasbot[i]=='K ' + chr(3) or bot.cartasbot[i]=='K ' + chr(4) or bot.cartasbot[i]=='K ' + chr(5) or bot.cartasbot[i]=='K ' + chr(6):
            rey+=1
        if bot.cartasbot[i]=='A ' + chr(3) or bot.cartasbot[i]=='A ' + chr(4) or bot.cartasbot[i]=='A ' + chr(5) or bot.cartasbot[i]=='A ' + chr(6):
            ass+=1    
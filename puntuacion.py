import poker2
import bot


puntostotalesbot=0
puntostotales=0
def puntosjugador(cartasrepartidas):
    global puntostotales
    for i in range(cartasrepartidas):
        if poker2.cartas_jugador1[i]=='2 ' + chr(3) or poker2.cartas_jugador1[i]=='2 ' + chr(4) or poker2.cartas_jugador1[i]=='2 ' + chr(5) or poker2.cartas_jugador1[i]=='2 ' + chr(6):
            puntostotales=puntostotales+1
        if poker2.cartas_jugador1[i]=='3 ' + chr(3) or poker2.cartas_jugador1[i]=='3 ' + chr(4) or poker2.cartas_jugador1[i]=='3 ' + chr(5) or poker2.cartas_jugador1[i]=='3 ' + chr(6):
            puntostotales=puntostotales+2
        if poker2.cartas_jugador1[i]=='4 ' + chr(3) or poker2.cartas_jugador1[i]=='4 ' + chr(4) or poker2.cartas_jugador1[i]=='4 ' + chr(5) or poker2.cartas_jugador1[i]=='4 ' + chr(6):
            puntostotales=puntostotales+3
        if poker2.cartas_jugador1[i]=='5 ' + chr(3) or poker2.cartas_jugador1[i]=='5 ' + chr(4) or poker2.cartas_jugador1[i]=='5 ' + chr(5) or poker2.cartas_jugador1[i]=='5 ' + chr(6):
            puntostotales=puntostotales+4
        if poker2.cartas_jugador1[i]=='6 ' + chr(3) or poker2.cartas_jugador1[i]=='6 ' + chr(4) or poker2.cartas_jugador1[i]=='6 ' + chr(5) or poker2.cartas_jugador1[i]=='6 ' + chr(6):
            puntostotales=puntostotales+5
        if poker2.cartas_jugador1[i]=='7 ' + chr(3) or poker2.cartas_jugador1[i]=='7 ' + chr(4) or poker2.cartas_jugador1[i]=='7 ' + chr(5) or poker2.cartas_jugador1[i]=='7 ' + chr(6):
            puntostotales=puntostotales+6
        if poker2.cartas_jugador1[i]=='8 ' + chr(3) or poker2.cartas_jugador1[i]=='8 ' + chr(4) or poker2.cartas_jugador1[i]=='8 ' + chr(5) or poker2.cartas_jugador1[i]=='8 ' + chr(6):
            puntostotales=puntostotales+7
        if poker2.cartas_jugador1[i]=='9 ' + chr(3) or poker2.cartas_jugador1[i]=='9 ' + chr(4) or poker2.cartas_jugador1[i]=='9 ' + chr(5) or poker2.cartas_jugador1[i]=='9 ' + chr(6):
            puntostotales=puntostotales+8
        if poker2.cartas_jugador1[i]=='10 ' + chr(3) or poker2.cartas_jugador1[i]=='10 ' + chr(4) or poker2.cartas_jugador1[i]=='10 ' + chr(5) or poker2.cartas_jugador1[i]=='10 ' + chr(6):
            puntostotales=puntostotales+9
        if poker2.cartas_jugador1[i]=='J ' + chr(3) or poker2.cartas_jugador1[i]=='J ' + chr(4) or poker2.cartas_jugador1[i]=='J ' + chr(5) or poker2.cartas_jugador1[i]=='J ' + chr(6):
            puntostotales=puntostotales+10
        if poker2.cartas_jugador1[i]=='Q ' + chr(3) or poker2.cartas_jugador1[i]=='Q ' + chr(4) or poker2.cartas_jugador1[i]=='Q ' + chr(5) or poker2.cartas_jugador1[i]=='Q ' + chr(6):
            puntostotales=puntostotales+11
        if poker2.cartas_jugador1[i]=='K ' + chr(3) or poker2.cartas_jugador1[i]=='K ' + chr(4) or poker2.cartas_jugador1[i]=='K ' + chr(5) or poker2.cartas_jugador1[i]=='K ' + chr(6):
            puntostotales=puntostotales+12
        if poker2.cartas_jugador1[i]=='A ' + chr(3) or poker2.cartas_jugador1[i]=='A ' + chr(4) or poker2.cartas_jugador1[i]=='A ' + chr(5) or poker2.cartas_jugador1[i]=='A ' + chr(6):
            puntostotales=puntostotales+13

def puntosbot(cartasrepartidas):
    global puntostotalesbot
    for i in range(cartasrepartidas):
        if bot.cartasbot[i]=='2 ' + chr(3) or bot.cartasbot[i]=='2 ' + chr(4) or bot.cartasbot[i]=='2 ' + chr(5) or bot.cartasbot[i]=='2 ' + chr(6):
            puntostotalesbot=puntostotalesbot+1
        if bot.cartasbot[i]=='3 ' + chr(3) or bot.cartasbot[i]=='3 ' + chr(4) or bot.cartasbot[i]=='3 ' + chr(5) or bot.cartasbot[i]=='3 ' + chr(6):
            puntostotalesbot=puntostotalesbot+2
        if bot.cartasbot[i]=='4 ' + chr(3) or bot.cartasbot[i]=='4 ' + chr(4) or bot.cartasbot[i]=='4 ' + chr(5) or bot.cartasbot[i]=='4 ' + chr(6):
            puntostotalesbot=puntostotalesbot+3
        if bot.cartasbot[i]=='5 ' + chr(3) or bot.cartasbot[i]=='5 ' + chr(4) or bot.cartasbot[i]=='5 ' + chr(5) or bot.cartasbot[i]=='5 ' + chr(6):
            puntostotalesbot=puntostotalesbot+4
        if bot.cartasbot[i]=='6 ' + chr(3) or bot.cartasbot[i]=='6 ' + chr(4) or bot.cartasbot[i]=='6 ' + chr(5) or bot.cartasbot[i]=='6 ' + chr(6):
            puntostotalesbot=puntostotalesbot+5
        if bot.cartasbot[i]=='7 ' + chr(3) or bot.cartasbot[i]=='7 ' + chr(4) or bot.cartasbot[i]=='7 ' + chr(5) or bot.cartasbot[i]=='7 ' + chr(6):
            puntostotalesbot=puntostotalesbot+6
        if bot.cartasbot[i]=='8 ' + chr(3) or bot.cartasbot[i]=='8 ' + chr(4) or bot.cartasbot[i]=='8 ' + chr(5) or bot.cartasbot[i]=='8 ' + chr(6):
            puntostotalesbot=puntostotalesbot+7
        if bot.cartasbot[i]=='9 ' + chr(3) or bot.cartasbot[i]=='9 ' + chr(4) or bot.cartasbot[i]=='9 ' + chr(5) or bot.cartasbot[i]=='9 ' + chr(6):
            puntostotalesbot=puntostotalesbot+8
        if bot.cartasbot[i]=='10 ' + chr(3) or bot.cartasbot[i]=='10 ' + chr(4) or bot.cartasbot[i]=='10 ' + chr(5) or bot.cartasbot[i]=='10 ' + chr(6):
            puntostotalesbot=puntostotalesbot+9
        if bot.cartasbot[i]=='J ' + chr(3) or bot.cartasbot[i]=='J ' + chr(4) or bot.cartasbot[i]=='J ' + chr(5) or bot.cartasbot[i]=='J ' + chr(6):
            puntostotalesbot=puntostotalesbot+10
        if bot.cartasbot[i]=='Q ' + chr(3) or bot.cartasbot[i]=='Q ' + chr(4) or bot.cartasbot[i]=='Q ' + chr(5) or bot.cartasbot[i]=='Q ' + chr(6):
            puntostotalesbot=puntostotalesbot+11
        if bot.cartasbot[i]=='K ' + chr(3) or bot.cartasbot[i]=='K ' + chr(4) or bot.cartasbot[i]=='K ' + chr(5) or bot.cartasbot[i]=='K ' + chr(6):
            puntostotalesbot=puntostotalesbot+12
        if bot.cartasbot[i]=='A ' + chr(3) or bot.cartasbot[i]=='A ' + chr(4) or bot.cartasbot[i]=='A ' + chr(5) or bot.cartasbot[i]=='A ' + chr(6):
            puntostotalesbot=puntostotalesbot+13


def comparacion():
    if puntostotales>puntostotalesbot:
        print("Tienes mejores cartas, Has ganado", "Tu tenias:", puntostotales, "Y el bot tenia:", puntostotalesbot)
    else:
        print("El bot tiene mejores cartas que tu, Has perdido","Tu tenias:", puntostotales, "Y el bot tenia:", puntostotalesbot)
    
import poker2
import bot

corazonesjugador  = 0; diamantesjugador  = 0; treborjugador  = 0;   picasjugador = 0
corazonesbot       =0; diamantesbot      = 0; treborbot      = 0;   picasbot     = 0
def  puntosjugador(cartasrepartidas):
    global corazonesjugador; global diamantesjugador; global treborjugador; global picasjugador
    for i in range(cartasrepartidas):
        if poker2.cartas_jugador1[i] == '2 '   + chr(3) or poker2.cartas_jugador1[i]=='3 ' + chr(3) or poker2.cartas_jugador1[i]=='4 ' + chr(3) or poker2.cartas_jugador1[i]=='5 ' + chr(3)  or poker2.cartas_jugador1[i]=='6 ' + chr(3) or poker2.cartas_jugador1[i]=='7 ' + chr(3) or poker2.cartas_jugador1[i]=='8 ' + chr(3) or poker2.cartas_jugador1[i]=='9 ' + chr(3) or poker2.cartas_jugador1[i]=='10 ' + chr(3) or poker2.cartas_jugador1[i]=='J ' + chr(3) or poker2.cartas_jugador1[i]=='Q ' + chr(3) or poker2.cartas_jugador1[i]=='K ' + chr(3) or poker2.cartas_jugador1[i]=='A ' + chr(3):
            corazonesjugador+=1
        elif poker2.cartas_jugador1[i]=='2 '   + chr(4) or poker2.cartas_jugador1[i]=='3 ' + chr(4) or poker2.cartas_jugador1[i]=='4 ' + chr(4) or poker2.cartas_jugador1[i]=='5 ' + chr(4)  or poker2.cartas_jugador1[i]=='6 ' + chr(4) or poker2.cartas_jugador1[i]=='7 ' + chr(4) or poker2.cartas_jugador1[i]=='8 ' + chr(4) or poker2.cartas_jugador1[i]=='9 ' + chr(4) or poker2.cartas_jugador1[i]=='10 ' + chr(4) or poker2.cartas_jugador1[i]=='J ' + chr(4) or poker2.cartas_jugador1[i]=='Q ' + chr(4) or poker2.cartas_jugador1[i]=='K ' + chr(4) or poker2.cartas_jugador1[i]=='A ' + chr(4):
            diamantesjugador+=1
        elif poker2.cartas_jugador1[i]=='2 '   + chr(5) or poker2.cartas_jugador1[i]=='3 ' + chr(5) or poker2.cartas_jugador1[i]=='4 ' + chr(5) or poker2.cartas_jugador1[i]=='5 ' + chr(5)  or poker2.cartas_jugador1[i]=='6 ' + chr(5) or poker2.cartas_jugador1[i]=='7 ' + chr(5) or poker2.cartas_jugador1[i]=='8 ' + chr(5) or poker2.cartas_jugador1[i]=='9 ' + chr(5) or poker2.cartas_jugador1[i]=='10 ' + chr(5) or poker2.cartas_jugador1[i]=='J ' + chr(5) or poker2.cartas_jugador1[i]=='Q ' + chr(5) or poker2.cartas_jugador1[i]=='K ' + chr(5) or poker2.cartas_jugador1[i]=='A ' + chr(5):
            treborjugador+=1
        elif poker2.cartas_jugador1[i]=='2 '   + chr(6) or poker2.cartas_jugador1[i]=='3 ' + chr(6) or poker2.cartas_jugador1[i]=='4 ' + chr(6) or poker2.cartas_jugador1[i]=='5 ' + chr(6)  or poker2.cartas_jugador1[i]=='6 ' + chr(6) or poker2.cartas_jugador1[i]=='7 ' + chr(6) or poker2.cartas_jugador1[i]=='8 ' + chr(6) or poker2.cartas_jugador1[i]=='9 ' + chr(6) or poker2.cartas_jugador1[i]=='10 ' + chr(6) or poker2.cartas_jugador1[i]=='J ' + chr(6) or poker2.cartas_jugador1[i]=='Q ' + chr(6) or poker2.cartas_jugador1[i]=='K ' + chr(6) or poker2.cartas_jugador1[i]=='A ' + chr(6):
            picasjugador+=1


def puntosbot(cartasrepartidas):
    global corazonesbot; global diamantesbot; global treborbot; global picasbot
    for i in range(cartasrepartidas):
        if bot.cartasbot[i] == '2 '   + chr(3) or bot.cartasbot[i]=='3 ' + chr(3) or bot.cartasbot[i]=='4 ' + chr(3) or bot.cartasbot[i]=='5 ' + chr(3)  or bot.cartasbot[i]=='6 ' + chr(3) or bot.cartasbot[i]=='7 ' + chr(3) or bot.cartasbot[i]=='8 ' + chr(3) or bot.cartasbot[i]=='9 ' + chr(3) or bot.cartasbot[i]=='10 ' + chr(3) or bot.cartasbot[i]=='J ' + chr(3) or bot.cartasbot[i]=='Q ' + chr(3) or bot.cartasbot[i]=='K ' + chr(3) or bot.cartasbot[i]=='A ' + chr(3):
            corazonesbot+=1
        elif bot.cartasbot[i]=='2 '   + chr(4) or bot.cartasbot[i]=='3 ' + chr(4) or bot.cartasbot[i]=='4 ' + chr(4) or bot.cartasbot[i]=='5 ' + chr(4)  or bot.cartasbot[i]=='6 ' + chr(4) or bot.cartasbot[i]=='7 ' + chr(4) or bot.cartasbot[i]=='8 ' + chr(4) or bot.cartasbot[i]=='9 ' + chr(4) or bot.cartasbot[i]=='10 ' + chr(4) or bot.cartasbot[i]=='J ' + chr(4) or bot.cartasbot[i]=='Q ' + chr(4) or bot.cartasbot[i]=='K ' + chr(4) or bot.cartasbot[i]=='A ' + chr(4):
            diamantesbot+=1
        elif bot.cartasbot[i]=='2 '   + chr(5) or bot.cartasbot[i]=='3 ' + chr(5) or bot.cartasbot[i]=='4 ' + chr(5) or bot.cartasbot[i]=='5 ' + chr(5)  or bot.cartasbot[i]=='6 ' + chr(5) or bot.cartasbot[i]=='7 ' + chr(5) or bot.cartasbot[i]=='8 ' + chr(5) or bot.cartasbot[i]=='9 ' + chr(5) or bot.cartasbot[i]=='10 ' + chr(5) or bot.cartasbot[i]=='J ' + chr(5) or bot.cartasbot[i]=='Q ' + chr(5) or bot.cartasbot[i]=='K ' + chr(5) or bot.cartasbot[i]=='A ' + chr(5):
            treborbot+=1
        elif bot.cartasbot[i]=='2 '   + chr(6) or bot.cartasbot[i]=='3 ' + chr(6) or bot.cartasbot[i]=='4 ' + chr(6) or bot.cartasbot[i]=='5 ' + chr(6)  or bot.cartasbot[i]=='6 ' + chr(6) or bot.cartasbot[i]=='7 ' + chr(6) or bot.cartasbot[i]=='8 ' + chr(6) or bot.cartasbot[i]=='9 ' + chr(6) or bot.cartasbot[i]=='10 ' + chr(6) or bot.cartasbot[i]=='J ' + chr(6) or bot.cartasbot[i]=='Q ' + chr(6) or bot.cartasbot[i]=='K ' + chr(6) or bot.cartasbot[i]=='A ' + chr(6):
            picasbot+=1



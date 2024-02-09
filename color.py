import poker2
import bot

#Funcion para juntar el color de las cartas en una variable por color del jugador
def  puntosjugador(cartasrepartidas):
    global corazones; global diamantes; global trebor; global picas
    corazones  = 0; diamantes  = 0; trebor  = 0;   picas = 0
    for i in range(cartasrepartidas):
        if poker2.cartas_jugador1[i] == '2 '   + chr(3) or poker2.cartas_jugador1[i]=='3 ' + chr(3) or poker2.cartas_jugador1[i]=='4 ' + chr(3) or poker2.cartas_jugador1[i]=='5 ' + chr(3)  or poker2.cartas_jugador1[i]=='6 ' + chr(3) or poker2.cartas_jugador1[i]=='7 ' + chr(3) or poker2.cartas_jugador1[i]=='8 ' + chr(3) or poker2.cartas_jugador1[i]=='9 ' + chr(3) or poker2.cartas_jugador1[i]=='10 ' + chr(3) or poker2.cartas_jugador1[i]=='J ' + chr(3) or poker2.cartas_jugador1[i]=='Q ' + chr(3) or poker2.cartas_jugador1[i]=='K ' + chr(3) or poker2.cartas_jugador1[i]=='A ' + chr(3):
            corazones+=1
        elif poker2.cartas_jugador1[i]=='2 '   + chr(4) or poker2.cartas_jugador1[i]=='3 ' + chr(4) or poker2.cartas_jugador1[i]=='4 ' + chr(4) or poker2.cartas_jugador1[i]=='5 ' + chr(4)  or poker2.cartas_jugador1[i]=='6 ' + chr(4) or poker2.cartas_jugador1[i]=='7 ' + chr(4) or poker2.cartas_jugador1[i]=='8 ' + chr(4) or poker2.cartas_jugador1[i]=='9 ' + chr(4) or poker2.cartas_jugador1[i]=='10 ' + chr(4) or poker2.cartas_jugador1[i]=='J ' + chr(4) or poker2.cartas_jugador1[i]=='Q ' + chr(4) or poker2.cartas_jugador1[i]=='K ' + chr(4) or poker2.cartas_jugador1[i]=='A ' + chr(4):
            diamantes+=1
        elif poker2.cartas_jugador1[i]=='2 '   + chr(5) or poker2.cartas_jugador1[i]=='3 ' + chr(5) or poker2.cartas_jugador1[i]=='4 ' + chr(5) or poker2.cartas_jugador1[i]=='5 ' + chr(5)  or poker2.cartas_jugador1[i]=='6 ' + chr(5) or poker2.cartas_jugador1[i]=='7 ' + chr(5) or poker2.cartas_jugador1[i]=='8 ' + chr(5) or poker2.cartas_jugador1[i]=='9 ' + chr(5) or poker2.cartas_jugador1[i]=='10 ' + chr(5) or poker2.cartas_jugador1[i]=='J ' + chr(5) or poker2.cartas_jugador1[i]=='Q ' + chr(5) or poker2.cartas_jugador1[i]=='K ' + chr(5) or poker2.cartas_jugador1[i]=='A ' + chr(5):
            trebor+=1
        elif poker2.cartas_jugador1[i]=='2 '   + chr(6) or poker2.cartas_jugador1[i]=='3 ' + chr(6) or poker2.cartas_jugador1[i]=='4 ' + chr(6) or poker2.cartas_jugador1[i]=='5 ' + chr(6)  or poker2.cartas_jugador1[i]=='6 ' + chr(6) or poker2.cartas_jugador1[i]=='7 ' + chr(6) or poker2.cartas_jugador1[i]=='8 ' + chr(6) or poker2.cartas_jugador1[i]=='9 ' + chr(6) or poker2.cartas_jugador1[i]=='10 ' + chr(6) or poker2.cartas_jugador1[i]=='J ' + chr(6) or poker2.cartas_jugador1[i]=='Q ' + chr(6) or poker2.cartas_jugador1[i]=='K ' + chr(6) or poker2.cartas_jugador1[i]=='A ' + chr(6):
            picas+=1

#Funcion para juntar el color de las cartas en una variable por color del bot
def puntosbot(cartasrepartidas):
    global corazones; global diamantes; global trebor; global picas
    corazones=0; diamantes=0; trebor=0; picas=0
    for i in range(cartasrepartidas):
        if bot.cartasbot[i] == '2 '   + chr(3) or bot.cartasbot[i]=='3 ' + chr(3) or bot.cartasbot[i]=='4 ' + chr(3) or bot.cartasbot[i]=='5 ' + chr(3)  or bot.cartasbot[i]=='6 ' + chr(3) or bot.cartasbot[i]=='7 ' + chr(3) or bot.cartasbot[i]=='8 ' + chr(3) or bot.cartasbot[i]=='9 ' + chr(3) or bot.cartasbot[i]=='10 ' + chr(3) or bot.cartasbot[i]=='J ' + chr(3) or bot.cartasbot[i]=='Q ' + chr(3) or bot.cartasbot[i]=='K ' + chr(3) or bot.cartasbot[i]=='A ' + chr(3):
            corazones+=1
        elif bot.cartasbot[i]=='2 '   + chr(4) or bot.cartasbot[i]=='3 ' + chr(4) or bot.cartasbot[i]=='4 ' + chr(4) or bot.cartasbot[i]=='5 ' + chr(4)  or bot.cartasbot[i]=='6 ' + chr(4) or bot.cartasbot[i]=='7 ' + chr(4) or bot.cartasbot[i]=='8 ' + chr(4) or bot.cartasbot[i]=='9 ' + chr(4) or bot.cartasbot[i]=='10 ' + chr(4) or bot.cartasbot[i]=='J ' + chr(4) or bot.cartasbot[i]=='Q ' + chr(4) or bot.cartasbot[i]=='K ' + chr(4) or bot.cartasbot[i]=='A ' + chr(4):
            diamantes+=1
        elif bot.cartasbot[i]=='2 '   + chr(5) or bot.cartasbot[i]=='3 ' + chr(5) or bot.cartasbot[i]=='4 ' + chr(5) or bot.cartasbot[i]=='5 ' + chr(5)  or bot.cartasbot[i]=='6 ' + chr(5) or bot.cartasbot[i]=='7 ' + chr(5) or bot.cartasbot[i]=='8 ' + chr(5) or bot.cartasbot[i]=='9 ' + chr(5) or bot.cartasbot[i]=='10 ' + chr(5) or bot.cartasbot[i]=='J ' + chr(5) or bot.cartasbot[i]=='Q ' + chr(5) or bot.cartasbot[i]=='K ' + chr(5) or bot.cartasbot[i]=='A ' + chr(5):
            trebor+=1
        elif bot.cartasbot[i]=='2 '   + chr(6) or bot.cartasbot[i]=='3 ' + chr(6) or bot.cartasbot[i]=='4 ' + chr(6) or bot.cartasbot[i]=='5 ' + chr(6)  or bot.cartasbot[i]=='6 ' + chr(6) or bot.cartasbot[i]=='7 ' + chr(6) or bot.cartasbot[i]=='8 ' + chr(6) or bot.cartasbot[i]=='9 ' + chr(6) or bot.cartasbot[i]=='10 ' + chr(6) or bot.cartasbot[i]=='J ' + chr(6) or bot.cartasbot[i]=='Q ' + chr(6) or bot.cartasbot[i]=='K ' + chr(6) or bot.cartasbot[i]=='A ' + chr(6):
            picas+=1
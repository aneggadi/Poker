import time
import poker2
import bot
import puntuacion
import color
import comparacion

#programa principal
def juego():
    poker2.credito()
    print("Tu credito actual es:", poker2.max_credito)
    print("Tu mano:")
    print("  ")
    poker2.repartir(2)
    print("  ")
    bot.repartir(2)
    poker2.ciega()
    print("El flop es:")
    poker2.flop(3)
    print("  ")
    print("Tus cartas con el flop es:")
    print(" ".join(poker2.cartas_jugador1))
    time.sleep(1)
    puntuacion.numjugador(len(poker2.cartas_jugador1))
    color.puntosjugador(len(poker2.cartas_jugador1))
    comparacion.escaleracolor()
    print(puntuacion.ass)
    valorcartasjugador=comparacion.valorcartas
    puntuacion.numbot(len(bot.cartasbot))
    color.puntosbot(len(bot.cartasbot))
    comparacion.escaleracolor()
    print("Tu puntuacion actual es:", valorcartasjugador)
    time.sleep(1)
    poker2.pregunta()
    if valorcartasjugador>comparacion.valorcartas:
        ganador=poker2.max_credito+poker2.bote
        print("has ganado al bot enohrabuena!!!. Te has llevado:", ganador)
    elif valorcartasjugador==comparacion.valorcartas:
        empate=poker2.bote/2
        print("Habeis quedado empate tu y el bot os vamos a repartir el bote, te has llevado:", empate)
    else:
        print("Menudo pirngado te ha ganado un bot, se ha llevado el bot:", poker2.bote)
    
    jugardenuevo=input("Quieres volver a jugar o terminar (jugar/terminar)")
    if jugardenuevo=="jugar":
        juego()
    if jugardenuevo=="terminar":
        exit()

juego()
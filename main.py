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
    puntuacion.numjugador(len(poker2.cartas_jugador1))
    puntuacion.numbot(len(bot.cartasbot))
    print("  ")
    print("Tus cartas con el flop es:")
    print(" ".join(poker2.cartas_jugador1))
    time.sleep(1)
    puntuacion.numjugador(5)
    color.puntosjugador(5)
    print(puntuacion.dos, puntuacion.tres, puntuacion.cuatro, puntuacion.cinco, 
            puntuacion.seis, puntuacion.siete, puntuacion.ocho, puntuacion.nueve,
            puntuacion.diez, puntuacion.jota, puntuacion.reina, puntuacion.rey, 
            puntuacion.rey, puntuacion.ass)
    print(color.corazonesjugador, color.diamantesjugador, color.picasbot, color.treborjugador)
    comparacion.escaleracolor()
    print("tu puntuacion actual es:", comparacion.valorcartasjugador)
    time.sleep(1)
    poker2.pregunta()
    poker2.botap(poker2.max_creditbot)
    jugardenuevo=input("Quieres volver a jugar o terminar (jugar/terminar)")
    if jugardenuevo=="jugar":
        juego()
    if jugardenuevo=="terminar":
        exit()

juego()
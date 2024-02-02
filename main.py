import time
import poker2
import bot
import puntuacion

def juego():
    print("Tu credito actual es:", poker2.max_credito)
    print("Tu mano:")
    print("  ")
    poker2.repartir(2)
    print("  ")
    bot.repartir(2)
    poker2.ciega()
    print("El flop es:")
    poker2.flop(3)
    puntuacion.puntosjugador(5)
    puntuacion.puntosbot(5)
    print("  ")
    print("Tus cartas con el flop es:")
    print(" ".join(poker2.cartas_jugador1))
    time.sleep(1)
    print("tu puntuacion actual es:" , puntuacion.puntostotales)
    time.sleep(1)
    poker2.pregunta()
    poker2.botap(poker2.max_credito)
    puntuacion.comparacion()
    jugardenuevo=input("Quieres volver a jugar o terminar (jugar/terminar)")
    if jugardenuevo=="jugar":
        juego()
    if jugardenuevo=="terminar":
        exit()

juego()
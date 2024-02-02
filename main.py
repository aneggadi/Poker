import poker2
import bot

print("Tu mano:") 
poker2.repartir(2)
print("  ")
print("Cartas del bot:")
bot.repartir(2)
print(poker2.apostar(), "Tu credito actual es:", poker2.max_credito)
print("El flop es:")
poker2.flop(3)
print("Tus cartas con el flop es:")
print(" ".join(poker2.cartas_jugador1))
print("Las cortas del bot con el flop es:")
print(" ".join(bot.cartasbot))
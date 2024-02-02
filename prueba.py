from itertools import combinations
def baraja(numero_barajas, numero_cartas):
# Definir los palos y los valores de las cartas
    palos = [chr(3), chr(4), chr(5), chr(6)]
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Crear una baraja completa
    baraja = [(valor, palo) for valor in valores for palo in palos]

# Generar todas las combinaciones posibles de 5 cartas (mano de poker)
    combinaciones_poker = list(combinations(baraja, numero_cartas))

# Imprimir las primeras 5 combinaciones como ejemplo
    for i in range(numero_barajas):
        print(f"Combinación {i + 1}: {combinaciones_poker[i]}")

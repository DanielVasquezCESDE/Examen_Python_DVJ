"""
Escriba un programa que muestre una partida de dados entre dos jugadores, se debe
ingresar la cantidad de turnos que se van a jugar, cada jugador tira un dado. Si un jugador
saca un valor mayor que el otro, gana los puntos de ambos dados. Si los dos jugadores
sacan el mismo valor, ninguno recibe puntos. Si en el ultimo turno hay un empate, esos
puntos se pierden y termina la partida. Debe mostrar quien gana la partida, quien gana
cada turno y la puntuación acumulada por cada jugador.
Para el examen pueden usar la librería random (import random) y utilizar el método
random.randint(desde, hasta) que toma números enteros de forma aleatorias según rango
dado.
"""
import random

jugadores = []

print("\n--------------🎲¡JUEGO DE DADOS!🎲--------------\n")

jugadores.append(input(f"Ingrese el nombre de jugador Nr. 1:\n"))
jugadores.append(input(f"Ingrese el nombre de jugador Nr. 2:\n"))

cant_turno = int(input(f"Ingrese los turnos a jugar:\n"))

puntos_jug_1 = 0
puntos_jug_2 = 0
#if cant_turno == max(cant_turno):
#    if dado_valor[0] == dado_valor[1]

for i in range(cant_turno):
    dado_valor = []

    print(f"\n--- Turno Nro. {i+1}---\n")

    dado_valor.append(random.randint(1, 6))
    dado_valor.append(random.randint(1, 6))

    print(f"{jugadores[0]} tiró {dado_valor[0]}")
    print(f"{jugadores[1]} tiró {dado_valor[1]}")

    if dado_valor[0] > dado_valor[1]:
        puntos_jug_1 += dado_valor[0]
        puntos_jug_2 += 0
        print(f"¡El jugador {jugadores[0]}, ganó el turno!\n {jugadores[0]} lleva {puntos_jug_1} puntos.\n{jugadores[1]} lleva {puntos_jug_2} puntos.\n ")

    elif dado_valor[0] == dado_valor[1]:
        puntos_jug_1 += 0
        puntos_jug_2 += 0
        print(f"¡Ninguno gana puntos!\n {jugadores[0]} lleva {puntos_jug_1} puntos.\n{jugadores[1]} lleva {puntos_jug_2} puntos.\n ")

    elif dado_valor[0] < dado_valor[1]:
        puntos_jug_2 += dado_valor[1]
        puntos_jug_1 += 0
        print(f"¡El jugador {jugadores[1]}, ganó el turno!\n {jugadores[0]} lleva {puntos_jug_1} puntos.\n{jugadores[1]} lleva {puntos_jug_2} puntos.\n ")


if puntos_jug_1 > puntos_jug_2:
    print(f"👌¡El jugador {jugadores[0]}, ganó la partida con {puntos_jug_1} puntos!👌\n")
elif puntos_jug_1 < puntos_jug_2:
    print(f"👌¡El jugador {jugadores[1]}, ganó la partida con {puntos_jug_2} puntos!👌\n")
elif puntos_jug_1 == puntos_jug_2:
    print(f"😐¡EM-PA-TE, ambos con {puntos_jug_1} puntos!😐\n")
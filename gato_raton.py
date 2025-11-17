import random

def imprimir_tablero(posicion_gato, posicion_raton, posiciones_obstaculos, tamaño):
    for fila in range(tamaño):
        for columna in range(tamaño):
            posicion_actual = (fila, columna)
            if posicion_actual == posicion_gato:
                print("😼", end=" ")
            elif posicion_actual == posicion_raton:
                print("🐭", end=" ")
            elif posicion_actual in posiciones_obstaculos:
                print("🧱", end=" ")
            else:
                print("⬜", end=" ")
        print()
    print()
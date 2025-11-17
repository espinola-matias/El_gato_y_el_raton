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

def obtener_movimientos_validos(posicion_actual, posiciones_obstaculos, tamaño):
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    fila, columna = posicion_actual
    movimientos_validos = []
    
    for direccion in direcciones:
        nueva_fila = fila + direccion[0]
        nueva_columna = columna + direccion[1]
        
        if 0 <= nueva_fila < tamaño and 0 <= nueva_columna < tamaño:
            if (nueva_fila, nueva_columna) not in posiciones_obstaculos: 
                movimientos_validos.append((nueva_fila, nueva_columna))
                
    return movimientos_validos

def distancia_jugadores(posicion_gato, posicion_raton):
    return abs(posicion_gato[0] - posicion_raton[0]) + abs(posicion_gato[1] - posicion_raton[1])

def evaluar_condiciones(posicion_gato, posicion_raton):
    if posicion_gato == posicion_raton:
        return -1000
    return distancia_jugadores(posicion_gato, posicion_raton)
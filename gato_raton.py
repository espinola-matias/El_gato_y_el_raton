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

def minimax(posicion_gato, posicion_raton, posiciones_obstaculos, profundidad, turno_raton, tamaño):
    if profundidad == 0 or posicion_gato == posicion_raton:
        return evaluar_condiciones(posicion_gato, posicion_raton)

    if turno_raton:
        mejor_valor = -float("inf")
        for movimiento_raton in obtener_movimientos_validos(posicion_raton, posiciones_obstaculos, tamaño): 
            valor = minimax(posicion_gato, movimiento_raton, posiciones_obstaculos, profundidad - 1, False, tamaño)
            mejor_valor = max(mejor_valor, valor)
        return mejor_valor
    else:
        mejor_valor = float("inf")
        for movimiento_gato in obtener_movimientos_validos(posicion_gato, posiciones_obstaculos, tamaño): 
            valor = minimax(movimiento_gato, posicion_raton, posiciones_obstaculos, profundidad - 1, True, tamaño)
            mejor_valor = min(mejor_valor, valor)
        return mejor_valor

def raton_minimax(posicion_gato, posicion_raton, posiciones_obstaculos, tamaño):
    mejor_valor = -float("inf")
    mejor_movimiento = posicion_raton
    for movimiento_raton in obtener_movimientos_validos(posicion_raton, posiciones_obstaculos, tamaño):
        valor = minimax(posicion_gato, movimiento_raton, posiciones_obstaculos, 5, False, tamaño)
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_movimiento = movimiento_raton
    return mejor_movimiento 

def gato_minimax(posicion_gato, posicion_raton, posiciones_obstaculos, tamaño):
    mejor_valor = float("inf")
    mejor_movimiento = posicion_gato
    for movimiento_gato in obtener_movimientos_validos(posicion_gato, posiciones_obstaculos, tamaño):
        valor = minimax(movimiento_gato, posicion_raton, posiciones_obstaculos, 5, True, tamaño)
        if valor < mejor_valor:
            mejor_valor = valor
            mejor_movimiento = movimiento_gato
    return mejor_movimiento

def mover_raton(posicion_actual, posiciones_obstaculos, tamaño):
    mapa_movimientos = {
        'w': (-1, 0),  
        's': (1, 0),   
        'a': (0, -1), 
        'd': (0, 1)}
    fila_actual, columna_actual = posicion_actual
    
    movimientos_validos = obtener_movimientos_validos(posicion_actual, posiciones_obstaculos, tamaño)
    if not movimientos_validos:
        print("¡ATRAPADO! No hay movimientos disponibles")
        return posicion_actual
    
    while True:
        entrada = input(f"Tu turno ({posicion_actual}) Mueve Raton ('W' (ARRIBA)/'A' (IZQUIERDA)/'S'(ABAJO)/'D' (DERECHA)): ").strip().lower()
        
        if entrada not in mapa_movimientos:
            print("Entrada invaida, Usa solo W, A, S o D")
            continue
            
        fila, columna = mapa_movimientos[entrada]
        nueva_fila = fila_actual + fila
        nueva_columna = columna_actual + columna
        nueva_posicion = (nueva_fila, nueva_columna)
        
        if nueva_posicion in movimientos_validos:
            return nueva_posicion
        else:
            print("Movimiento invalido, Casilla ocupada o fuera de limites")

def inicio_juego():
    limite_movimientos = 10
    porcentaje_obstaculos = 0.10 
    print("¡Bienvenido al juego del Gato y Raton!")
    tamaño = int(input("Dime el tamaño del tablero que deseas (ej. 10): "))
    num_casillas = tamaño * tamaño
    num_obstaculos = int(num_casillas * porcentaje_obstaculos)

    print("\n--- Modo de Juego ---")
    print("1. Simulación (Gato IA vs Raton IA)")
    print("2. Jugar (Gato IA vs Raton Humano)")

    while True:
        modo = input("Elige el modo (1 o 2): ").strip()
        if modo in ['1', '2']:
            modo_simulacion = (modo == '1')
            break
        print("Opcion no valida. Por favor, elige 1 o 2")
    
    posicion_gato = (tamaño - 1, tamaño - 1)
    posicion_raton = (0, 0)
    
    posiciones_ocupadas = {posicion_gato, posicion_raton}
    posiciones_obstaculos = set()

    while len(posiciones_obstaculos) < num_obstaculos:
        fila_aleatoria = random.randint(0, tamaño - 1)
        columna_aleatoria = random.randint(0, tamaño - 1)
        nueva_posicion = (fila_aleatoria, columna_aleatoria)
        
        if nueva_posicion not in posiciones_ocupadas:
            posiciones_obstaculos.add(nueva_posicion)
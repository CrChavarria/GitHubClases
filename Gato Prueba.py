def imprimir_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-----")

def verificar_ganador(tablero, jugador):
    # Verificar filas
    for fila in tablero:
        if all(casilla == jugador for casilla in fila):
            return True

    # Verificar columnas
    for col in range(3):
        if all(tablero[fila][col] == jugador for fila in range(3)):
            return True

    # Verificar diagonales
    if (tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador) or \
       (tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador):
        return True

    return False

def jugar_gato():
    tablero = [[' ' for _ in range(3)] for _ in range(3)]
    jugadores = ['X', 'O']
    jugador_actual = 0
    turno = 1

    while turno <= 9:
        imprimir_tablero(tablero)
        print("Turno", turno)
        jugador = jugadores[jugador_actual]
        fila = int(input("Ingresa la fila (0, 1, 2): "))
        col = int(input("Ingresa la columna (0, 1, 2): "))

        if tablero[fila][col] == ' ':
            tablero[fila][col] = jugador
            if verificar_ganador(tablero, jugador):
                imprimir_tablero(tablero)
                print("¡El jugador", jugador, "ha ganado!")
                return

            jugador_actual = (jugador_actual + 1) % 2
            turno += 1
        else:
            print("Casilla ocupada. Intenta nuevamente.")

    imprimir_tablero(tablero)
    print("¡Es un empate!")

jugar_gato()

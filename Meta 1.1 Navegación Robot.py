# Flores Cisneros Adrian Alejandro
# 951
# Se realizó el 23/08/2026
# Ejercicio 3: Navegación en un Almacén
#La función verificar_recogida_productos simula el recorrido de un robot sobre una cuadrícula (o sea una matriz) siguiendo una secuencia
# de movimientos (R = derecha, L= izquierda, D= abajo, U=arriba). En cada paso valida que no se salga del almacén ni choque con un obstáculo,
# y va registrando qué productos recoge. Al final devuelve True solo si recogió todos los productos y regresó al punto de inicio


MOVIMIENTOS= { 'R': (0,1),
               'L': (0,-1),
               'D': (1,0),
               'U': (-1,0),}

def verificar_recoleccion_objeto(almacen,movimientos):
    filas= len(almacen)
    columnas= len(almacen[0]) if filas > 0 else 0

    objetos_totales= set()
    for f in range(filas):
        for c in range(columnas):
            if almacen[f][c] == 'P':
                objetos_totales.add((f,c))

    fila, columna =0,0
    objetos_recogidos= set()
    if (fila,columna) in objetos_totales:
        objetos_recogidos.add((fila,columna))

    for movimiento in movimientos:
        if movimiento not in MOVIMIENTOS:
            return False

        delta_fila, delta_columna = MOVIMIENTOS[movimiento]
        nueva_fila = fila + delta_fila
        nueva_columna = columna + delta_columna

        # El robot no puede salirse del almacén
        if not (0 <= nueva_fila < filas and 0 <= nueva_columna < columnas):
            return False

        # El robot no puede pasar por un obstáculo
        if almacen[nueva_fila][nueva_columna] == '#':
            return False

        fila, columna = nueva_fila, nueva_columna

        if (fila, columna) in objetos_totales:
            objetos_recogidos.add((fila, columna))

    volvio_al_inicio = (fila, columna) == (0, 0)
    recogio_todos_los_objetos= objetos_recogidos == objetos_totales

    return volvio_al_inicio and recogio_todos_los_objetos


if __name__ == "__main__":
    almacen= [
        ['.', '.', '#', 'P'],
        ['.', '#', '.', '.'],
        ['P', '.', 'P', '.'],
        ['#', '.', '#', '.'],
    ]
    print("-----------------------")
    movimientos_correctos =['D', 'D', 'R', 'R', 'U', 'R', 'U', 'D', 'L', 'D', 'L', 'L', 'U', 'U']
    print(verificar_recoleccion_objeto(almacen, movimientos_correctos))
    print("El robot no tuvo complicaciones, correcto :D")

    # Ejemplo donde el robot choca con un obstáculo
    print("-----------------------")
    movimientos_con_obstaculo =['D', 'D', 'D']
    print(verificar_recoleccion_objeto(almacen, movimientos_con_obstaculo))
    print("El Robot choco contra un obstaculo, perdiste :c")

    # Ejemplo donde no se recogen todos los productos ni se vuelve al inicio
    print("-----------------------")
    movimientos_incompletos= ['D', 'D']
    print(verificar_recoleccion_objeto(almacen, movimientos_incompletos))
    print("El Robot no recogio TODOS los objetos, perdiste :c")
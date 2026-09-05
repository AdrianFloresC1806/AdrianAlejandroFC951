# Flores Cisneros Adrian Alejandro
# 951
# Se realizó el 23/08/2026
# Simula el historial de cambios de una hoja de cálculo usando una lista
# como pila. Cada elemento del historial es una tupla (celda, valor) que
# representa el cambio que se registró en esa celda

def registrar_un_cambio (historial_cambios,celda,valor):
    historial_cambios.append((celda, valor))


def deshacer_cambio (historial_cambios):
    if historial_cambios:
        return historial_cambios.pop()

    print("No ha habido un cambio")
    return None


if __name__ == "__main__":
    historial_cambios = []
    registrar_un_cambio(historial_cambios,'a1',10)
    registrar_un_cambio(historial_cambios,'b2',20)

    print("-------------------")
    print("Historial de Cambios:")
    print(historial_cambios)
    print("-------------------")

    deshacer_cambio(historial_cambios)
    print("-------------------")
    print("Historial de Cambios despues de deshacer uno:")
    print(historial_cambios)
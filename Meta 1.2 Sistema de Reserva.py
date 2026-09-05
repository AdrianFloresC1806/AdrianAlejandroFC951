# Flores Cisneros Adrian Alejandro
# 951
# Se elaboró el 30/08/2026

#Este programa en Python simula un sistema de control de hotel (cuartos 1 al 9) mediante conjuntos (set). Cuenta con
# funciones principales para reservar, liberar y consultar la disponibilidad de los cuartos en tiempo real. Además,
# incluye validaciones para evitar errores como reservar habitaciones ocupadas o inexistentes, concluyendo con una
# serie de pruebas para comprobar el correcto funcionamiento de cada función.




habitaciones_dispo = {1,2,3,4,5,6,7,8,9}
habitaciones_reservadas = set ()


def reservar_habitaciones(numero_habitacion):
    if numero_habitacion in habitaciones_dispo:
        habitaciones_dispo.remove(numero_habitacion)
        habitaciones_reservadas.add(numero_habitacion)
        print(f"La habitación numero -{numero_habitacion}- se reservo")

    elif numero_habitacion in habitaciones_reservadas:
        print(f"La La habitación numero -{numero_habitacion}- ya esta reservada")

    else:
        print(f"La habitacion numero -{numero_habitacion}- no existe")

def liberar_habitaciones(numero_habitacion):
    if numero_habitacion in habitaciones_reservadas:
        habitaciones_reservadas.remove(numero_habitacion)
        habitaciones_dispo.add(numero_habitacion)
        print(f"La habitacion numero -{numero_habitacion}- se libero")
    elif numero_habitacion in habitaciones_dispo:
        print(f"La habitacion numero -{numero_habitacion}- no esta reservada")
    else:
        print(f"La habitacion numero -{numero_habitacion}- no existe")

def mostrar_habitaciones():
    if len(habitaciones_dispo) == 9:
        print("----------")
        print("Habitaciones disponibles del Hotel:")
        print(habitaciones_dispo)
        print("----------")
        print("Habitaciones reservadas del Hotel:")
        print(len(habitaciones_reservadas))
        print("----------")

    else:
        print("----------")
        print("Habitaciones disponibles del Hotel:")
        print(habitaciones_dispo)
        print("----------")
        print("Habitaciones reservadas del Hotel:")
        print(habitaciones_reservadas)
        print("----------")


if __name__ == '__main__':

    mostrar_habitaciones()


    print("Reservar Habitaciones")
    reservar_habitaciones(2)
    print("----------")
    reservar_habitaciones(3)


    print("----------")
    print("----------")
    print("----------")
    print("Estatus de Habitaciones")
    mostrar_habitaciones()
    print("----------")
    print("----------")


    print("Liberar una Habitación")
    print("----------")
    liberar_habitaciones(2)
    print("----------")
    print("----------")
    print("----------")


    print("Reservar Habitacion ya reservada")
    reservar_habitaciones(3)
    print("----------")
    print("----------")
    print("----------")

    print("Reservar Habitacion inexistente")
    reservar_habitaciones(27)
    print("----------")
    print("----------")
    print("----------")


    print("Liberar una Habitacion Inexistente")
    liberar_habitaciones(14)
    print("----------")
    print("----------")

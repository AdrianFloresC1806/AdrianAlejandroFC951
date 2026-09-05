# Flores Cisneros Adrian Alejandro
# 951
# Se elaboró el 30/08/2026
#Este programa en Python implementa un sistema de encriptación y desencriptación por sustitución mapeando letras a
# claves aleatorias de 3 caracteres. Genera un diccionario dinámico con combinaciones únicas para cada letra del
# abecedario, permitiendo codificar texto y luego revertirlo a su mensaje original. Incluye funciones específicas para
# realizar la conversión en ambas direcciones, así como para imprimir el diccionario de equivalencias generado durante
# la ejecución.


import random

abecedario="abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
todo="abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789!#%&'()*+,-./:;<=>?@[]^_`{|}~¡¿ÁÉÍÓÚáéíóúÜüÑñ"

dicc_encriptacion={}


for letra in abecedario:
    codigo= ""
    for i in range(3):
        codigo += random.choice(todo)

    dicc_encriptacion[letra]=codigo


def diccionario_encriptacion():
    for letra, codigo in dicc_encriptacion.items():
        print(f"({letra}, {codigo})")

def mensaje_encriptacion(mensaje):
    mensaje_encriptado= ""
    for letra in mensaje:
        mensaje_encriptado += dicc_encriptacion[letra]
    return mensaje_encriptado

def desencriptar(mensaje_encriptado):
    mensaje_desencriptado=""
    for i in range (0, len(mensaje_encriptado),3):
        codigo = mensaje_encriptado[i:i+3]
        for letra, valor in dicc_encriptacion.items():
            if valor == codigo:
                mensaje_desencriptado += letra
    return mensaje_desencriptado

def encriptado_desencriptado():
    for letra in desencriptado:
        print(f"({letra}, {dicc_encriptacion[letra]})")

if __name__ == "__main__":
    print("-----------------------------")
    print("Mensaje Encriptado")
    encriptado = mensaje_encriptacion("Azul")
    print(encriptado)

    print("-----------------------------")

    print("Mensaje Desencriptado")
    desencriptado = desencriptar(encriptado)
    print(desencriptado)

    print("-----------------------------")
    print("Codigo por letra")
    print(encriptado_desencriptado())

    print("-----------------------------")

    print("Diccionario de Encriptacion")
    print(diccionario_encriptacion())

#Flores Cisneros Adrian Alejandro
# 951
# Elaborado el 08/11/2026

import pandas as pd
import numpy as np


def crear_ventas():
    data = {
        "A": np.random.randint(100,1001, size = 3),
        "B": np.random.randint(100,1001, size = 3),
        "C": np.random.randint(100,1001, size = 3),
    }
    ventas = pd.DataFrame(data, index = ["Enero", "Febrero", "Marzo"])
    return ventas

def seleccionar_loc(ventas:pd.DataFrame, meses, productos=None):
    if productos is None:
        return ventas.loc[meses]
    return ventas.loc[meses, productos]

def seleccionar_iloc(ventas:pd.DataFrame, filas, columnas=None):
    if columnas is None:
        return ventas.iloc[filas]
    return ventas.iloc[filas, columnas]

def cambiar_venta(ventas:pd.DataFrame, mes, producto, valor):
    ventas.loc[mes, producto] = valor
    return ventas


if __name__=="__main__":
    ventas = crear_ventas()
    print(ventas)

    print("--------------------------------------------")
    print("--------------------------------------------")
    print("Ventas en Enero del Producto A")
    print(seleccionar_loc(ventas, "Enero", "A"))
    print("Ventas de todos los productos en Febrero")
    print(seleccionar_loc(ventas, "Febrero"))
    print("Ventas de todos los productos en el primer y tercer mes")
    print(seleccionar_loc(ventas, ["Enero", "Marzo"]))

    print("--------------------------------------------")
    print("--------------------------------------------")

    print("Ventas del primer mes para todos los productos")
    print(seleccionar_iloc(ventas, 0))
    print("Ventas del segundo producto en todos los meses")
    print(seleccionar_iloc(ventas, slice(None),1))
    print("Ventas del segundo y el tercer mes para el primer producto")
    print(seleccionar_iloc(ventas, [1,2],0))

    print("--------------------------------------------")
    print("--------------------------------------------")

    print("Cambiar ventas del producto B en marzo a 1200")
    print(cambiar_venta(ventas, "Marzo", "B",1200))


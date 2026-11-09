#Flores Cisneros Adrian Alejandro
# 951
# Elaborado el 08/11/2026
#


import pandas as pd

def crear_datos():
    data = {
        "Tienda":["A","A","A","B","B","B","C","C","C"],
        "Producto":["Manzana","Platano", "Naranaja","Manzana","Platano", "Naranaja","Manzana","Platano","Naranaja"],
        "Categoria":["Fruta","Fruta","Fruta","Fruta","Fruta","Fruta","Fruta","Fruta","Fruta",],
        "Precio":[30,20,35,25,30,45,35,20,25],
        "Cantidad_Vendida":[50,30,20,60,25,35,55,20,30],
        "Calificacion": ["A","B","C","A","B","A","C","B","A"]

    }
    df = pd.DataFrame(data)
    return df

def asignar_codigos(df: pd.DataFrame):
    df["Codigo_de_Tienda"] = df["Tienda"].map({"A":1,"B":2,"C":3})
    df ["Calificacion_Numerica"] = df["Calificacion"].map({"A":3,"B":2,"C":1})
    print(df)

def total_ventas_tienda(df: pd.DataFrame):
    df["Venta_Total"] = df["Precio"]*df["Cantidad_Vendida"]
    res = df.groupby("Tienda")["Venta_Total"].sum()
    print(res)

def precio_promedio_tienda(df: pd.DataFrame):
    res = df.groupby("Tienda")["Precio"].mean()
    print(res)

def cantidad_producto_tienda(df: pd.DataFrame):
    res = pd.pivot_table(df, values="Cantidad_Vendida", index="Producto", columns="Tienda", aggfunc="sum")
    print(res)

def total_ventas_producto_tienda(df: pd.DataFrame):
    df["Venta_Total"] = df["Precio"] * df["Cantidad_Vendida"]
    res = pd.pivot_table(df, values = "Venta_Total", index = "Producto", columns = "Tienda", aggfunc = "sum")
    print(res)


if __name__ == "__main__":
    df = crear_datos()

    asignar_codigos(df)
    print("---------------------------------")
    total_ventas_tienda(df)
    print("---------------------------------")
    precio_promedio_tienda(df)
    print("----------------------------------")
    cantidad_producto_tienda(df)
    print("----------------------------------")
    total_ventas_producto_tienda(df)
    print("----------------------------------")
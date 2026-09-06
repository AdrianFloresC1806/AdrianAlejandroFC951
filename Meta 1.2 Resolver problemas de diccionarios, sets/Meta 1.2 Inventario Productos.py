# Flores Cisneros Adrian Alejandro
# 951
# Se elaboró el 30/08/2026
#Este programa en Python implementa un sistema de gestión de inventario utilizando un diccionario donde cada código
# almacena el nombre, precio y cantidad del producto. Ofrece funciones para agregar, editar, eliminar, vender e
# imprimir los productos en existencia, controlando el stock disponible en cada transacción. Finalmente, ejecuta un
# bloque de pruebas para validar operaciones habituales y manejar casos de error como códigos repetidos o inventario
# insuficiente.



inventario = {}

def agregar_prod( codigo, nombre, precio, cantidad):
    if codigo in inventario:
        print(f"El producto {codigo} ya existe")

    inventario[codigo] ={
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    print(f"El Producto: {nombre} fue agregado")

def editar_prod( codigo, nombre=None, precio=None, cantidad=None):
    if codigo not in inventario:
        print(f"El producto {codigo} no existe")
        return
    if nombre is not None:
        inventario[codigo]["nombre"] = nombre
    if precio is not None:
        inventario[codigo]["precio"] = precio
    if cantidad is not None:
        inventario[codigo]["cantidad"] = cantidad
    print(f"El Producto: {nombre} fue ediado")

def eliminar_prod( codigo):
    if codigo in inventario:
        producto_eliminado = inventario.pop(codigo)
        print(f"El producto {codigo} fue eliminado")
    else:
        print(f"El producto {codigo} no existe")

def ventar_prod( codigo, cantidad_venddida):
    if codigo not in inventario:
        print(f"El producto {codigo} no existe")
        return
    producto = inventario[codigo]
    if cantidad_venddida > producto["cantidad"]:
        print(f"La cantidad del producto {codigo} es insuficiente")
        return

    producto["cantidad"] -= cantidad_venddida
    total = producto["precio"] + producto["cantidad"]
    print(f"Venta Exitosa: {cantidad_venddida} {producto['nombre']} = ${total:.2f}")
    print(f"Cantidad del Producto {codigo} es: {producto['cantidad']}")

def imprimir_inventario():
    if not inventario:
        print("El Inventario se encuentea vacio")

    else:
        print("Inventario")
        for codigo,datos in inventario.items():
            print(f"[{codigo}]{datos['nombre']} - Precio: ${datos['precio']:.2f} - Cantidad: {datos['cantidad']}")


if __name__ == "__main__":
    print("Imprimir el Inventario cuando esta Vacio")
    imprimir_inventario()


    print("----------------------------")
    print("Agregar productos")
    agregar_prod(1,"Collar", 600,5)
    agregar_prod(2,"Pendiente", 200,5)
    agregar_prod(3,"Anillo", 800,2)
    agregar_prod(4,"Pulsera", 150,20)
    print("----------------------------")

    print("----------------------------")
    print("Agregar productos con codigo Repetido")
    agregar_prod(3,"Anillo de oro", 200000,5)
    print("----------------------------")

    print("----------------------------")
    print("Eliminar un producto")
    eliminar_prod(2)
    print("----------------------------")

    print("----------------------------")
    print("Hacer una Venta")
    ventar_prod(1,1)
    imprimir_inventario()
    print("----------------------------")

    print("----------------------------")
    print("Hacer una Venta con productos insuficientes")
    ventar_prod(3,3)
    imprimir_inventario()
    print("----------------------------")

    print("----------------------------")
    print("Editar productos")
    imprimir_inventario()
    editar_prod(1,"Collar", 650,4)
    imprimir_inventario()
    print("----------------------------")
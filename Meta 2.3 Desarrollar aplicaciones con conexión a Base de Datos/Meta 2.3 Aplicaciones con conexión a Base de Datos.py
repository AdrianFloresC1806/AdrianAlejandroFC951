# Flores Cisneros Adrian Alejandro
# Se elaboro el 11/10/2026

import pyodbc
from datetime import date, datetime


SERVIDOR = r"localhost\SQLEXPRESS"
BASE_DATOS = "eventos_universitarios"
DRIVER = "ODBC Driver 18 for SQL Server"


def conectar():
    try:
        conexion = pyodbc.connect(
            f"DRIVER={{{DRIVER}}};"
            f"SERVER={SERVIDOR};"
            f"DATABASE={BASE_DATOS};"
            "Trusted_Connection=yes;"
        )
        return conexion
    except pyodbc.Error as error:
        print(f"\nNo fue posible conectar con la base de datos: {error}")
        return None


def imprimir_tabla(filas, con_disponibles=False):
    if not filas:
        print("\nNo se encontraron eventos.")
        return

    encabezado = (f"{'ID':<4}{'Nombre':<55}{'Fecha':<12}{'Hora':<7}"
                  f"{'Lugar':<26}{'Cupo':>5}{'Reg.':>6}")
    if con_disponibles:
        encabezado += f"{'Disp.':>7}"
    print("\n" + encabezado)
    print("-" * len(encabezado))

    for f in filas:
        linea = (f"{f.id:<4}{f.nombre[:53]:<55}{f.fecha.strftime('%d/%m/%Y'):<12}"
                 f"{f.hora.strftime('%H:%M'):<7}{f.lugar[:24]:<26}"
                 f"{f.cupo:>5}{f.registrados:>6}")
        if con_disponibles:
            linea += f"{f.cupo - f.registrados:>7}"
        print(linea)


def leer_entero(mensaje):
    try:
        return int(input(mensaje).strip())
    except ValueError:
        print("Debes escribir un número entero.")
        return None


def leer_fecha(mensaje):
    try:
        return datetime.strptime(input(mensaje).strip(), "%Y-%m-%d").date()
    except ValueError:
        print("Fecha inválida. Usa el formato AAAA-MM-DD (ej. 2026-12-05).")
        return None


def leer_hora(mensaje):
    try:
        return datetime.strptime(input(mensaje).strip(), "%H:%M").time()
    except ValueError:
        print("Hora inválida. Usa el formato HH:MM (ej. 14:30).")
        return None


def mostrar_eventos():
    conexion = None
    try:
        conexion = conectar()
        if conexion is None:
            return
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT id, nombre, fecha, hora, lugar, cupo, registrados "
            "FROM eventos ORDER BY fecha, hora"
        )
        imprimir_tabla(cursor.fetchall())
    except pyodbc.Error as error:
        print(f"\nFalló la consulta de eventos: {error}")
    finally:
        if conexion:
            conexion.close()


def buscar_evento(texto):
    conexion = None
    try:
        conexion = conectar()
        if conexion is None:
            return
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT id, nombre, fecha, hora, lugar, cupo, registrados "
            "FROM eventos WHERE nombre LIKE ? ORDER BY fecha, hora",
            (f"%{texto}%",),
        )
        imprimir_tabla(cursor.fetchall())
    except pyodbc.Error as error:
        print(f"\nFalló la búsqueda de eventos: {error}")
    finally:
        if conexion:
            conexion.close()


def eventos_con_disponibilidad(asistentes):
    if asistentes <= 0:
        print("El número de asistentes debe ser mayor que cero.")
        return
    conexion = None
    try:
        conexion = conectar()
        if conexion is None:
            return
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT id, nombre, fecha, hora, lugar, cupo, registrados "
            "FROM eventos WHERE (cupo - registrados) >= ? ORDER BY fecha, hora",
            (asistentes,),
        )
        filas = cursor.fetchall()
        if not filas:
            print(f"\nNingún evento tiene lugar para {asistentes} asistente(s).")
        else:
            print(f"\nEventos con lugar para {asistentes} asistente(s):")
            imprimir_tabla(filas, con_disponibles=True)
    except pyodbc.Error as error:
        print(f"\nFalló la consulta de disponibilidad: {error}")
    finally:
        if conexion:
            conexion.close()


def registrar_asistentes(id_evento, cantidad):
    if cantidad <= 0:
        print("La cantidad de asistentes debe ser mayor que cero.")
        return
    conexion = None
    try:
        conexion = conectar()
        if conexion is None:
            return
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT nombre, cupo, registrados FROM eventos WHERE id = ?", (id_evento,)
        )
        evento = cursor.fetchone()
        if evento is None:
            print(f"No existe un evento con id {id_evento}.")
            return

        disponibles = evento.cupo - evento.registrados
        if cantidad > disponibles:
            print(f"Cupo insuficiente. Lugares disponibles: {disponibles}.")
            return

        # La condición en el WHERE evita que dos usuarios sobrepasen el cupo a la vez.
        cursor.execute(
            "UPDATE eventos SET registrados = registrados + ? "
            "WHERE id = ? AND registrados + ? <= cupo",
            (cantidad, id_evento, cantidad),
        )
        if cursor.rowcount == 0:
            conexion.rollback()
            print("No se pudo registrar: el cupo cambió mientras se procesaba.")
            return

        conexion.commit()
        print(f"\nRegistro exitoso en '{evento.nombre}'.")
        print(f"Registrados actuales: {evento.registrados}")
        print(f"Nuevos asistentes: {cantidad}")
        print(f"Nuevo total de registrados: {evento.registrados + cantidad}")
    except pyodbc.Error as error:
        if conexion:
            conexion.rollback()
        print(f"\nFalló el registro de asistentes: {error}")
    finally:
        if conexion:
            conexion.close()


def cancelar_registros(id_evento, cantidad):
    if cantidad <= 0:
        print("La cantidad a cancelar debe ser mayor que cero.")
        return
    conexion = None
    try:
        conexion = conectar()
        if conexion is None:
            return
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT nombre, registrados FROM eventos WHERE id = ?", (id_evento,)
        )
        evento = cursor.fetchone()
        if evento is None:
            print(f"No existe un evento con id {id_evento}.")
            return

        if cantidad > evento.registrados:
            print(f"Solo hay {evento.registrados} persona(s) registrada(s); "
                  f"no se pueden cancelar {cantidad}.")
            return

        cursor.execute(
            "UPDATE eventos SET registrados = registrados - ? "
            "WHERE id = ? AND registrados >= ?",
            (cantidad, id_evento, cantidad),
        )
        if cursor.rowcount == 0:
            conexion.rollback()
            print("No se pudo cancelar: los registros cambiaron mientras se procesaba.")
            return

        conexion.commit()
        print(f"\nSe cancelaron {cantidad} registro(s) en '{evento.nombre}'.")
        print(f"Nuevo total de registrados: {evento.registrados - cantidad}")
    except pyodbc.Error as error:
        if conexion:
            conexion.rollback()
        print(f"\nFalló la cancelación de registros: {error}")
    finally:
        if conexion:
            conexion.close()


def agregar_evento(nombre, fecha, hora, lugar, cupo):
    if cupo <= 0:
        print("El cupo debe ser mayor que cero.")
        return
    conexion = None
    try:
        conexion = conectar()
        if conexion is None:
            return
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO eventos (nombre, fecha, hora, lugar, cupo, registrados) "
            "VALUES (?, ?, ?, ?, ?, 0)",
            (nombre, fecha, hora, lugar, cupo),
        )
        conexion.commit()
        print(f"\nEvento '{nombre}' agregado correctamente.")
    except pyodbc.Error as error:
        if conexion:
            conexion.rollback()
        print(f"\nNo se pudo agregar el evento: {error}")
    finally:
        if conexion:
            conexion.close()


def modificar_evento(id_evento, campo, nuevo_valor):
    # El nombre de la columna no puede ir como parámetro, por eso se valida
    # contra una lista cerrada (nunca proviene directamente del usuario).
    columnas_permitidas = {"fecha", "hora", "lugar", "cupo"}
    if campo not in columnas_permitidas:
        print("Campo no permitido.")
        return
    conexion = None
    try:
        conexion = conectar()
        if conexion is None:
            return
        cursor = conexion.cursor()

        cursor.execute("SELECT registrados FROM eventos WHERE id = ?", (id_evento,))
        evento = cursor.fetchone()
        if evento is None:
            print(f"No existe un evento con id {id_evento}.")
            return

        if campo == "cupo" and (nuevo_valor <= 0 or nuevo_valor < evento.registrados):
            print(f"El cupo debe ser mayor que cero y no menor que los "
                  f"registrados actuales ({evento.registrados}).")
            return

        cursor.execute(
            f"UPDATE eventos SET {campo} = ? WHERE id = ?", (nuevo_valor, id_evento)
        )
        conexion.commit()
        print(f"\nEl campo '{campo}' del evento {id_evento} se actualizó correctamente.")
    except pyodbc.Error as error:
        if conexion:
            conexion.rollback()
        print(f"\nNo se pudo modificar el evento: {error}")
    finally:
        if conexion:
            conexion.close()



def mostrar_eventos_proximos():
    conexion = None
    try:
        conexion = conectar()
        if conexion is None:
            return
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT id, nombre, fecha, hora, lugar, cupo, registrados "
            "FROM eventos "
            "WHERE fecha >= ? AND (cupo - registrados) > 0 "
            "ORDER BY fecha, hora",
            (date.today(),),
        )
        filas = cursor.fetchall()
        if not filas:
            print("\nNo hay eventos próximos con lugares disponibles.")
        else:
            print("\nEventos próximos con lugares disponibles:")
            imprimir_tabla(filas, con_disponibles=True)
    except pyodbc.Error as error:
        print(f"\nFalló la consulta de eventos próximos: {error}")
    finally:
        if conexion:
            conexion.close()


def opcion_modificar():
    id_evento = leer_entero("ID del evento a modificar: ")
    if id_evento is None:
        return
    print("¿Qué deseas modificar?  1) Fecha  2) Hora  3) Lugar  4) Cupo")
    opcion = input("Opción: ").strip()

    if opcion == "1":
        valor = leer_fecha("Nueva fecha (AAAA-MM-DD): ")
        campo = "fecha"
    elif opcion == "2":
        valor = leer_hora("Nueva hora (HH:MM): ")
        campo = "hora"
    elif opcion == "3":
        valor = input("Nuevo lugar: ").strip()
        campo = "lugar"
        if not valor:
            print("El lugar no puede estar vacío.")
            return
    elif opcion == "4":
        valor = leer_entero("Nuevo cupo: ")
        campo = "cupo"
    else:
        print("Opción no válida.")
        return

    if valor is not None:
        modificar_evento(id_evento, campo, valor)


def opcion_agregar():
    nombre = input("Nombre del evento: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return
    fecha = leer_fecha("Fecha (AAAA-MM-DD): ")
    if fecha is None:
        return
    hora = leer_hora("Hora (HH:MM): ")
    if hora is None:
        return
    lugar = input("Lugar: ").strip()
    if not lugar:
        print("El lugar no puede estar vacío.")
        return
    cupo = leer_entero("Cupo máximo: ")
    if cupo is None:
        return
    agregar_evento(nombre, fecha, hora, lugar, cupo)

def mostrar_menu():
    print("\n===== SISTEMA DE EVENTOS UNIVERSITARIOS =====\n")
    print("1. Mostrar eventos")
    print("2. Buscar evento")
    print("3. Consultar eventos con disponibilidad")
    print("4. Registrar asistentes")
    print("5. Cancelar registros")
    print("6. Agregar evento")
    print("7. Modificar evento")
    print("8. Mostrar eventos próximos")
    print("9. Salir")


if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ").strip()

        if opcion == "1":
            mostrar_eventos()
        elif opcion == "2":
            texto = input("Texto a buscar en el nombre: ").strip()
            if texto:
                buscar_evento(texto)
            else:
                print("[ERROR] Debes escribir un texto.")
        elif opcion == "3":
            n = leer_entero("Número de asistentes a registrar: ")
            if n is not None:
                eventos_con_disponibilidad(n)
        elif opcion == "4":
            id_evento = leer_entero("ID del evento: ")
            n = leer_entero("Número de asistentes a registrar: ")
            if id_evento is not None and n is not None:
                registrar_asistentes(id_evento, n)
        elif opcion == "5":
            id_evento = leer_entero("ID del evento: ")
            n = leer_entero("Número de registros a cancelar: ")
            if id_evento is not None and n is not None:
                cancelar_registros(id_evento, n)
        elif opcion == "6":
            opcion_agregar()
        elif opcion == "7":
            opcion_modificar()
        elif opcion == "8":
            mostrar_eventos_proximos()
        elif opcion == "9":
            print("\nSesion cerrada.")
            break
        else:
            print("\nERROR Opción no válida. Elige un número del 1 al 9.")
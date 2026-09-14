# Flores Cisneros Adrian Alejandro
# 951
# Se realizó el 13/09/2026
# Este script es la continuación del anterior, pero basicamente aquí se recuperan datos del producto que se quiere revisar
# se recopilan datos como el Nombre, el precio y la fecha de entrega que aparece en el tablon principal de cada producto
# toda la información se termina guardando en un CSV en el cual agrego explicitamente que busqueda se hizo y los productos que
# fueron lanzados a traves de esa busqueda, al igual que el número de página del cual se extrajeron los datos.

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def extraer_datos_producto(producto, num_pag, limite_pag):
    if num_pag > limite_pag:
        print(f"El número de página {num_pag} no existe en el apartado de {producto}")
        return [] # este ayuda a devolver una lista vacia en caso de que la pagina no exista

    url = "https://www.mercadolibre.com.mx/"
    s = Service(ChromeDriverManager().install())
    opc = Options()
    opc.add_argument('--window-size=1020x800')
    navegador = webdriver.Chrome(service=s, options=opc)
    wait = WebDriverWait(navegador, 10)

    data = []

    try:
        navegador.get(url)
        time.sleep(2)

        txtuser = wait.until(
            EC.presence_of_element_located((By.ID, "cb1-edit"))
        )
        buttonsearch = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "nav-search-btn"))
        )

        txtuser.send_keys(producto)
        time.sleep(2)
        buttonsearch.send_keys(Keys.ENTER)
        time.sleep(2)

        buttonsearchnum = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//a[@aria-label='Ir a la página {num_pag}']"))
        )
        buttonsearchnum.send_keys(Keys.ENTER)
        time.sleep(4)

        # aquí empieza la extracción de los datos en las páginas específicas
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ui-search-layout")))
        items = navegador.find_elements(By.CLASS_NAME, "poly-card")

        for item in items:
            try:
                nombre = item.find_element(By.CLASS_NAME, "poly-component__title").text
            except:
                nombre = "No tiene un nombre registrado"

            try:
                precio = item.find_element(By.CLASS_NAME, "andes-money-amount__fraction").text
            except:
                precio = "Precio no disponible"

            try:
                fecha_entrega = item.find_element(By.CLASS_NAME, "polylabel-pill").text
            except:
                fecha_entrega = "Sin Especificar"

            if not fecha_entrega.startswith("Llega"):
                fecha_entrega = "Sin Especificar"

            data.append({"Producto": producto, "Nombre": nombre, "Precio ($)": precio, "Fecha_Entrega": fecha_entrega, "Num_Pagina": num_pag})

    finally: # este finally deja que lo que reste del codigo se ejecute, sin importar si hay un error
        navegador.close()

    return data

# este lo uso para hacer el codigo más pequeño, ya que el otro era grande, basicamente en esta parte defino que se hara y
# que es lo que no se puede hacer en caso de. La parte mala es que el sitio web se abrira y cerrara despues de finalizar con cada producto
def luz(producto, num_pag):
    return extraer_datos_producto(producto, num_pag, limite_pag=10)

def proyectores(producto, num_pag):
    return extraer_datos_producto(producto, num_pag, limite_pag=5)

def pantalla(producto, num_pag):
    return extraer_datos_producto(producto, num_pag, limite_pag=6)


if __name__ == "__main__":
    todos_los_datos = []

    todos_los_datos.extend(luz("Lamp Girat", 1))
    todos_los_datos.extend(proyectores("Proyector 8k", 2))
    todos_los_datos.extend(pantalla("Pantalla para proyector enrollable", 4))

    # este if lo uso para meter absolutamente TODOS los datos de todos los productos diferentes
    if todos_los_datos:
        df = pd.DataFrame(todos_los_datos)
        df.to_csv("Recopilacion_Productos.csv", index=False, encoding='utf-8-sig')
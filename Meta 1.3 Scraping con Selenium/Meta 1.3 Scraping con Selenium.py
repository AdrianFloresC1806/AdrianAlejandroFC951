# Flores Cisneros Adrian Alejandro
# 951
# Se realizó el 05/09/2026
#Este script usa Selenium para automatizar búsquedas de productos en MercadoLibre. Para cada producto, escribe el
# término en el buscador, confirma con Enter y toma una captura de los resultados. Luego localiza el botón de la página
# deseada mediante su atributo aria-label (con XPath que me ayuda a buscar el atributo de forma "diferente"),
# hace clic y captura esa segunda vista. Se usan esperas explícitas (WebDriverWait) para asegurar que cada elemento
# exista antes de interactuar con él y que este no salte un error.

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def luz(producto,num_pag):

    url="https://www.mercadolibre.com.mx/"
    s=Service(ChromeDriverManager().install())
    opc=Options()
    opc.add_argument('--window-size=1020x800')
    navegador=webdriver.Chrome(service=s, options=opc)

    wait=WebDriverWait(navegador,10)

    navegador.get(url)
    time.sleep(2)

    txtuser=wait.until(
        EC.presence_of_element_located((By.ID, "cb1-edit"))
    )

    buttonsearch=wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "nav-search-btn"))
    )
    txtuser.send_keys(producto)
    time.sleep(2)
    buttonsearch.send_keys(Keys.ENTER)
    time.sleep(2)

    buttonsearchnum=wait.until(
        EC.element_to_be_clickable((By.XPATH, f"//a[@aria-label='Ir a la página {num_pag}']"))
    )
    #el xpath busca de forma general (id, Class, etc) en este caso para buscar un atributo con un identificador unico
    # aria-label cumple con lo que yo queria hacer ## //a busca la etiqueta con la estructura [@atributo = 'descripcion']

    buttonsearchnum.send_keys(Keys.ENTER)
    time.sleep(4)
    navegador.save_screenshot("Meta 1.3 pLuz.png")
    time.sleep(2)
    navegador.close()

def proyectores(producto,num_pag):

    url="https://www.mercadolibre.com.mx/"
    s=Service(ChromeDriverManager().install())
    opc=Options()
    opc.add_argument('--window-size=1020x800')
    navegador=webdriver.Chrome(service=s, options=opc)

    wait=WebDriverWait(navegador,10)

    navegador.get(url)
    time.sleep(2)

    txtuser=wait.until(
        EC.presence_of_element_located((By.ID, "cb1-edit"))
    )

    buttonsearch=wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "nav-search-btn"))
    )


    txtuser.send_keys(producto)
    time.sleep(2)
    buttonsearch.send_keys(Keys.ENTER)
    time.sleep(2)

    if num_pag > 5:
        print(f"La pagina numero {num_pag} no existe en el apartado de {producto}")

    else:

        buttonsearchnum=wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//a[@aria-label='Ir a la página {num_pag}']"))
        )

        buttonsearchnum.send_keys(Keys.ENTER)
        time.sleep(4)
        navegador.save_screenshot("Meta 1.3 qProyector.png")
        time.sleep(2)
        navegador.close()

def pantalla(producto, num_pag):

    url = "https://www.mercadolibre.com.mx/"
    s = Service(ChromeDriverManager().install())
    opc = Options()
    opc.add_argument('--window-size=1020x800')
    navegador = webdriver.Chrome(service=s, options=opc)

    wait = WebDriverWait(navegador, 10)

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

    if num_pag > 6:
        print(f"El numero de pagina {num_pag} no existe en el apartado de {producto}")

    else:
        buttonsearchnum=wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//a[@aria-label='Ir a la página {num_pag}']"))
        )

        buttonsearchnum.send_keys(Keys.ENTER)
        time.sleep(4)
        navegador.save_screenshot("Meta 1.3 rPantalla.png")
        time.sleep(2)
        navegador.close()



if __name__ == "__main__":
    luz("Lamp Girat",6)
    proyectores("Proyector 8k",5)
    pantalla("Pantalla para proyector enrollable", 3)

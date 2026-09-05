import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def luz(producto):
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
    txtuser.send_keys(Keys.ENTER)
    time.sleep(2)
    navegador.save_screenshot("M1.3.png")
    time.sleep(2)
    navegador.close()

def proyectores(producto):
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
    txtuser.send_keys(Keys.ENTER)
    time.sleep(2)
    navegador.save_screenshot("M1.3-Proyector.png")
    time.sleep(2)
    navegador.close()

def pantalla(producto):
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
    txtuser.send_keys(Keys.ENTER)
    time.sleep(2)
    navegador.save_screenshot("M1.3-Pantalla8k.png")
    time.sleep(2)
    navegador.close()



if __name__ == "__main__":
    luz("Lamp Girat")
    proyectores("Proyector 8k")
    pantalla("Pantalla para Proyector 8k")

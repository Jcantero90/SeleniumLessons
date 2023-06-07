'''
Seleccionamos de una tabla los elementos internos a través del select, es igual que en cypress.
'''

import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException  # para hacer el tryCatch.
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select #importamos el select.

service = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

# driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")

driver.get("http://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
driver.maximize_window()

tabla = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#select-demo")))
#tabla = driver.find_element_by_css_selector("#select-demo")
selectorTabla = Select(tabla)
selectorTabla.select_by_visible_text("Wednesday") #Esto selecciona elementos de la tabla a través del texto.
selectorTabla.select_by_index(1) #Elige el elemento a través de su posición en el index.
selectorTabla.select_by_value("Sunday") #Elige elementos a través del value (inspeccionar elemento).

selectorTabla = Select(driver.find_element_by_css_selector("#select-demo")); selectorTabla.select_by_visible_text("Saturday")

time.sleep(2)

#Primero ejecutamos un error.
try:
    selectorTablaTiempo = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#select-demo")))
    selectorTablaContiempo = Select(selectorTablaTiempo)
    selectorTablaContiempo.select_by_visible_text("Wednesdayy")  # Esto selecciona elementos de la tabla a través del texto. Aquí tenemos el error, no existe Wednesdayy.
    selectorTablaContiempo.select_by_index(1)  # Elige el elemento a través de su posición en el index.
    selectorTablaContiempo.select_by_value("Sunday")  # Elige elementos a través del value (inspeccionar elemento).
except NoSuchElementException as ex:
    print(ex.msg)
    print("el elemento no funciona.")
time.sleep(2)

#luego ejecutará este código tan normal.
try:
    selectorTablaTiempo = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#select-demo")))
    selectorTablaContiempo = Select(selectorTablaTiempo)
    selectorTablaContiempo.select_by_visible_text("Wednesday")  # Esto selecciona elementos de la tabla a través del texto.
    selectorTablaContiempo.select_by_index(1)  # Elige el elemento a través de su posición en el index.
    selectorTablaContiempo.select_by_value("Wednesday")  # Elige elementos a través del value (inspeccionar elemento).
except NoSuchElementException as ex:
    print(ex.msg)
    print("el elemento no funciona.")

time.sleep(2)
driver.close()
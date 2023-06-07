import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

# driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")

driver.get("https://demoqa.com/text-box")
driver.maximize_window()

nombre = driver.find_element_by_css_selector("#userName").send_keys("ExampleName")

button = driver.find_element_by_css_selector("#submit")

#Vamos a hacer una validación, para saber si el botón está disponible o no.
time.sleep(2)
if (button.is_enabled()==True):
    button.click()
    print("el botón está disponible")

#Esta sentencia no se ejecutará, ya que el botón SI está disponible.
if (button.is_displayed()==False):
    button.click()
    print("el botón no está disponible")

time.sleep(2)

#Validar un texto
texto = driver.find_element_by_css_selector("#name")

if (texto.text == "Name:ExampleName"):
    print("El texto "+texto.text+" coincide.")

else:
    print("El texto "+texto.text+" no coincide.")

time.sleep(2)
driver.close()
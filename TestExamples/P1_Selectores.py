#En esta página tocaremos los diferentes selectores que hay en Python.

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #Para usar el By a la hora de buscar un elemento.

service = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

# driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")

driver.get("https://demoqa.com/text-box")
driver.maximize_window()

nom = driver.find_element_by_id("userName") #elige un elemento con el find element
nom.send_keys("Yoni") #el send keys escribe lo que quieras.

email = driver.find_element_by_id("userEmail").send_keys("correoFake@email.com") #también puedes concatenar así.

address = driver.find_element_by_xpath("//*[@id='currentAddress']")\
    .send_keys("ejemplo") #Cogiendo el elemento por el Xpath.

PAddress = driver.find_element(By.ID,"permanentAddress").send_keys("permanent Address") #usamos el find element by id.

nameByCss = driver.find_element_by_css_selector("#submit").click() #El selector CSS es cuando inspeccionamos un elemento y copiamos el elemento.

elementsTableCssSelector = driver.find_element_by_css_selector("#item-2 > span") #otro elemento seleccionado por CSS.
elementsTableCssSelector.click()
time.sleep(2)

#vamos a buscar por el link text,
#El link text es el texto que se muestra a un visitante de la web y que se dirige a la página de destino con un hipervínculo.
#Son los Href. 
driver.get("https://demoqa.com/profile")

links = driver.find_element_by_link_text("login")\
    .click()


time.sleep(2)
driver.close()

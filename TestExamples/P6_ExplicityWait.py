#permite que un elemento desaparezca para pasar la prueba.

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#librerías para esperar a que un elemento desaparezca
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")


driver.get("http://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")
driver.maximize_window()
driver.find_element_by_css_selector("#downloadButton").click()

wait = WebDriverWait(driver, 20) #Aquí especifico que no esperemos más de 20 segundos a que desaparezca el elemento.

print("esperando a que desaparezca el elemento...")

#Aquí es donde le diremos lo que queremos hacer, el objeto EC tiene múltiples funcionalidades, esta en concreto espera que une elemento desaparezca.
elemento = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.ui-dialog.ui-corner-all.ui-widget" 
                                                                       ".ui-widget-content.ui-front.ui-dialog-buttons"
                                                                       ".ui-draggable > "
                                                                       "div.ui-dialog-buttonpane.ui-widget-content.ui"
                                                                       "-helper-clearfix > div > button")))

# Esperamos a que el elemento desaparezca de la página
wait.until(EC.staleness_of(elemento))

print("el elemento ha desaparecido tras 5 segundos. ")


time.sleep(2)
driver.close()
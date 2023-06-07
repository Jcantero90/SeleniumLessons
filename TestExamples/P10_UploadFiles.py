#Ensayaremos un script para subir archivos.
#Hemos creado una carpeta llamada "files" en el directorio raiz.
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

# driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")

driver.get("https://the-internet.herokuapp.com/upload")
driver.maximize_window()

#Una forma de subir un archivo es seleccionar el botón de subida de archivos, y hacerle un senKeys con la ruta del archivo que queremos subir.
buttonUploadFiles = driver.find_element_by_css_selector("#file-upload")
buttonUploadFiles.send_keys("C://Users//jonatan.cantero//Documents//Apuntes//Conceptos Testing//Selenium + python//ProyectoSelenium//files//imagen.jpg")
time.sleep(2)

#Es de buena práctica usar la ruta relativa, en vez de la absoluta, ya que cuando este código se ejecute de una máquina a otra,
#la ruta absoluta cambiará, pero la relativa no.

import os #Necesitamos importar os para llamar a la ruta relativa.

ruta_archivo = os.path.abspath("../files/imagen - copia.jpg")#Aquí especificamos la ruta del archivo,

buttonUploadFiles.send_keys(ruta_archivo)



time.sleep(2)
driver.close()
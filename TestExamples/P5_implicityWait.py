#con el implicity wait podremos hacer que las pruebas no fallen instantaneamente, sino que le daremos a la busqueda del elemento unos segundos de cortesia antes de que la prueba falle. 
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

# driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
driver.implicitly_wait(5)#Le aplica tiempo a la busqueda de un elemento. si no lo encuentra tarda en este caso 5 segundo en fallar la prueba.

#Esta prueba fallará a caso hecho, ya que queremos que no encuentre el elemento para que la prueba a los 5 segundos falle.
nom = driver.find_element_by_id("userNam").send_keys("esto es un send keys")

time.sleep(2)
driver.close()
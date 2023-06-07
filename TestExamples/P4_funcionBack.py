#volver atrás o hacia delante en una página. No sirve para nada pero lo doy de todas formas.
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

# driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")

driver.get("https://demoqa.com/text-box")
print("visitando demoQA...")
time.sleep(2)
driver.get("https://the-internet.herokuapp.com")
print("visitando The-internet.herokuap...")
time.sleep(2)
driver.get("https://www.seleniumeasy.com/")
print("visitando SeleniumEasy...")
time.sleep(2)
driver.back()#para volver una página atrás, es la forma fácil.
print("volviendo a The internet...")
time.sleep(2)
driver.execute_script("window.history.go(-1)") #diciendole que volvamos una página atrás.
print("volviendo a SeleniumEasy...")
driver.execute_script("window.history.go(2)") #hemos ido a la última página
time.sleep(2)


time.sleep(2)
driver.close()
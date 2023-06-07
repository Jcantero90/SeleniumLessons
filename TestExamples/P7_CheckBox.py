#Validamos los checkboxes.

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

# driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")

driver.get("http://demo.seleniumeasy.com/basic-checkbox-demo.html")
driver.maximize_window()

checkbox = WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#isAgeSelected"))) ##webdriver valida el tiempo, y el EC es el assertion, le decimos la validación que necesitamos.
checkbox.click()

if checkbox.is_selected():
    print("El checkbox está seleccionado")
else:
    print("El checkbox NO está seleccionado")

checkbox.click()

if checkbox.is_selected():
    print("El checkbox está seleccionado")
else:
    print("El checkbox NO está seleccionado")

time.sleep(2)
driver.close()

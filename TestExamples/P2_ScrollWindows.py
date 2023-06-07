# Bajar página.
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

# driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
nom = driver.find_element_by_id("userName")
nom.send_keys("yoni")

driver.execute_script("window.scrollTo(0,1000)")  # hace un scroll hacia la posición que indicamos.
time.sleep(2)

# Para hacer Scroll para que se mueva hacia un elemento.
subitButton = driver.find_element_by_css_selector("#submit")

ir = driver.execute_script("arguments[0].scrollIntoView();", subitButton)

time.sleep(2)
driver.close()

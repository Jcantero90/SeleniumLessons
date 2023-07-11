#Función Tab para no usar tantos selectores. 

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

service = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

# driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")

driver.get("https://demoqa.com/text-box")

driver.maximize_window()

nom = driver.find_element_by_id("userName") #

nom.send_keys("Yoni"  #escribimos el dato del primer text box.
              + Keys.TAB
              + "emaildeYoni@gmail.com"
              + Keys.TAB
              + "otro dato sin importancia"
              + Keys.TAB
              + "dorito"
              + Keys.ENTER #Es pasa pulsar enter.
              + "Huevo kinder"
              )

elements = driver.find_element_by_css_selector("#submit")
elements.click()

time.sleep(2)
driver.close()
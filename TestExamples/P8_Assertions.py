'''

Aquí te describo todas las variables que ofrece el alias `EC`:

- `title_is(title)`: espera a que el título de la página sea exactamente igual al valor de `title`.
- `title_contains(title)`: espera a que el título de la página contenga el valor de `title`.
- `presence_of_element_located(locator)`: espera a que el elemento especificado por el `locator` (por ejemplo, un objeto `By`) esté presente en el DOM de la página.
- `visibility_of_element_located(locator)`: espera a que el elemento especificado por el `locator` sea visible y tenga un tamaño mayor que cero.
- `visibility_of(element)`: espera a que el elemento sea visible y tenga un tamaño mayor que cero.
- `presence_of_all_elements_located(locator)`: espera a que todos los elementos especificados por el `locator` estén presentes en el DOM de la página.
- `text_to_be_present_in_element(locator, text)`: espera a que el texto especificado por `text` esté presente en el elemento especificado por el `locator`.
- `text_to_be_present_in_element_value(locator, text)`: espera a que el valor del atributo `value` del elemento especificado por el `locator` contenga el valor de `text`.
- `frame_to_be_available_and_switch_to_it(locator)`: espera a que el marco especificado por el `locator` esté disponible y cambia al contexto del marco.
- `invisibility_of_element_located(locator)`: espera a que el elemento especificado por el `locator` no sea visible en la página.
- `element_to_be_clickable(locator)`: espera a que el elemento especificado por el `locator` sea visible y habilitado, lo que significa que se puede hacer clic en él.
- `element_to_be_selected(element)`: espera a que el elemento especificado esté seleccionado.
- `element_located_to_be_selected(locator)`: espera a que el elemento especificado por el `locator` esté seleccionado.
- `element_selection_state_to_be(element, is_selected)`: espera a que el elemento especificado tenga el estado de selección especificado (`True` si está seleccionado, `False` si no lo está).
- `element_located_selection_state_to_be(locator, is_selected)`: espera a que el elemento especificado por el `locator` tenga el estado de selección especificado.
- `alert_is_present()`: espera a que aparezca una alerta.

Estas son las variables más comunes que ofrece `EC`, pero hay muchas otras que puedes explorar en la documentación oficial de Selenium.

'''

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("C:\Drivers\chromedriver.exe")
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

# driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")

'''
HACER UN ASSERTION CON TODOS LOS MÉTODOS QUE HAY ARRIBA. 
'''

driver.get("http://demo.seleniumeasy.com/basic-checkbox-demo.html")
driver.maximize_window()

title = WebDriverWait(driver, 10).until(EC.title_is((driver.title,"Selenium Easy")))

print(title)

time.sleep(2)
driver.close()

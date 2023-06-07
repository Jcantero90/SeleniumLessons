import unittest
import time
from selenium import webdriver
from ..Funciones.PO_functions import PO_functions

#Hemos de declarar la clase
class TestStringMethods(unittest.TestCase):

#Es la configuración de las pruebas como tal, definimos el webdriver.
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

#Es nuestro test, aquí usamor la variable self.driver para realizar las pruebas que necesitesmo.
    def test1(self):
        driver = self.driver
        function = PO_functions(driver)
        function.holaMundo()
        function.timeFunction(2)

    def test2(self):
        driver = self.driver
        function = PO_functions(driver)
        function.pruebaArgumentos("https://demoqa.com/text-box","#userName","Name")
        function.timeFunction(2)
        f = function.GetCss("#userName")
        f.send_keys("asoidmfo")

#El tearDown es para cerrar nuestros test.
    def tearDown(self):
        driver = self.driver
        driver.close()
if __name__ == '__main__':
    unittest.main()
'''
assertEqual(a, b): comprueba que el valor de a es igual al valor de b.
assertNotEqual(a, b): comprueba que el valor de a no es igual al valor de b.
assertTrue(x): comprueba que el valor de x es verdadero.
assertFalse(x): comprueba que el valor de x es falso.
assertIs(a, b): comprueba que a es b (es decir, que son el mismo objeto).
assertIsNot(a, b): comprueba que a no es b (es decir, que no son el mismo objeto).
assertIsNone(x): comprueba que x es None.
assertIsNotNone(x): comprueba que x no es None.
assertIn(a, b): comprueba que a está en la secuencia b.
assertNotIn(a, b): comprueba que a no está en la secuencia b.
assertIsInstance(a, b): comprueba que a es una instancia de la clase b.
assertNotIsInstance(a, b): comprueba que a no es una instancia de la clase b.
assertAlmostEqual(a, b): comprueba que el valor de a es aproximadamente igual al valor de b. Esta aserción se utiliza para comparar números en coma flotante.
assertNotAlmostEqual(a, b): comprueba que el valor de a no es aproximadamente igual al valor de b.
assertGreater(a, b): comprueba que el valor de a es mayor que el valor de b.
assertGreaterEqual(a, b): comprueba que el valor de a es mayor o igual que el valor de b.
assertLess(a, b): comprueba que el valor de a es menor que el valor de b.
assertLessEqual(a, b): comprueba que el valor de a es menor o igual que el valor de b.
assertRaises(exception, callable, *args, **kwargs): comprueba que la llamada a la función callable con los argumentos args y kwargs genera una excepción de tipo exception.
'''
import unittest
import time
from selenium import webdriver

#Hemos de declarar la clase
class TestStringMethods(unittest.TestCase):

#Es la configuración de las pruebas como tal, definimos el webdriver.
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

#Es nuestro test, aquí usamor la variable self.driver para realizar las pruebas que necesitesmos.
    def test1(self):
        self.driver.get("https://demoqa.com/text-box")
        time.sleep(2)

    def test2(self):
        self.driver.get("https://demoqa.com/text-box")
        self.driver.find_element_by_css_selector("#userName").send_keys("Name")
        time.sleep(4)

#El tearDown es para cerrar nuestros test.
    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()
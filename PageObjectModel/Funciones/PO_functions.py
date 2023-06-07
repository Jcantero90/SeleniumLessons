import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class PO_functions():

    def __init__(self,driver):
        self.driver = driver

    #Esto imprime un hola mundo.
    def holaMundo(self):
        print("Hola Mundo desde un PageObjectModel!")

    #Es una prueba de argumentos, no necesitamos enviar el driver.
    def pruebaArgumentos(self,url,selector,nombre):
        self.driver.get(url)
        self.driver.find_element_by_css_selector(selector).send_keys(nombre)

    #definimos una función para el tiempo.
    def timeFunction(self, tim):
        time.sleep(tim)

    #Buscar elemento por selector css
    def GetCssAndSensKeys(self, css):
        val = self.driver.find_element_by_css_selector(css)
        return val

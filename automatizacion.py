#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 12:10:10 2019

@author: rodolfopardo
"""
#Importo las librerias 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests 
import time
from bs4 import BeautifulSoup

#Funcion para comenzar con Google Chrome y busca la etiqueta
def inicia(*args):
       driver = webdriver.Chrome(executable_path="Downloads/chromedriver")
       driver.get(url)
       elem = driver.find_element_by_name('q')
       elem.send_keys(busqueda)
       time.sleep(2)
       elem = driver.find_element_by_name('btnK')
       elem.click()
       driver.maximize_window()
       time.sleep(2)
       driver.save_screenshot("screenshot1.png")
       time.sleep(2)
       driver.minimize_window()
       time.sleep(2)
       print('Usted acaba de visitar ',driver.title, 'a través de ', driver.name)
       driver.close()

#Le pido al usuario que ingrese la busqueda
busqueda = input("Ingrese lo que quiere buscar:")
url = "https://google.com.ar" 

#Llamo a la funcion inicia
inicia(url, busqueda)

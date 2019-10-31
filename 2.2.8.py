import os 
from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)


input1 = browser.find_element_by_css_selector('[name = ''firstname'']')
input1.send_keys("Anton")
input2 = browser.find_element_by_css_selector('[name = ''lastname'']')
input2.send_keys("Shapovalov")
input3 = browser.find_element_by_css_selector('[name = ''email'']')
input3.send_keys("v")

#current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
#file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
#element.send_keys(file_path)
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))

button = browser.find_element_by_css_selector("button.btn")
button.click()

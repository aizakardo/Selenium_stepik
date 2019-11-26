import os 
from selenium import webdriver
import time 
import math
#import os


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
#file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла, т.к. файл должен лежать в той же директории, что и исполняемый
#element.send_keys(file_path)

browser.find_element_by_id('file').send_keys('C:\\test.txt')

button = browser.find_element_by_css_selector("button.btn")
button.click()
time.sleep(5)
browser.quit()

# В этом задании в форме регистрации требуется загрузить текстовый файл.

#   Напишите скрипт, который будет выполнять следующий сценарий:
# 1. Открыть страницу http://suninjuly.github.io/file_input.html
# 2. Заполнить текстовые поля: имя, фамилия, email
# 3. Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# 4. Нажать кнопку "Submit"
# Если все сделано правильно и быстро, вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.
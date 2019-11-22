from selenium import webdriver
import math
import time

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)

button1 = browser.find_element_by_css_selector('.btn')
button1.click()

confirm = browser.switch_to.alert
confirm.accept()

x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

button2 = browser.find_element_by_css_selector('.btn')
button2.click()

answer = browser.find_element_by_css_selector('#answer')
answer.send_keys(y)

#   В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
# 1. Открыть страницу http://suninjuly.github.io/alert_accept.html
# 2. Нажать на кнопку
# 3. Принять confirm
# 4. На новой странице решить капчу для роботов, чтобы получить число с ответом
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом.
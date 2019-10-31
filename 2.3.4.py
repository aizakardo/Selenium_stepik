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
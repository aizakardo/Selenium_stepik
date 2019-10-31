from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

treasure = browser.find_element_by_css_selector('#treasure')
x = treasure.get_attribute('valuex')

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

answer = browser.find_element_by_css_selector('#answer')
answer.send_keys(y)

option1 = browser.find_element_by_css_selector('#robotCheckbox')
option1.click()

option2 = browser.find_element_by_css_selector('#robotsRule')
option2.click()

button = browser.find_element_by_css_selector('.btn')
button.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
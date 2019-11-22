from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

answer = browser.find_element_by_css_selector('#answer')
answer.send_keys(y)

option1 = browser.find_element_by_css_selector("[for = 'robotCheckbox']")
option1.click()

option2 = browser.find_element_by_css_selector("[for = 'robotsRule']")
option2.click()

button = browser.find_element_by_css_selector('.btn')
button.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()

#   Ваша программа должна выполнить следующие шаги:

# 1. Открыть страницу http://suninjuly.github.io/math.html.
# 2. Считать значение для переменной x.
# 3. Посчитать математическую функцию от x (код для этого приведён ниже).
# 4. Ввести ответ в текстовое поле.
# 5. Отметить checkbox "I'm the robot".
# 6. Выбрать radiobutton "Robots rule!".
# 7. Нажать на кнопку Submit.
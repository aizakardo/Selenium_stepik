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

# В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, как и в прошлом задании. Но теперь значение переменной х спрятано в "сундуке", точнее, значение хранится в атрибуте valuex у картинки с изображением сундука.

#   Ваша программа должна:
# 1. Открыть страницу http://suninjuly.github.io/get_attribute.html.
# 2. Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# 3. Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# 4. Посчитать математическую функцию от x (сама функция остаётся неизменной).
# 5. Ввести ответ в текстовое поле.
# 6. Отметить checkbox "I'm the robot".
# 7. Выбрать radiobutton "Robots rule!".
# 8. Нажать на кнопку "Submit".
# Для вычисления значения выражения в п.4 используйте функцию calc(x) из предыдущей задачи.
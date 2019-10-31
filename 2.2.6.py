from selenium import webdriver
import time
import math

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

button = browser.find_element_by_css_selector('.btn')

answer = browser.find_element_by_css_selector('#answer')
answer.send_keys(y)

option1 = browser.find_element_by_css_selector("[for = 'robotCheckbox']")
option1.click()

option2 = browser.find_element_by_css_selector("[for = 'robotsRule']")
browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
option2.click()


#Для этой задачи вам понадобится использовать метод execute_script, чтобы сделать прокрутку в область видимости элементов, перекрытых футером.
button.click()
# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
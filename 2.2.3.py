from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element_by_css_selector('#num1')
num2 = browser.find_element_by_css_selector('#num2')

x = num1.text
y = num2.text

answer = str(int(x) + int(y))

#browser.find_element_by_css_selector('#dropdown').click()
#browser.find_element_by_css_selector("[value='select']").click()

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_tag_name("#dropdown"))
select.select_by_value(answer) # ищем элемент с текстом "Python"

button = browser.find_element_by_css_selector('.btn')
button.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
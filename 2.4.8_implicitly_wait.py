from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

book = browser.find_element_by_id('book')
price = WebDriverWait(browser, 10).until(
  EC.text_to_be_present_in_element((By.ID, "price"),'$100')
)
book.click()
x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
y = calc(x)
answer = browser.find_element_by_css_selector('#answer')
answer.send_keys(y)

button2 = browser.find_element_by_css_selector('#solve')
button2.click()

time.sleep(5)
browser.quit()
#   В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
# 1. Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# 2. Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# 3. Нажать на кнопку "Book"
# 4. Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
# 
# Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.
# Если все сделано правильно и быстро, то вы увидите окно с числом.

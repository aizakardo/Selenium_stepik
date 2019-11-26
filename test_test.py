import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()
number = '897'
link = "https://stepik.org/lesson/236905/step/1"
browser.get(link)
answer = math.log(int(time.time()))
browser.implicitly_wait(3)
area = browser.find_element_by_css_selector(".textarea")
area.send_keys(str(answer))
button = browser.find_element_by_css_selector(".submit-submission")
button.click()
text = browser.find_element_by_css_selector(".smart-hints__hint")
correct_text = text.text
b = str(correct_text)
assert b == "Correct!", print(f" got {b}")
time.sleep(6)
browser.quit()
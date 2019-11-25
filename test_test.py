import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()
number = '897'
link = "https://stepik.org/lesson/236903/step/1"
browser.get(link)

browser.implicitly_wait(3)

# area = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, ".textarea"))

area = browser.find_element_by_css_selector(".textarea")
answer = math.log(int(time.time()))
area.send_keys(str(answer))
button = browser.find_element_by_css_selector(".submit-submission")
button.click()
time.sleep(10)
browser.quit()

find_text = browser.find_element_by_css_selector(".smart-hints__hint")
assert find_text.text == "Correct"
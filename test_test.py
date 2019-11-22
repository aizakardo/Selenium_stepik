import pytest
import time
import math
from selenium import webdriver

browser = webdriver.Chrome()
number = '895'
link = f"https://stepik.org/lesson/236{number}/step/1"
browser.get(link)

#browser.implicitly_wait(3)

area = browser.find_element_by_css_selector(".textarea")
answer = int(math.log(int(time.time())))
area.send_keys(answer)
button = browser.find_element_by_css_selector(".submit-submission")
button.click()
time.sleep(10)
browser.quit()
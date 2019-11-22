import pytest
import time
import math
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number', ["895", "896", "897", "898", "899", "903", "904", "905"])
def test_guest_should_see_login_link(browser, number):
#   link = f"http://selenium1py.pythonanywhere.com/{language}/"
    link = f"https://stepik.org/lesson/236{number}/step/1"
    browser.get(link)
    answer = math.log(int(time.time()))
    area = browser.find_element_by_css_selector(".textarea")
    area.send_keys(answer)
    browser.find_element_by_css_selector(".submit-submission")

   

answer = math.log(int(time.time()))
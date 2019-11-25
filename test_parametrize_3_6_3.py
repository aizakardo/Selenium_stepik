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

@pytest.mark.parametrize('number', ["895", "896", "897","898", "899", "903", "904", "905"]) #
def test_guest_should_see_login_link(browser, number):
#   link = f"http://selenium1py.pythonanywhere.com/{language}/"
    link = f"https://stepik.org/lesson/236{number}/step/1"
    browser.get(link)
    answer = math.log(int(time.time()))
    browser.implicitly_wait(3)
    area = browser.find_element_by_css_selector(".textarea")
    area.send_keys(str(answer))
    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()
    text = browser.find_element_by_css_selector(".smart-hints__hint")
    correct_text = text.text
    correct = "Correct!"
    assert correct_text == correct, print(f" got {correct_text}")
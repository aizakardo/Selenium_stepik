import unittest
import time
from selenium import webdriver

class unittest(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector('div.first_block input.first')
        input1.send_keys("Anton")
        input2 = browser.find_element_by_css_selector('div.first_block input.second')
        input2.send_keys("Anton")
        input3 = browser.find_element_by_css_selector('div.first_block input.third')
        input3.send_keys("Anton")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Text doesn`t match")
        
    def test_abs2(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector('div.first_block input.first')
    #input1 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder=''Input your first name'']')
    #input1 = browser.find_element_by_partial_link_text(Input_your_first_name)
    input1.send_keys("Anton")
    input2 = browser.find_element_by_css_selector('div.first_block input.second')
    input2.send_keys("Anton")
    input3 = browser.find_element_by_css_selector('div.first_block input.third')
    input3.send_keys("Anton")


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
        
if __name__ == "__main__":
    unittest.main()
    assertEqual 



try: 


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
from selenium import webdriver
import time 
link = "http://suninjuly.github.io/simple_form_find_task.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_tag_name('div input')
    print("inp1")
    input1.send_keys("Anton")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Shapovalov")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Moscow")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# Вам нужно открыть страницу по ссылке и заполнить форму на этой странице с помощью Selenium.
# Если всё сделано правильно, то вы увидите окно с проверочным кодом. 
# Это число вам нужно ввести в качестве ответа в этой задаче.
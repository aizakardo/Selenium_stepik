from selenium import webdriver
import time 
link = "http://suninjuly.github.io/find_xpath_form"
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
    button = browser.find_element_by_xpath("//div[6]/button[3]")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# На странице http://suninjuly.github.io/find_xpath_form вы найдете такую же форму регистрации, как в шаге 3, при этом в нее добавилась куча одинаковых кнопок отправки. 
# Но сработает только кнопка с текстом "Submit", и наша задача нажать в коде именно на неё. 

#   Ваши шаги: 
# 1. В коде из шага 4 замените ссылку на  http://suninjuly.github.io/find_xpath_form.
# 2. Подберите уникальный XPath-селектор так, чтобы он находил только кнопку с текстом Submit. XPath можете формулировать как угодно (по тексту, по структуре, по атрибутам) - главное, чтобы он работал.
# 3. Модифицируйте код из шага 3 таким образом, чтобы поиск кнопки происходил с помощью XPath.
# 4. Запустите ваш код.
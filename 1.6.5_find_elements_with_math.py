from selenium import webdriver
import time 
import math
link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()
browser.get(link)
x = str(math.ceil(math.pow(math.pi, math.e)*10000))  
link1 = browser.find_element_by_partial_link_text(x)
link1.click()
try:
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

#   На указанной ниже странице вам нужно найти зашифрованную ссылку и кликнуть по ней:

# 1. Добавьте в самый верх своего кода import math
# 2. Добавьте команду в код, которая откроет страницу: http://suninjuly.github.io/find_link_text
# 3. Добавьте команду, которая найдет ссылку с текстом. Текст ссылки, который нужно найти, зашифрован формулой: 
#     str(math.ceil(math.pow(math.pi, math.e)*10000))
#     (можно вставить данное выражение в свой код, а можно выполнить в интерпретаторе, скопировать оттуда результат и уже его использовать в вашем коде) 

# 4. Добавьте команду для клика по найденной ссылке: она перенесет вас на форму регистрации
# 5. Заполните скриптом форму так же как вы делали в предыдущем шаге урока
# 6. После успешного заполнения вы получите код - отправьте его в качестве ответа на это задание

from selenium import webdriver

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait2.html")

button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text

# Какую ошибку вы увидите в консоли, если попытаетесь выполнить команду browser.find_element_by_id("button") после открытия страницы http://suninjuly.github.io/cats.html?
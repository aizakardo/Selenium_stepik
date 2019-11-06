import unittest
import time
from selenium import webdriver

class TestSum(unittest.TestCase):

    def test_case1(self):
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
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Error on test_2")
        
    def test_case2(self):
        link = "http://suninjuly.github.io/registration1.html"
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
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Error on test_2")
            
if __name__ == "__main__":
    unittest.main()
    print("Everything passed")  

    #time.sleep(10)
     #   browser.quit()
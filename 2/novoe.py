from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

class Test_name(unittest.TestCase):
    
    def test_name1(self):
        input1= browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
        self.assertEqual("First name", 'input1', "ЧЕТ НЕ ТО")#должно быть', 'что есть', 'что произошло')
        
        input1.send_keys("First name")
        button = browser.find_element(By.CSS_SELECTOR, ("button.btn"))
        button.click()

    def test_name2(self):
        input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
        self.assertEqual("Last name", 'input2', "ЧЕТ НЕ ТО")#должно быть', 'что есть', 'что произошло')
        
        input2.send_keys("Last name")
        button = browser.find_element(By.CSS_SELECTOR, ("button.btn"))
        button.click()


    def test_name3(self):
        input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]') 
        self.assertEqual("Email", 'input3', "ЧЕТ НЕ ТО")
        input3.send_keys("Email")
        button = browser.find_element(By.CSS_SELECTOR, ("button.btn"))
        button.click()   

if __name__ == '__main__':
    unittest.main()

    time.sleep(1)
        
welcome_text = browser.find_element_by_tag_name("h1").text

    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()

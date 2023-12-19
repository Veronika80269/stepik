from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1= browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
    input1.send_keys("First name")

    input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
    input2.send_keys("Last name")

    input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
    input3.send_keys("Email")

    for element in elements:
        element.send_keys("Test text")
    
   
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ("button.btn"))
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = browser.find_element_by_tag_name("h1").text
    
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
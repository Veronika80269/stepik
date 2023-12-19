from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

name = browser.find_element(By.NAME,"firstname")
name.send_keys("Ivanov")

last_name = browser.find_element(By.NAME,"lastname")
last_name.send_keys("Ivan")

email= browser.find_element(By.NAME,"email")
email.send_keys("pochta")

# получаем путь к директории текущего исполняемого скрипта nika2.py
current_dir = os.path.abspath(os.path.dirname(__file__))
# имя файла, который будем загружать на сайт из задания
text_name ="text.txt"

# получаем путь к file_text.txt
file_path = os.path.join(current_dir, text_name)
#выбираем на сайте кнопку"Выбрать файл"
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
# отправляем файл
element.send_keys(file_path)


button = browser.find_element(By.TAG_NAME, 'button')
button.click()

time.sleep(30)
browser.quit()





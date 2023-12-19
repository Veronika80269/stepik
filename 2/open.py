from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
 return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)

button= browser.find_element(By.TAG_NAME, "button")
button.click()

confirm = browser.switch_to.alert#переключиться на окно с alert
confirm.accept()#согласиться с сообщением,отказ-confirm.dismiss()

x_element=browser.find_element(By.ID,"input_value")
x = x_element.text
y=calc(x)

input= browser.find_element(By.ID, "answer")
input.send_keys(y) #значение без кавычек

button2= browser.find_element(By.TAG_NAME, "button")
button2.click()







time.sleep(30)
browser.quit()

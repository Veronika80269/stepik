from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
 return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.TAG_NAME,"button")
button.click()

new_window = browser.window_handles[1]#браузере  открыто две вкладки, выбираем 2 вкладку:
browser.switch_to.window(new_window) #Для переключения на новую вкладку в браузере

x_element = browser.find_element(By.ID,"input_value")
x=x_element.text
y=calc(x)

input=browser.find_element(By.ID,"answer")
input.send_keys(y)

button = browser.find_element(By.TAG_NAME,"button")
button.click()



time.sleep(30)
browser.quit()


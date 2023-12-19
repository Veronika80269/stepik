from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
 return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element(By.ID, "input_value")
x=x_element.text
y=calc(x)

browser.execute_script("window.scrollBy(0, 120);")

text=browser.find_element(By.ID, "answer")
text.send_keys(y)

option1 = browser.find_element(By.ID, "robotCheckbox")
option1.click()

option2 = browser.find_element(By.ID, "robotsRule")
option2.click()

button = browser.find_element(By.TAG_NAME, "button")
button.click()



time.sleep(30)
browser.quit()

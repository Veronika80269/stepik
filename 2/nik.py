from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
 return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
y.send_keys("Число")


time.sleep(30)
browser.quit()

# не забываем оставить пустую строку в конце файла
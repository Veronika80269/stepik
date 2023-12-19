from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)


x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

text=browser.find_element(By.ID, "answer")
text.send_keys(y)

#успеваем скопировать код за 30 секунд
time.sleep(30)
browser.quit()
#не забываем оставить пустую строку в конце файла
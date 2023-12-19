from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def sum (x, y):
 return str(int(x)+int(y))

link = "http://suninjuly.github.io/selects2.html"

browser = webdriver.Chrome()
browser.get(link)

x_element= browser.find_element(By.ID, "num1")
x=x_element.text
y_element= browser.find_element(By.ID, "num2")
y=y_element.text
sum=(int(x))+int(y)

sum1=str(sum)

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(sum1) 

button=browser.find_element(By.CLASS_NAME, "btn-default")
button.click()

    # успеваем скопировать код за 30 секунl
time.sleep(30)
browser.quit()

# не забываем оставить пустую строку в конце файла
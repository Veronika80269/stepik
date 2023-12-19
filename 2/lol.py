from re import X
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
 return 


link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, "treasure")
x = x_element.get_attribute("valuex")
y=calc(x)
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value("1") # ищем элемент с текстом "Python"

time.sleep(30)
browser.quit()
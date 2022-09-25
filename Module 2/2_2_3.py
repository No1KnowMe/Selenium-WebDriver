from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/selects1.html'
browser.get(link)

try:
    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text
    answer = int(num1) + int(num2)

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(answer))

    browser.find_element(By.CLASS_NAME, 'btn.btn-default').click()

finally:
    time.sleep(10)
    browser.quit()
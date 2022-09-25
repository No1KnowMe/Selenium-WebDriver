from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/get_attribute.html'
browser.get(link)


def calc(x):
    return math.log(abs(12*math.sin(int(x))))


try:
    x = browser.find_element(By.ID, 'treasure').get_attribute('valuex')

    input_value = browser.find_element(By.ID, 'answer')
    input_value.send_keys(calc(x))

    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CLASS_NAME, 'btn.btn-default').click()

finally:
    time.sleep(10)
    browser.quit()
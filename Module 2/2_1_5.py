from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time


def calc(x):
    return math.log(abs(12*math.sin(int(x))))


link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element(By.CSS_SELECTOR, '#input_value').text

try:
    answer = calc(x)

    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(answer)

    checkbox = browser.find_element(By.CSS_SELECTOR, '[type=checkbox]')
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, '[value=robots]')
    radiobutton.click()
    
    submit = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()

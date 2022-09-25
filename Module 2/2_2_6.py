from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/execute_script.html'
browser.get(link)


def calc(x):
    return math.log(abs(12*math.sin(int(x))))


try:
    x = browser.find_element(By.ID, 'input_value').text

    input_value = browser.find_element(By.ID, 'answer')
    input_value.send_keys(calc(x))

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    radiobutton = browser.find_element(By.ID, 'robotsRule')
    button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')

    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    radiobutton.click()
    button.click()

finally:
    time.sleep(10)
    browser.quit()
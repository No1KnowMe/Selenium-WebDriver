from selenium import webdriver
from selenium.webdriver.common.by import By
import os, time

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'
browser.get(link)

try:
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    first_name = browser.find_element(By.CSS_SELECTOR, '[name=firstname]')
    first_name.send_keys('First')

    last_name = browser.find_element(By.CSS_SELECTOR, '[name=lastname]')
    last_name.send_keys('Last')

    email = browser.find_element(By.CSS_SELECTOR, '[name=email]')
    email.send_keys('Email')

    input_file = browser.find_element(By.ID, 'file')
    input_file.send_keys(file_path)

    button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    button.click()

finally:
    time.sleep(10)
    browser.quit()

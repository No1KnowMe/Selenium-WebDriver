from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, math

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'
browser.get(link)

try:
    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    submit_button = browser.find_element(By.ID, 'book')
    submit_button.click()

    x = browser.find_element(By.ID, 'input_value').text
    answer = math.log(abs(12 * math.sin(int(x))))

    browser.find_element(By.ID, 'answer').send_keys(answer)
    browser.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()

finally:
    time.sleep(10)
    browser.quit()
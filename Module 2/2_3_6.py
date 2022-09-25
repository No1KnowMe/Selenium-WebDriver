from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'
browser.get(link)

try:
    browser.find_element(By.TAG_NAME, 'button').click()
    second_page = browser.window_handles[1]
    browser.switch_to.window(second_page)

    x = browser.find_element(By.ID, 'input_value').text
    answer = math.log(abs(12*math.sin(int(x))))

    browser.find_element(By.ID, 'answer').send_keys(answer)
    browser.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()

finally:
    time.sleep(10)
    browser.quit()
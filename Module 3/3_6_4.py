import pytest, math, time
from selenium import webdriver
from selenium.webdriver.common.by import By

# answer = math.log(int(time.time() + 19.34))
links = ['https://stepik.org/lesson/236895/step/1',
         'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1',
         'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1',
         'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1',
         'https://stepik.org/lesson/236905/step/1']


class TestClass:
    @pytest.mark.parametrize('link_url', links)
    def test_1(self, browser, link_url):
        link = f'{link_url}'
        browser.get(link)
        inp_answer = browser.find_element(By.CSS_SELECTOR, 'div > textarea')
        answer = math.log(int(time.time()))
        inp_answer.send_keys(answer)
        button = browser.find_element(By.CLASS_NAME, 'submit-submission')
        button.click()
        assert browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text == 'Correct!'
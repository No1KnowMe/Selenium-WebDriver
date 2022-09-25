from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import unittest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


def fill_form(link):
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
    input3.send_keys("erge@gmail.com")

    time.sleep(1)

    '''button = browser.find_element_by_css_selector("button.btn")
    button.click()'''

    btn = browser.find_element(By.CSS_SELECTOR, "[class='btn btn-default']")
    btn.click()

    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(browser.find_element_by_tag_name("h1").text)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    return str(browser.find_element_by_tag_name("h1").text)


class TestReg(unittest.TestCase):
    def test_link1(self):
        self.assertEqual(fill_form(link1), "Congratulations! You have successfully registered!",
                         "RRRRegistration is failed")

    def test_link2(self):
        self.assertEqual(fill_form(link2), "Congratulations! You have successfully registered!",
                         "Registration is failed")


if __name__ == "__main__":
    unittest.main()
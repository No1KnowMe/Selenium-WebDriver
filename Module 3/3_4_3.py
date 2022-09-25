import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

link = 'http://selenium1py.pythonanywhere.com/'


@pytest.fixture
def browser():
    print('\nStart browser for test...')
    browser = webdriver.Chrome()
    return browser


class TestPage1:
    # вызываем фикстуру в тесте, передав её как параметр
    def test_quest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '#login_link')

    def test_quest_should_see_basket_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '.basket-mini .btn-group > a')
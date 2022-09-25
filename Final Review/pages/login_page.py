from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def register_new_user(email, password):
        email = str(time.time()) + "@fakemail.org"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        print(self.browser.current_url)
        assert LoginPageLocators.LOGIN_URL in self.browser.current_url, "This is not login link"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "There is no login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "There is no register form"

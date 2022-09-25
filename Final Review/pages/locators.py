from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_URL = "login"
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators:
    ADD_TO_CART_BTN = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    ADDED_TO_CART_PRODUCT = (By.CSS_SELECTOR, ".alertinner > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > p")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
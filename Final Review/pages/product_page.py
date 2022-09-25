from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
        add_to_cart_btn.click()

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    def should_be_product_page(self):
        assert self.add_to_cart(), "This is not a product page"

    def should_be_same_product(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text \
               == self.browser.find_element(*ProductPageLocators.ADDED_TO_CART_PRODUCT).text, \
            "Not the same product"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_TO_CART_PRODUCT), \
            "Success message is presented, but should not be"

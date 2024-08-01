from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    def open(self):
        self.open_url('https://www.target.com/cart')


class CartPage(Page):
    CART_EMPTY_MSG = (By.XPATH, "//h1[text()='Your cart is empty']")

    def verify_cart_empty(self):
        self.wait_for_element_appear(*self.CART_EMPTY_MSG)
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)

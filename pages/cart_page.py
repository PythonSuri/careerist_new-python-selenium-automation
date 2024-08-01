from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):

    CART_EMPTY_MSG = (By.XPATH, "//h1[text()='Your cart is empty']")
    CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

    def open(self):
        self.open_url('https://www.target.com/cart')

    def verify_cart_empty(self):
        self.wait_for_element_appear(*self.CART_EMPTY_MSG)
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)

    def verify_product_name(self):
        self.wait_for_element_appear(*self.CART_ITEM_TITLE)
        self.wait_for_element_appear(*self.CART_SUMMARY)

    def verify_cart_items(self):
        self.wait_for_element_appear(*self.CART_SUMMARY)



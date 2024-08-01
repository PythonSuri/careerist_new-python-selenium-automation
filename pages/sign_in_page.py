from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SignInPage(Page):
    SIGN_IN_MSG = (By.XPATH, "//span[text()='Sign into your Target account']")

    def verify_sign_in_form(self):
        self.wait_for_element_appear(*self.SIGN_IN_MSG)
        self.verify_text('Sign into your Target account', *self.SIGN_IN_MSG)

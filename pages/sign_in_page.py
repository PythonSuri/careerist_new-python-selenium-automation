from selenium.webdriver.common.by import By

from pages.base_page import Page

from time import sleep


class SignInPage(Page):
    SIGN_IN_MSG = (By.XPATH, "//span[text()='Sign into your Target account']")
    TOS_LINK = (By.XPATH, "//a[text()='Target terms and conditions']")

    def verify_sign_in_form(self):
        self.wait_for_element_appear(*self.SIGN_IN_MSG)
        self.verify_text('Sign into your Target account', *self.SIGN_IN_MSG)

    def click_tos_link(self):
        self.click(*self.TOS_LINK)
from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_MSG = (By.XPATH, "//span[text()='Sign into your Target account']")
    TOS_LINK = (By.XPATH, "//a[text()='Target terms and conditions']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "[inputmode='email'][name='username']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[id='password'][name='password']")
    EMAIL = 'testing_fake@aol.com' # => INVALID EMAIL
            # USE VALID EMAIL for Positive Scenario
    PASSWORD = 'Password1'         # => INVALID PASSWORD
            # USE VALID PASSWORD for Positive Scenario
    SIGN_IN_W_PSW_BTN = (By.CSS_SELECTOR, "[id='login'][type='submit']")
    LOGIN_ERR_MSG = (By.CSS_SELECTOR, "[data-test='authAlertDisplay']")
    USER_WELCOME_MSG = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")

    def verify_sign_in_form(self):
        self.wait_for_element_appear(*self.SIGN_IN_MSG)
        self.verify_text('Sign into your Target account', *self.SIGN_IN_MSG)

    def click_tos_link(self):
        self.click(*self.TOS_LINK)

    def enter_credentials(self):
        self.input_text(self.EMAIL, *self.EMAIL_FIELD)
        self.input_text(self.PASSWORD, *self.PASSWORD_FIELD)

    def click_sign_in_w_password(self):
        self.wait_and_click(*self.SIGN_IN_W_PSW_BTN)

    def verify_login_error_msg(self):
        self.wait_for_element_appear(*self.LOGIN_ERR_MSG)
        self.verify_text("We can't find your account.", *self.LOGIN_ERR_MSG)

    def verify_logged_user(self):
        self.wait_for_element_appear(*self.USER_WELCOME_MSG)
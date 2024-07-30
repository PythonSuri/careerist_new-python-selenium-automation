from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then
from selenium.webdriver.common.by import By
from time import sleep


SIGN_IN_BTN = (By.CSS_SELECTOR, "[aria-label='Account, sign in']")
SIDE_NAV_SIGN_IN_BTN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
SIGN_IN_FORM = (By.XPATH, "//span[text()='Sign into your Target account']")

@when('Click on Sign In')
def click_sign_in(context):
    context.driver.find_element(*SIGN_IN_BTN).click()
    context.driver.wait.until(EC.visibility_of_element_located(SIDE_NAV_SIGN_IN_BTN))


@when('From right side navigation menu click Sign In')
def click_side_nav(context):
    context.driver.find_element(*SIDE_NAV_SIGN_IN_BTN).click()
    context.driver.wait.until(EC.visibility_of_element_located(SIGN_IN_FORM))
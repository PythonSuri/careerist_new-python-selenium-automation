from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on Sign In')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//span[@class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']").click()
    sleep(4)


@when('From right side navigation menu click Sign In')
def click_side_nav(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
    sleep(4)
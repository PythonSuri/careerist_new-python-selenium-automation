from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import then, when

from time import sleep


CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


@when('Open cart page')
def open_cart(context):
    context.app.cart_page.open()


@then('Verify cart contains correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
    context.driver.wait.until(EC.visibility_of_element_located(CART_SUMMARY))
    print(f'Actual product in cart: {context.product_name}')
    assert context.product_name in actual_name, f'Expected {context.product_name} but got {actual_name}'


@then('Verify cart contains {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert amount in cart_summary, f'Expected {amount} items but got {cart_summary}'


@then('Verify Your cart is empty message is shown')
def verify_cart_message(context):
    context.app.cart_page.verify_cart_empty()


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1").text
    assert expected_text == actual_text, f'Expected {expected_text} did not match actual {actual_text}'


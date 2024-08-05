from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then

from selenium.webdriver.common.by import By
from time import sleep


#@given('Open Sign In page')
#def open_sign_in_page(context):
#    context.app.sign_in_page.open_sign_in_page()


@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.sign_in_page.get_current_window()


@when('Click on Target terms and conditions link')
def click_tos_link(context):
    context.app.sign_in_page.click_tos_link()


@when('Switch to the newly opened window')
def switch_window(context):
    context.app.sign_in_page.switch_to_new_window()


@then('Verify Terms and Conditions page is opened')
def verify_tos_opened(context):
    context.app.terms_and_conditions_page.verify_tos_url()


@then('Close a new window and switch back to original')
def close_new_and_switch_to_original_window(context):
    context.app.terms_and_conditions_page.close()
    context.app.terms_and_conditions_page.switch_to_window_by_id(context.original_window)


@when('Click on Sign In')
def click_sign_in_icon(context):
    context.app.header.click_sign_in_icon()


@when('From right side navigation menu click Sign In')
def click_side_nav_icon(context):
    context.app.header.click_side_nav_icon()


@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    context.app.sign_in_page.verify_sign_in_form()








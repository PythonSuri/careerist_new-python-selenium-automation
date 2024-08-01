from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then

from selenium.webdriver.common.by import By
from time import sleep


@when('Click on Sign In')
def click_sign_in_icon(context):
    context.app.header.click_sign_in_icon()


@when('From right side navigation menu click Sign In')
def click_side_nav_icon(context):
    context.app.header.click_side_nav_icon()


@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    context.app.sign_in_page.verify_sign_in_form()





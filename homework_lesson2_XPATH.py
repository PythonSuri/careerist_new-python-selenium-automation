# Homework Lesson 2 - Workshop - Homework

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()

service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

#-------------------------------------------------------------------------------------------------
# Task 1 - Practice with Locators
driver.refresh()
# Create locators + search strategy for these page elements of Amazon Sign in page:

# Amazon logo
# Email field
# Continue button
# Conditions of use link
# Privacy Notice link
# Need help link
# Forgot your password link
# Other issues with Sign-In link
# Create your Amazon account button

# Hint:
# Email field, search by ID, “ap_email”

# open the url
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

# Amazon logo
driver.find_element(By.XPATH,"//a[@class='a-link-nav-icon']")

# Email field
driver.find_element(By.XPATH, "//input[@aria-describedby='Enter your email or mobile phone number']")
driver.find_element(By.ID,'ap_email')

# Continue button
driver.find_element(By.XPATH, "//input[@aria-labelledby='continue-announce']")
driver.find_element(By.ID,'continue')

# Conditions of use link
driver.find_element(By.XPATH,"//a[text()='Conditions of Use']")

# Privacy Notice link
driver.find_element(By.XPATH,"//a[text()='Privacy Notice']")

# Need help link
driver.find_element(By.XPATH,"//*[@class='a-expander-prompt']")

# Forgot your password link
driver.find_element(By.XPATH,"//*[@class='a-link-normal']")
driver.find_element(By.XPATH,"//a[@id='auth-fpp-link-bottom']")

# Other issues with Sign-In link
driver.find_element(By.XPATH,"//a[@id='ap-other-signin-issues-link']")

# Create your Amazon account button
driver.find_element(By.XPATH,"//a[@id='createAccountSubmit']")
driver.find_element(By.XPATH,"//span[@id='auth-create-account-link']")

sleep(9)
print('Test passed')

#-------------------------------------------------------------------------------------------------
# Task 2 - Create a Test Case

# Create a test case for the SignIn page using python & selenium script.
# (Make sure to use Incognito browser mode when searching for locators)

# Test Case: Users can navigate to SignIn page
driver.refresh()

# 1. Open https://www.target.com/
driver.get('https://www.target.com')

# 2. Click SignIn button
driver.find_element(By.XPATH,"//span[@class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']").click()

sleep(2)

# 3. Click SignIn from side navigation
driver.find_element(By.XPATH,"//a[@data-test='accountNav-signIn']").click()

# 4. Verify SignIn page opened:
# “Sign into your Target account” text is shown,
# SignIn button is shown (you can just use driver.find_element()
# to check for element’s presence, no need to assert here)

expected_text = 'Sign into your Target account'
sleep(2)
actual_text = driver.find_element(By.XPATH,"//span").text
print(actual_text)

assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'
print('Test case passed')

sleep(2)



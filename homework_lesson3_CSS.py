# Homework Lesson 3 - Workshop - Homework

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()

service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.refresh()

#-------------------------------------------------------------------------------------------------
# Task 1 - Practice with Locators

# Find the most optimal locators for Create Account on amazon.com (Registration) page elements:

# Amazon logo
# Create account
# Your name placeholder
# Mobile number or email placeholder
# Password placeholder
# Password must be at least 6 characters
# Re-enter password placeholder
# Continue button
# Conditions of Use link
# Privacy Notice link
# Sign in link

# open the url
driver.get('https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&webAuthnChallengeIdForAutofill=x9yzX72Vu6SP9uBjhOJ_ad3lvAjiJdtS%3ANA&webAuthnGetParametersForAutofill=eyJycElkIjoiYW1hem9uLmNvbSIsImNoYWxsZW5nZSI6Ing5eXpYNzJWdTZTUDl1QmpoT0pfYWQzbHZBamlKZHRTIiwidGltZW91dCI6OTAwMDAwLCJhbGxvd0NyZWRlbnRpYWxzIjpudWxsLCJtZWRpYXRpb24iOiJjb25kaXRpb25hbCIsInVzZXJWZXJpZmljYXRpb24iOiJwcmVmZXJyZWQifQ%3D%3D&pageId=usflex&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcss%2Fhomepage.html%3Fref_%3Dnav_ya_signin&prevRID=G2243SBSN8MCBSQNN8R1&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

# Amazon logo
driver.find_element(By.CSS_SELECTOR, "[aria-label='Amazon'].a-icon-logo.a-icon")
driver.find_element(By.CSS_SELECTOR,"[aria-label='Amazon'][role='img']")
driver.find_element(By.CSS_SELECTOR,".a-icon[aria-label='Amazon']")
driver.find_element(By.CSS_SELECTOR, ".a-icon-logo.a-icon")
driver.find_element(By.CSS_SELECTOR, ".a-link-nav-icon")

# Create account
driver.find_element(By.CSS_SELECTOR, ".a-spacing-small")

# Your name placeholder
driver.find_element(By.CSS_SELECTOR, "[placeholder='First and last name'][type='text']")
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")
driver.find_element(By.CSS_SELECTOR, "input#ap_customer_name")

# Mobile number or email placeholder
driver.find_element(By.CSS_SELECTOR, "[autocomplete='email'][type='email']")
driver.find_element(By.CSS_SELECTOR, "#ap_email")
driver.find_element(By.CSS_SELECTOR, "input#ap_email")
driver.find_element(By.CSS_SELECTOR,"input.auth-required-field.a-input-text")
driver.find_element(By.CSS_SELECTOR,"input#ap_email.auth-required-field.a-input-text")

# Password placeholder
driver.find_element(By.CSS_SELECTOR, "[placeholder='At least 6 characters'][type='password']")
driver.find_element(By.CSS_SELECTOR, "#ap_password")
driver.find_element(By.CSS_SELECTOR, "input#ap_password")
driver.find_element(By.CSS_SELECTOR,"input#ap_password.auth-required-field.a-input-text")

# Passwords must be at least 6 characters
driver.find_element(By.CSS_SELECTOR, "[aria-live='polite'].auth-inlined-information-message.a-box")
driver.find_element(By.CSS_SELECTOR,".a-alert-inline.a-alert-inline-info.auth-inlined-information-message.a-spacing-top-mini.a-box")

# Re-enter password placeholder
driver.find_element(By.CSS_SELECTOR,".a-span12.auth-required-field.auth-require-fields-match.a-input-text")
driver.find_element(By.CSS_SELECTOR,"input#ap_password_check.a-span12.auth-required-field.auth-require-fields-match.a-input-text")
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")
driver.find_element(By.CSS_SELECTOR, "input#ap_password_check")
driver.find_element(By.CSS_SELECTOR, "[autocomplete='new-password'][type='password']")

# Continue button
driver.find_element(By.CSS_SELECTOR, "#auth-continue-announce")
driver.find_element(By.CSS_SELECTOR, "#auth-continue-announce.a-button-text")

# Conditions of Use link
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")

# Privacy Notice link
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']")

# Sign in link
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")

sleep(2)
print('Test passed')

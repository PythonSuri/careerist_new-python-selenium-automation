from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.refresh()
driver.get('https://www.amazon.coms')

sleep(6)

# find by CSS, using ID:
driver.find_element(By.CSS_SELECTOR,"#twotabsearchtextbox") # driver.find_element(By.ID,'twotabsearchtextbox')
driver.find_element(By.CSS_SELECTOR,"input#twotabsearchtextbox")

# find by CSS, using classes:
driver.find_element(By.CSS_SELECTOR,".nav-input")
driver.find_element(By.CSS_SELECTOR,".nav-progressive-attribute.nav-input")

# find by tag + classes:
driver.find_element(By.CSS_SELECTOR,"input.nav-progressive-attribute.nav-input")

# find by tag + id + classes:
driver.find_element(By.CSS_SELECTOR,"input#twotabsearchtextbox.nav-progressive-attribute.nav-input")

# find by attributes:
driver.find_element(By.CSS_SELECTOR,"[placeholder='Search Amazon']") # $$("[placeholder='Search Amazon']")
driver.find_element(By.CSS_SELECTOR,"[placeholder='Search Amazon'][type='text']")

# find by tag + attributes:
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search Amazon'][type='text']")

# find by tag + #id + .class + [attributes]:
driver.find_element(By.CSS_SELECTOR,"input#twotabsearchtextbox.nav-input[placeholder='Search Amazon'][type='text']")
driver.find_element(By.CSS_SELECTOR,"input[type='text'].nav-input[placeholder='Search Amazon']#twotabsearchtextbox")

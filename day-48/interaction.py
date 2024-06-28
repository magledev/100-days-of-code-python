from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

binaryPath = "/usr/bin/brave"
# binaryPath = "/usr/bin/brave-browser"
driverPath = "/usr/bin/chromedriver"

options = webdriver.ChromeOptions()
options.binary_location = binaryPath
driverService = Service(driverPath)
driver = webdriver.Chrome(service=driverService, options=options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
button = driver.find_element(By.CSS_SELECTOR, "form button")

first_name.send_keys("Bob")
last_name.send_keys("Walton")
email.send_keys("bobbyboy@email.com")
# button.click()

# driver.quit()

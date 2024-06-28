import time
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

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

cookie_time = 1
start = int(time.time())
end = int(start + cookie_time)

while time.time() < end:
    cookie.click()

credits = driver.find_element(By.ID, "money")
time.sleep(0.25)
credits = int((credits.text).replace(",", ""))
print(credits)

item_ids = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_monis = driver.find_elements(By.CSS_SELECTOR, "#store b")
item_prices = [price for price in item_monis[:-1]]
items = [item.get_attribute("id") for item in item_ids[:-1]]

costs = []

for price in item_prices:
    element_text = price.text
    if price != "":
        cost = int(element_text.split("-")[1].strip().replace(",", ""))
        costs.append(cost)

upgrades = {}
for n in range(len(item_prices)):
    upgrades[items[n]] = (costs[n],)

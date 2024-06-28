import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

binaryPath = "/usr/bin/brave"
# binaryPath = "/usr/bin/brave-browser"
driverPath = "/usr/bin/chromedriver"

options = webdriver.ChromeOptions()
options.binary_location = binaryPath
driverService = Service(driverPath)
driver = webdriver.Chrome(service=driverService, options=options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

cookie_time = 300
start = time.time()
end = start + cookie_time
interlude = time.time() + 5

while True:
    cookie.click()
    if time.time() > interlude:
        buyable = []
        store = driver.find_elements(By.CSS_SELECTOR, value="#store div")
        for item in store[:-1]:
            if item.get_attribute('class') != "grayed":
                buyable.append(item)
        buyable[-1].click()
        timeout = time.time() + 5
    if time.time() > end:
        cookie_per_s = driver.find_element(By.ID, value="cps").text
        print(cookie_per_s)
        break
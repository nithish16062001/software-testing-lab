from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome
driver = webdriver.Chrome()

# Open website
driver.get("https://www.saucedemo.com")

# Maximize browser window
driver.maximize_window()

# Enter username
driver.find_element(By.ID, "user-name").send_keys("standard_user")

# Enter password
driver.find_element(By.ID, "password").send_keys("secret_sauce")

# Click Login button
driver.find_element(By.ID, "login-button").click()

# Wait for page to load
time.sleep(3)

# Verify successful login
title = driver.find_element(By.CLASS_NAME, "title").text

if title == "Products":
    print("Title Verified")

if "inventory" in driver.current_url:
    print("Login Successful")
else:
    print("Login Failed")
from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch Chrome Browser
driver = webdriver.Chrome()

# Open Website
driver.get("https://www.flipkart.com")

# Maximize browser window (optional)
driver.maximize_window()

# Count Links
links = driver.find_elements(By.TAG_NAME, "a")
print("Number of Links:", len(links))

# Count Images
images = driver.find_elements(By.TAG_NAME, "img")
print("Number of Images:", len(images))

# Count Buttons
buttons = driver.find_elements(By.TAG_NAME, "button")
print("Number of Buttons:", len(buttons))

# Count Input Fields
inputs = driver.find_elements(By.TAG_NAME, "input")
print("Number of Input Fields:", len(inputs))

# Close Browser
driver.quit()
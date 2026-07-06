from selenium import webdriver

# Connect to Selenium Server
driver = webdriver.Remote(
    command_executor="http://10.101.36.82:4444",
    options=webdriver.ChromeOptions()
)

# Open website
driver.get("https://vaijnanika.in/")

# Print title
print("Title:", driver.title)

# Close browser
driver.quit()
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time

print("--- Initializing Firefox Automation ---")

try:
    # 1. Start the Firefox Driver
    driver = webdriver.Firefox()

    # 2. Navigate to a site
    print("Navigate to GitHub")
    driver.get("https://github.com/josephdo0206")

    # 3. Wait 5 seconds so you can see it work
    print("Handshake Successful. Browser will close in 5 seconds.")
    time.sleep(5)

    # 4. Close the browser
    driver.quit()
    print("Test Complete: Engine and Browser are synced")

except Exception as e:
    print(f"Error detected: {e}")
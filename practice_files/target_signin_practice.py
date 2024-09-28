from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# Create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

try:
    # Step 1: Open the URL
    driver.get('https://www.target.com/')
    sleep(10)

    # Step 2: Click SignIn button
    driver.find_element(By.XPATH, "//span[@class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']").click()
    sleep(10)

    # Step 3: Click SignIn from side navigation
    driver.find_element(By.XPATH, "//span[@class ='sc-859e7637-0 hHZPQy']").click()
    sleep(10)

    # Step 4: Verify SignIn page opened
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, '//span[text()="Sign into your Target account"]'))
    )
    print('Sign In page verified.')

except Exception as e:
    print(f"Error: {e}")
    sleep(20)
    # Close the browser
    driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Set up the ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Open the Amazon sign-in page
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

# wait
wait = WebDriverWait(driver, 10)

# practice locators using XPATH:
# amazon logo
logo = wait.until(EC.presence_of_element_located((By.XPATH, "//i[contains(@class, 'a-icon-logo')]")))

#email field
email_field = driver.find_element(By.XPATH, "//input[@id='ap_email']")

#continue button
continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")

#conditions of use link
conditions_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Conditions of Use']")

#privacy notice link
privacy_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Privacy Notice')]")

#need help link
need_help_link = driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom']")

#forgot your password link
forgot_password_link = driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom']")

#other issues with sign in link
#create your amazon account button

# Close the browser
driver.quit()




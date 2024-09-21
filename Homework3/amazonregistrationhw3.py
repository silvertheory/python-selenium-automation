from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# open the URL
driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

# create a WebDriverWait object
wait = WebDriverWait(driver, 10)

# amazon logo
amazon_logo = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "i.a-icon.a-icon-logo")))

# customer name input field
customer_name_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ap_customer_name")))

# email input field
email_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ap_email")))

# password input field
password_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ap_password")))

# password check input field
password_check_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ap_password_check")))

# continue button
continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#continue")))

# conditions of Use link
conditions_of_use_link = driver.find_element(By.CSS_SELECTOR, 'a[href*="ap_register_notification_condition_of_use"]')

# privacy Notice link
privacy_notice_link = driver.find_element(By.CSS_SELECTOR, 'a[href*="ap_register_notification_privacy_notice"]')

# sign in link
sign_in_link = driver.find_element(By.CSS_SELECTOR, 'a.a-link-emphasis[href*="ap/signin"]')


# driver.quit()
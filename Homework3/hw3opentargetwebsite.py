from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('Click on Cart icon')
def search_product(context):
    # Search field => enter tea
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    # Search button => click
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/CartIcon']").click()
    sleep(5)  # wait for search results page to load


@then('Verify "Your cart is empty" message is shown')
def verify_results(context):
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='sc-fe064f5c-0 dtCtuk']").text
    expected_result = 'tea'
    assert expected_result in actual_result, f'Expected {expected_result}, got actual {actual_result}'


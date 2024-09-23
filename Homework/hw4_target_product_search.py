from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('Search for a product {product_name}')
def search_product(context, product_name):
    # Search field => enter product name (from Behave variable)
    search_field = context.driver.find_element(By.ID, 'search')
    search_field.clear()
    search_field.send_keys(product_name)

    # Search button => click
    search_button = context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    search_button.click()


@then('Verify that correct search results for {product_name} are shown')
def verify_results(context, product_name):
    # Wait for search results page to load
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@data-test='resultsHeading']"))
    )

    # Verify the correct search results are shown
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert product_name.lower() in actual_result.lower(), f'Expected {product_name}, but got {actual_result}'

    assert expected_result in actual_result, f'Expected {expected_result}, got actual {actual_result}'
    print('Test case passed')

    driver.quit()

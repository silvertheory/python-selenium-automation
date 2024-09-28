from selenium.webdriver.common.by import By
from behave import given, when, then

CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')

@when('Search for a product "{product_name}"')
def search_product(context, product_name):
    context.header = Header(context.driver)
    context.header.search_product(product_name)

@when('Select the first product from search results')
def select_first_product(context):
    context.search_results = SearchResultsPage(context.driver)
    context.search_results.select_first_product()

@when('Add the product to the cart')
def add_product_to_cart(context):
    context.product_page = ProductPage(context.driver)
    context.product_page.add_product_to_cart()

@when('Click on the cart icon')
def click_cart_icon(context):
    context.product_page.click_view_cart()  # Assuming the view cart button appears after adding product

@then('Verify the product is in the cart')
def verify_product_in_cart(context):
    context.cart_page = CartPage(context.driver)
    assert context.cart_page.is_product_in_cart(), "Product was not added to the cart!"

@then('Close the browser')
def close_browser(context):
    context.driver.quit()


@then('Verify Cart Empty message shown')
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()


@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
    print(f'Actual product in cart name: {actual_name}')
    assert context.product_name in actual_name, f"Expected {context.product_name} but got {actual_name}"


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"


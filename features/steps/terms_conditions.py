from behave import given, when, then
from pages.target_app_page import TargetAppPage
from pages.header import Header

@given('Open sign in page')
def open_sign_in_page(context):
    context.driver.get('https://www.target.com/login')

@when('Store original window')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle

@when('Click on Target terms and conditions link')
def click_terms_conditions_link(context):
    header = Header(context.driver)
    header.click_terms_conditions_link()  # Assuming you have this method in Header class

@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.driver.switch_to.new_window('window')

@then('Verify Terms and Conditions page opened')
def verify_terms_conditions_page(context):
    expected_url = "https://www.target.com/terms-and-conditions"  # Adjust URL if necessary
    assert context.driver.current_url == expected_url, f"Expected URL to be {expected_url}, but got {context.driver.current_url}"

@then('User can close new window and switch back to original')
def close_new_window_and_switch_back(context):
    context.driver.close()  # Close the new window
    context.driver.switch_to.window(context.original_window)  # Switch back to the original window
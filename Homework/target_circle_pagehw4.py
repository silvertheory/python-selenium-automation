from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open target web page
@given('Open Target Circle page')
def open_circle_page(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify there are {num_cells} benefit cells')
def verify_benefit_cells(context, num_cells):
    # Wait for the benefit cells to load
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'styles__BenefitCell')]"))
    )

    # Find all elements that represent benefit cells
    benefit_cells = context.driver.find_elements(By.XPATH, "//div[contains(@class, 'styles__BenefitCell')]")

    # Verify that the number of benefit cells is equal to num_cells
    assert len(benefit_cells) == int(num_cells), f'Expected {num_cells} benefit cells, but got {len(benefit_cells)}'

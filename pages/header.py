from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class Header(Page):
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    SIGN_IN_BTN = (By.CSS_SELECTOR, "[data-test='@web/SignIn']")

    def search_product(self, item):
        self.input_text(item, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6) # wait for search results page to load

    def click_cart(self):
        self.wait_to_be_clickable_click(*self.CART_BTN)
        # self.driver.find_element(*self.CART_BTN).click()

    def click_sign_in(self):
        self.wait_to_be_clickable(*self.SIGN_IN_BTN)
        sleep(6)

    def click_terms_conditions_link(self):
        TERMS_CONDITIONS_LINK = (By.XPATH, "//a[contains(@class, 'gvPtqx') and text()='Target terms and conditions']")  # Adjust locator as needed
        self.wait_to_be_clickable_click(*TERMS_CONDITIONS_LINK)
        sleep(6)

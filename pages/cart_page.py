from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    CART_EMPTY_MSG = (By.XPATH, "//*[contains(text(),'Your Amazon Cart is empty')]")

    def verify_cart_empty(self, expected_text):
        self.verify_text(expected_text, *self.CART_EMPTY_MSG)
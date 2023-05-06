from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignInPage(Page):
    SIGNIN_HEADING = (By.XPATH, "//*[contains(text(),'Sign in')]")
    def verify_signin_open(self, expected_heading):
        self.verify_heading(expected_heading, *self.SIGNIN_HEADING)
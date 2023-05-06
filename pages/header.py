from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import Page

class Header(Page):
    MAIN_SEARCH_BAR = (By.ID, 'Search-In-Modal')
    SEARCH_BTN = (By.CSS_SELECTOR, 'svg.icon.icon-search.modal__toggle-open')


    def input_search_text(self, text):
        self.input_text(text, *self.MAIN_SEARCH_BAR)

    def click_search(self):
        self.click(*self.SEARCH_BTN)


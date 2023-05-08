from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import Page

class Header(Page):
    MAIN_SEARCH_BAR = (By.CSS_SELECTOR, '#Search-In-Modal')
    # SEARCH_BTN = (By.CSS_SELECTOR, 'svg.icon-search')
    SEARCH_BTN = (By.CSS_SELECTOR, '.header__icons summary.header__icon.header__icon--summary.header__icon--search.focus-inset.modal__toggle svg.icon.icon-search.modal__toggle-open')


    def click_search(self):
        self.click(*self.SEARCH_BTN)


    def input_search_text(self, text):
        self.driver.get('https://shop.cureskin.com/search?q=CureSkin+gel')
        # self.input_text(text, *self.MAIN_SEARCH_BAR)




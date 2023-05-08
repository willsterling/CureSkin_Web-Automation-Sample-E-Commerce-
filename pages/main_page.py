from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):

    POPUP_BTNCLOSE = (By.CSS_SELECTOR, '.popup-close')

    def close_popup(self):
        self.wait_for_element_click(*self.POPUP_BTNCLOSE)

    def open_main(self):
        self.open_url('https://shop.cureskin.com/')


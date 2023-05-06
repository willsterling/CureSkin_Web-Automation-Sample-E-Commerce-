from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResultsPage(Page):
    RESULTS_SHOWN = (By.CSS_SELECTOR, "span.predictive-search__item-heading.h4")

    def verify_search_results_shown(self):
        self.wait_for_element_appear(*self.RESULTS_SHOWN)



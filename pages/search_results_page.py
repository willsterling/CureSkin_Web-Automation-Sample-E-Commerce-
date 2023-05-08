from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResultsPage(Page):
    # RESULTS_SHOWN = (By.CSS_SELECTOR, "span.predictive-search__item-heading.h4")
    RESULTS_SHOWN = (By.CSS_SELECTOR, "a.card-information__text.h4")

    def verify_search_results_shown(self, expected_result):
        actual_result = self.find_elements(*self.RESULTS_SHOWN)
        print(type(actual_result))
        assert int(expected_result) == len(actual_result), f'Expected {expected_result} but got {len(actual_result)}'

        # self.wait_for_element_appear(*self.RESULTS_SHOWN)



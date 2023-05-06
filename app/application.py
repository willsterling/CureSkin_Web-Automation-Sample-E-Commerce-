from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage
from pages.cart_page import CartPage

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.cart_page = CartPage(self.driver)
        #continue to add pages here as we create separate files for each page


app = Application('driver')
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page:

    def __init__(self, driver):
        self.driver = driver
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        # e.clear()
        e.send_keys(text)
        print(f'Inputting text: {text}')

    def wait_for_element_click(self, *locator):
            e = self.wait.until(EC.element_to_be_clickable(locator), message=f'Element not clickable by {locator}')
            e.click()

    def wait_for_element_disappear(self, *locator):
            self.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self, *locator):
            return self.wait.until(EC.presence_of_element_located(locator))

    def verify_text(self, expected_text, *locator):
        actual_result = self.driver.find_element(*locator).text
        assert expected_text == actual_result, f'Expected {expected_text} but got {actual_result}'

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, \
            f'Checking by locator {locator}. Expected text {expected_text} is not in {actual_text}'

    def verify_heading(self, expected_heading, *locator):
        actual_heading = self.driver.find_element(*locator).text
        assert expected_heading == actual_heading, f'Expected {expected_heading} but got {actual_heading}'
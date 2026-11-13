from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Contains simple, reusable Selenium actions for all pages."""

    def __init__(self, driver):
        self.driver = driver
        # Wait up to 20 seconds for slow demo pages to load
        self.wait = WebDriverWait(driver, 20)

    def open_url(self, url):
        """Navigates the browser to a specific web address."""
        self.driver.get(url)

    def click(self, locator):
        """Waits for an element to be clickable, then clicks it."""
        element = self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Could not find clickable element: {locator}"
        )
        element.click()

    def type_text(self, locator, text):
        """Waits for a text box to appear, clears it, and types text."""
        element = self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Could not find input box: {locator}"
        )
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Waits for an element to appear and returns its visible text."""
        element = self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Could not read text from element: {locator}"
        )
        return element.text

    def count_elements(self, locator):
        """Counts how many matching elements appear on the screen."""
        elements = self.wait.until(
            EC.visibility_of_all_elements_located(locator),
            message=f"Could not find elements: {locator}"
        )
        return len(elements)
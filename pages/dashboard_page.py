from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):
    """Represents the OrangeHRM Dashboard after logging in."""

    # --- LOCATORS ---
    PAGE_TITLE = (By.TAG_NAME, "h6")
    SIDEBAR_SEARCH_BOX = (By.XPATH, "//input[@placeholder='Search']")
    SIDEBAR_MENU_ITEMS = (By.XPATH, "//ul[@class='oxd-main-menu']//span")
    PROFILE_DROPDOWN = (By.CLASS_NAME, "oxd-userdropdown-tab")
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Logout']")

    # --- ACTIONS ---
    def search_menu(self, keyword):
        self.type_text(self.SIDEBAR_SEARCH_BOX, keyword)

    def logout(self):
        self.click(self.PROFILE_DROPDOWN)
        self.click(self.LOGOUT_BUTTON)

    # --- CHECKS ---
    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def get_menu_item_names(self):
        """Returns a list of visible menu names in the left sidebar."""
        items = self.wait.until(
            lambda driver: driver.find_elements(*self.SIDEBAR_MENU_ITEMS)
        )
        return [item.text for item in items if item.text != ""]
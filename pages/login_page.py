from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Represents the OrangeHRM Login Screen."""

    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    # --- LOCATORS (Where elements live on the page) ---
    USERNAME_BOX = (By.NAME, "username")
    PASSWORD_BOX = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_BANNER = (By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]")
    REQUIRED_LABELS = (By.XPATH, "//span[text()='Required']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//p[contains(., 'Forgot your password')]")

    # --- ACTIONS (What a user can do on this page) ---
    def open(self):
        self.open_url(self.URL)

    def login(self, username, password):
        """Types username & password, then clicks Login."""
        self.type_text(self.USERNAME_BOX, username)
        self.type_text(self.PASSWORD_BOX, password)
        self.click(self.LOGIN_BUTTON)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def click_forgot_password(self):
        self.click(self.FORGOT_PASSWORD_LINK)

    # --- CHECKS (Information we read from this page) ---
    def get_error_message(self):
        return self.get_text(self.ERROR_BANNER)

    def get_required_warning_count(self):
        return self.count_elements(self.REQUIRED_LABELS)
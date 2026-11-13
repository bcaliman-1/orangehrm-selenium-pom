import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@pytest.fixture
def driver():
    """Opens a fresh Firefox browser before each test and closes it after."""
    browser = webdriver.Firefox()
    browser.maximize_window()
    yield browser
    browser.quit()


def test_1_valid_login(driver):
    """Verify a user can log in with valid Admin credentials."""
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    login_page.open()
    login_page.login("Admin", "admin123")

    assert dashboard_page.get_page_title() == "Dashboard"


def test_2_invalid_login(driver):
    """Verify an error message appears when using a wrong password."""
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("Admin", "wrong_password")

    assert login_page.get_error_message() == "Invalid credentials"


def test_3_empty_login_fields(driver):
    """Verify 'Required' warnings appear under both empty fields."""
    login_page = LoginPage(driver)

    login_page.open()
    login_page.click_login_button()

    assert login_page.get_required_warning_count() == 2


def test_4_forgot_password_link(driver):
    """Verify clicking 'Forgot your password?' opens the reset page."""
    login_page = LoginPage(driver)

    login_page.open()
    login_page.click_forgot_password()

    assert "requestPasswordResetCode" in driver.current_url


def test_5_search_menu_and_logout(driver):
    """Verify sidebar search filters results and user can log out."""
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    #Login
    login_page.open()
    login_page.login("Admin", "admin123")

    #Locate the left sidebar
    dashboard_page.search_menu("Recruitment")
    assert dashboard_page.get_menu_item_names() == ["Recruitment"]

    #Logout and confirm the presence of the login screen
    dashboard_page.logout()
    assert "auth/login" in driver.current_url
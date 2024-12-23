import pytest
from pages.login_page import LoginPage
from base_test import driver
from base_test import manage_browser

@pytest.fixture
def login_page(driver):
    driver.get("https://practice.expandtesting.com/login")
    return LoginPage(driver)

def test_login_success(driver, login_page):
    # enter correct credentials
    login_page.login_data("practice", "SuperSecretPassword!")
    # need to scroll page, because ad is hiding the button
    login_page.scroll_by_pixels(500)
    login_page.login_button()
    # check if user is logged properly
    assert login_page.login_success(), "User is not in logged page."

def test_logout(driver, login_page):
    # check if user can log out
    login_page.logout_button()
    assert login_page.logged_out(), "User is not logged out."

def test_login_invalid_username(driver, login_page):
    # enter incorrect username
    login_page.login_data("a", "SuperSecretPassword!")
    # need to scroll page, because ad is hiding the button
    login_page.scroll_by_pixels(500)
    login_page.login_button()
    # check if user is navigated to error page
    assert login_page.login_fail(), "There is no error massage about invalid username"

def test_login_invalid_password(driver, login_page):
    # enter incorrect password value
    login_page.login_data("practice", "a")
    # need to scroll page, because ad is hiding the button
    login_page.scroll_by_pixels(500)
    login_page.login_button()
    # check if user is navigated to error page
    assert login_page.login_fail(), "There is no error massage about invalid password"
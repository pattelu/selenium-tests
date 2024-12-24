import pytest
from pages.register_page import RegisterPage
from base_test import driver
from base_test import manage_browser

@pytest.fixture
def register_page(driver):
    driver.get("https://practice.expandtesting.com/register")
    return RegisterPage(driver)

def test_invalid_username(driver, register_page):
    # no username
    register_page.register_data("", "SuperSecret1!", "SuperSecret1!")
    register_page.scroll_by_pixels(250)
    register_page.register_button()
    assert register_page.is_error()
    # invalid username - special characters
    register_page.register_data("!@#%", "SuperSecret1!", "SuperSecret1!")
    register_page.scroll_by_pixels(250)
    register_page.register_button()
    assert register_page.is_error()
    # too short username
    register_page.register_data("a", "SuperSecret1!", "SuperSecret1!")
    register_page.scroll_by_pixels(250)
    register_page.register_button()
    assert register_page.is_error()

def test_invalid_password(driver, register_page):
    # no password
    register_page.register_data("valid", "", "")
    register_page.scroll_by_pixels(250)
    register_page.register_button()
    assert register_page.is_error()
    # too short password
    register_page.register_data("valid", "A1!", "A1!")
    register_page.scroll_by_pixels(250)
    register_page.register_button()
    assert register_page.is_error()
    # passwords are different
    register_page.register_data("valid", "SuperSecret1!", "DifferentPassword1!")
    register_page.scroll_by_pixels(250)
    register_page.register_button()
    assert register_page.is_error()

def test_register(driver, register_page):
    # valid username and password
    register_page.register_data("valid", "SuperSecret1!", "SuperSecret1!")
    register_page.scroll_by_pixels(250)
    register_page.register_button()
    assert register_page.is_login_page()
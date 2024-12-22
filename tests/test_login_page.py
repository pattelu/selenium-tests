from pages.login_page import LoginPage
from utils.base_test import BaseTest
import time

class TestLoginPage(BaseTest):
    def test_login_page(self):
        self.open_url("https://practice.expandtesting.com/login")
        login_page = LoginPage(self.driver)

        #enter correct value
        login_page.login_data("practice", "SuperSecretPassword!")
        #need to scroll page, because ad is hiding the button
        login_page.scroll_to_bottom()
        login_page.login_button()

        #check if user is logged properly
        assert login_page.login_success(), "User is not in logged page."

        #check if user can log out
        login_page.logout_button()
        assert login_page.logged_out()

        #enter incorrect username value
        login_page.login_data("a", "SuperSecretPassword!")
        #need to scroll page, because ad is hiding the button
        login_page.scroll_to_bottom()
        login_page.login_button()

        #check if user is navigated to error page
        assert login_page.login_fail(), "User got error about invalid credentials"

        #enter incorrect password value
        login_page.login_data("practice", "a")
        #need to scroll page, because ad is hiding the button
        login_page.scroll_to_bottom()
        login_page.login_button()

        #check if user is navigated to error page
        assert login_page.login_fail(), "User got error about invalid credentials"

        #wait 2 seconds before close browser
        time.sleep(2)
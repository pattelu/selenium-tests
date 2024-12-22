from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        # login page
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")

        # logged page
        self.login_text = (By.CLASS_NAME, "subheader")

        self.error_text = (By.ID, "flash")

        # buttons
        self.login_btn = (By.CSS_SELECTOR, "#login > button")
        self.logout_btn = (By.CSS_SELECTOR, "body > main > div.page-layout > div > a > i")

    def login_data(self, username, password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)

    def login_success(self):
        text = "Welcome to the Secure Area."
        subheader = self.driver.find_element(*self.login_text).text
        print(f"Text: {text}")
        print(f"Subheader text: {subheader}")
        return text in self.driver.find_element(*self.login_text).text

    def login_fail(self):
        username_error = "Your username is invalid!"
        password_error = "Your password is invalid!"
        error_massage = self.driver.find_element(*self.error_text).text
        print(f"Username error: {username_error}")
        print(f"Password error: {password_error}")
        print(f"Page error: {error_massage}")
        return username_error or password_error == self.driver.find_element(*self.error_text).text

    def logged_out(self):
        loggedout_text = "You logged out of the secure area!"
        error_massage = self.driver.find_element(*self.error_text).text
        print(f"Password error: {loggedout_text}")
        print(f"Page error: {error_massage}")
        return loggedout_text in self.driver.find_element(*self.error_text).text

    def scroll_to_bottom(self):
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        time.sleep(2)

    def login_button(self):
        self.driver.find_element(*self.login_btn).click()

    def logout_button(self):
        self.driver.find_element(*self.logout_btn).click()
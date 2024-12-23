from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

class LoginPage:
    # login page
    username = (By.ID, "username")
    password = (By.ID, "password")
    error_text = (By.ID, "flash")
    # logged page
    login_text = (By.CLASS_NAME, "subheader")
    # buttons
    login_btn = (By.CSS_SELECTOR, "#login > button")
    logout_btn = (By.CSS_SELECTOR, "body > main > div.page-layout > div > a > i")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

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

    def scroll_by_pixels(self, pixels):
        self.driver.execute_script(f"window.scrollBy(0,{pixels});")
        time.sleep(2)

    def login_button(self):
        self.driver.find_element(*self.login_btn).click()

    def logout_button(self):
        self.driver.find_element(*self.logout_btn).click()
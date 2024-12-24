from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import secrets
import string
import time

class RegisterPage:
    # inputs
    username = (By.ID, "username")
    password = (By.ID, "password")
    confirm_password = (By.ID, "confirmPassword")
    # alerts
    alert = (By.XPATH, "//*[@id='flash']/b")
    # buttons
    register_btn = (By.CSS_SELECTOR, "#login > button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def register_data(self, username, password, confirm_password):
        if username == "valid":
            length = 12
            random_string = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))
            self.driver.find_element(*self.username).send_keys(random_string)
        else:
            self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.confirm_password).send_keys(confirm_password)

    def is_error(self):
        all_fields = "All fields are required."
        short_username = "Username must be at least 3 characters long."
        short_password = "Password must be at least 4 characters long."
        invalid_username = "Invalid username. Usernames can only contain lowercase letters, numbers, and single hyphens, must be between 3 and 39 characters, and cannot start or end with a hyphen."
        different_passwords = "Passwords do not match."
        alert = self.driver.find_element(*self.alert).text
        print(f"Alert: {alert}")
        return (all_fields == self.driver.find_element(*self.alert).text or
                short_username == self.driver.find_element(*self.alert).text or
                short_password == self.driver.find_element(*self.alert).text or
                invalid_username == self.driver.find_element(*self.alert).text or
                different_passwords == self.driver.find_element(*self.alert).text
        )
    def is_login_page(self):
        current_url = self.driver.current_url
        print(f"Current url: {current_url}")
        return self.driver.current_url == "https://practice.expandtesting.com/login"

    def register_button(self):
        self.driver.find_element(*self.register_btn).click()

    def scroll_by_pixels(self, pixels):
        self.driver.execute_script(f"window.scrollBy(0,{pixels});")
        time.sleep(2)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

class BaseTest:
    def setup_method(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def open_url(self, url):
        self.driver.get(url)
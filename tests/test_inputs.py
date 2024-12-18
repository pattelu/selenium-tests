from pages.inputs_page import InputsPage
from utils.base_test import BaseTest

#from selenium.webdriver.chrome.service import Service


import time

# https://sites.google.com/chromium.org/driver/

class TestInputs(BaseTest):
    def test_inputs(self):
        self.open_url("https://practice.expandtesting.com/inputs")
        inputs_page = InputsPage(self.driver)

        #add values to input fields
        inputs_page.input_values("10", "Test", "pwd", "11211990")

        #check the values in output fields are correct
        assert inputs_page.output_values(), "Wrong output values"

        time.sleep(3)


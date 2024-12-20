from pages.inputs_page import InputsPage
from utils.base_test import BaseTest
import time

class TestInputs(BaseTest):
    def test_inputs(self):
        self.open_url("https://practice.expandtesting.com/inputs")
        inputs_page = InputsPage(self.driver)

        #add values to input fields
        inputs_page.input_values("10", "Test", "pwd", "11211990")

        #press "Display Inputs" button
        inputs_page.display_inputs()

        #check the values in output fields are correct
        assert inputs_page.check_output_number(), "Wrong value"
        assert inputs_page.check_output_text(), "Wrong value"
        assert inputs_page.check_output_password(), "Wrong value"
        assert inputs_page.check_output_date(), "Wrong value"

        #press "Clear Inputs" button
        inputs_page.clear_inputs()

        #wait 2 seconds before close browser
        time.sleep(2)
import pytest
from pages.inputs_page import InputsPage
from base_test import driver
from base_test import manage_browser
import time

@pytest.fixture
def inputs_page(driver):
    driver.get("https://practice.expandtesting.com/inputs")
    return InputsPage(driver)

'''
    TDL:
    -check if in every input field you can add only proper character
    -check why firefox doesn't input date
'''

def test_output(driver, inputs_page):
    #add values to input fields
    inputs_page.input_values("10", "Test", "pwd", "11211990")
    #press "Display Inputs" button
    inputs_page.display_inputs()
    #check the values in output fields are correct
    assert inputs_page.check_output_number(), "Wrong number value"
    assert inputs_page.check_output_text(), "Wrong text value"
    assert inputs_page.check_output_password(), "Wrong password value"
    assert inputs_page.check_output_date(), "Wrong date value"
    #press "Clear Inputs" button
    inputs_page.clear_inputs()
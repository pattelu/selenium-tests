import pytest
from pages.inputs_page import InputsPage
from base_test import driver
from base_test import manage_browser

@pytest.fixture
def inputs_page(driver):
    driver.get("https://practice.expandtesting.com/inputs")
    return InputsPage(driver)

def test_number_input(driver, inputs_page):
    inputs_page.input_values("10","","","")
    inputs_page.display_inputs()
    assert inputs_page.check_output_number(), "Wrong number value."
    inputs_page.clear_inputs()

    inputs_page.input_values("Abc!", "", "", "")
    inputs_page.display_inputs()
    assert not inputs_page.check_output_number() is not None, "Wrong number value."
    inputs_page.clear_inputs()

def test_text_input(driver, inputs_page):
    inputs_page.input_values("", "Abc12!", "", "")
    inputs_page.display_inputs()
    assert inputs_page.check_output_text(), "Wrong text value."
    inputs_page.clear_inputs()

def test_password_input(driver, inputs_page):
    inputs_page.input_values("", "", "Abc12!", "")
    inputs_page.display_inputs()
    assert inputs_page.check_output_password(), "Wrong password value."
    inputs_page.clear_inputs()

def test_date_input(driver, inputs_page):
    inputs_page.input_values("", "", "", "1990-10-21")
    inputs_page.display_inputs()
    assert inputs_page.check_output_date(), "Wrong date value."
    inputs_page.clear_inputs()

    inputs_page.input_values("", "", "", "Abc!")
    inputs_page.display_inputs()
    assert not inputs_page.check_output_date() is not None, "Wrong date value."
    inputs_page.clear_inputs()

def test_all_outputs(driver, inputs_page):
    #add values to input fields
    inputs_page.input_values("10", "Test", "pwd", "1990-10-21")
    #press "Display Inputs" button
    inputs_page.display_inputs()
    #check the values in output fields are correct
    assert inputs_page.check_output_number(), "Wrong number value."
    assert inputs_page.check_output_text(), "Wrong text value."
    assert inputs_page.check_output_password(), "Wrong password value."
    assert inputs_page.check_output_date(), "Wrong date value."
    #press "Clear Inputs" button
    inputs_page.clear_inputs()
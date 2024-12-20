from selenium.webdriver.common.by import By

class InputsPage:
    def __init__(self, driver):
        self.driver = driver

        #inputs
        self.input_number = (By.ID, "input-number")
        self.input_text = (By.ID, "input-text")
        self.input_password = (By.ID, "input-password")
        self.input_date = (By.ID, "input-date")

        #outputs
        self.output_number = (By.ID, "output-number")
        self.output_text = (By.ID, "output-text")
        self.output_password = (By.ID, "output-password")
        self.output_date = (By.ID, "output-date")

        #buttons
        self.display_inputs_btn = (By.ID, "btn-display-inputs")
        self.clear_inputs_btn = (By.ID, "btn-clear-inputs")

    def input_values(self, number, text, password, date):
        self.driver.find_element(*self.input_number).send_keys(number)
        self.driver.find_element(*self.input_text).send_keys(text)
        self.driver.find_element(*self.input_password).send_keys(password)
        self.driver.find_element(*self.input_date).send_keys(date)

    def check_output_number(self):
        input_number = self.driver.find_element(*self.input_number).get_attribute("value")
        output_number = self.driver.find_element(*self.output_number).text
        print(f"Input number: {input_number}")
        print(f"Output number: {output_number}")
        return self.driver.find_element(*self.input_number).get_attribute("value") == self.driver.find_element(*self.output_number).text

    def check_output_text(self):
        input_text = self.driver.find_element(*self.input_text).get_attribute("value")
        output_text = self.driver.find_element(*self.output_text).text
        print(f"Input text: {input_text}")
        print(f"Output text: {output_text}")
        return self.driver.find_element(*self.input_text).get_attribute("value") == self.driver.find_element(*self.output_text).text
    
    def check_output_password(self):
        input_password = self.driver.find_element(*self.input_password).get_attribute("value")
        output_password = self.driver.find_element(*self.output_password).text
        print(f"Input password: {input_password}")
        print(f"Output password: {output_password}")
        return self.driver.find_element(*self.input_password).get_attribute("value") == self.driver.find_element(*self.output_password).text

    def check_output_date(self):    
        date_input = self.driver.find_element(*self.input_date).get_attribute("value")
        date_output = self.driver.find_element(*self.output_date).text
        print(f"Input date: {date_input}")
        print(f"Output Date: {date_output}")
        return self.driver.find_element(*self.input_date).get_attribute("value") == self.driver.find_element(*self.output_date).text

    def display_inputs(self):
        self.driver.find_element(*self.display_inputs_btn).click()

    def clear_inputs(self):
        self.driver.find_element(*self.clear_inputs_btn).click()
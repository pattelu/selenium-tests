from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        self.driver.find_element(*self.display_inputs_btn).click()
    
    def output_values(self):
        return self.driver.find_element(*self.input_number).text in self.driver.find_element(*self.output_number).text
        return self.driver.find_element(*self.input_text).text in self.driver.find_element(*self.output_text).text
        return self.driver.find_element(*self.input_password).text in self.driver.find_element(*self.output_password).text
        
        #Conver date to output format
        date_str = self.driver.find_element(*self.input_date).text
        day = date_str[2:4]
        month = data_str[:2]
        year = data_str[4:5]
        formatted_date = f"{year}-{month}-{day}"

        return formatted_date in self.driver.find_element(*self.output_date).text
        self.driver.find_element(*self.clear_inputs_btn).click()
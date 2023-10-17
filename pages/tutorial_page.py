# Import necessary libraries
import time
from selenium.webdriver.common.by import By

# Define a class for the TutorialPage using the Page Object Model (POM) design pattern
class TutorialPage:
    # Constructor method for the class
    def __init__(self, driver):
        # The driver instance is passed to the class
        self.driver = driver

    # Method to fill the name field
    def fill_name(self, name):
        # Locate the name field using XPATH locator
        name_field = self.driver.find_element(By.XPATH, "//input[@id='name']")
        # Send the 'name' value to the name field
        name_field.send_keys(name)

    # Method to fill the email field
    def fill_email(self, email):
        # Locate the email field using XPATH locator
        email_field = self.driver.find_element(By.XPATH, "//input[@name='email']")
        # Send the 'email' value to the email field
        email_field.send_keys(email)

    # Method to fill the phone field
    def fill_phone(self, phone):
        # Locate the phone field using ID locator
        phone_field = self.driver.find_element(By.ID, "phone")
        # Send the 'phone' value to the phone field
        phone_field.send_keys(phone)

    # Method to click the dropdown
    def click_dropdown(self, dropdown_xpath, option_text):
        # Locate the dropdown using XPATH locator
        dropdown = self.driver.find_element(By.XPATH, dropdown_xpath)
        dropdown.click()
        time.sleep(1)
        
        self.driver.find_element(By.XPATH, f"//a[text()='{option_text}']").click()
        time.sleep(3)

    # Method to click the gender dropdown
    def click_gender(self, gender):
        self.click_dropdown("//button[@data-toggle='dropdown']", gender)

    # Method to set the checkbox
    def set_checkbox(self):
        checkbox = self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()


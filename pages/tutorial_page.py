# Import necessary libraries
import time
from selenium.webdriver.common.by import By


class TutorialPage:
    """Define a class for the TutorialPage using the Page Object Model (POM) design pattern"""

    def __init__(self, driver):
        """Constructor method for the class

        Args:
            driver (selenium.webdriver): The driver instance is passed to the class
        """

        self.driver = driver

    def fill_name(self, name):
        """Method to fill the name field

        Args:
            name (str): the 'name' value
        """
        name_field = self.driver.find_element(By.XPATH, "//input[@id='name']")
        name_field.send_keys(name)

    def fill_email(self, email):
        """Method to fill the email field

        Args:
            email (str): the 'email' value
        """

        email_field = self.driver.find_element(By.XPATH, "//input[@name='email']")
        email_field.send_keys(email)

    def fill_phone(self, phone):
        """Method to fill the phone field

        Args:
            phone (str): the 'email' value
        """

        phone_field = self.driver.find_element(By.ID, "phone")
        phone_field.send_keys(phone)

    def click_dropdown(self, dropdown_xpath, option_text):
        """Method to click the dropdown

        Args:
            dropdown_xpath (str): the XPATH locator
            option_text (str): the option text
        """
        dropdown = self.driver.find_element(By.XPATH, dropdown_xpath)
        dropdown.click()

        self.driver.find_element(By.XPATH, f"//a[text()='{option_text}']").click()

    def click_gender(self, gender):
        """Method to click the gender dropdown

        Args:
            gender (str): the 'gender' value
        """
        self.click_dropdown("//button[@data-toggle='dropdown']", gender)

    def set_checkbox(self):
        """Method to set the checkbox"""
        self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()

    def cick_button(self):
        """Method to click the button"""
        self.driver.find_element(By.XPATH, "//button[text()='Click me!']").click()

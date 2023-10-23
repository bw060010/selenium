# Import necessary libraries
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class TutorialPage:
    """Define a class for the TutorialPage using the Page Object Model (POM) design pattern"""

    def __init__(self, driver, logger):
        """Constructor method for the class

        Args:
            driver (selenium.webdriver): The driver instance is passed to the class
            logger (logging): Error logging
        """

        self.driver = driver
        self.logger = logger

    # create one function for each field, to make the code more readable
    def fill_element(self, element_name, value, xpath_locator):
        """Method to fill a field

        Args:
            element_name (str): the name of the element
            value (str): the value to fill the field with
            xpath_locator (str): the XPATH locator
        """
        try:
            element = self.driver.find_element(By.XPATH, xpath_locator)
        except NoSuchElementException as e:
            self.logger.error("Elemenent not found: %s", e)
            raise
        element.send_keys(value)

    def click_dropdown(self, dropdown_xpath, option_text):
        """Method to click the dropdown

        Args:
            dropdown_xpath (str): the XPATH locator
            option_text (str): the option text
        """
        try:
            dropdown = self.driver.find_element(By.XPATH, dropdown_xpath)
        except NoSuchElementException as e:
            self.logger.error("Elemenent not found: %s", e)
            raise
        dropdown.click()

        try:
            dropdown = self.driver.find_element(
                By.XPATH, f"//a[text()='{option_text}']"
            )
        except NoSuchElementException as e:
            self.logger.error("Elemenent not found: %s", e)
            raise

        dropdown.click()

    def click_gender(self, gender):
        """Method to click the gender dropdown

        Args:
            gender (str): the 'gender' value
        """
        self.click_dropdown("//button[@data-toggle='dropdown']", gender)

    def set_checkbox(self):
        """Method to set the checkbox"""
        try:
            checkbox = self.driver.find_element(By.XPATH, "//input[@type='checkbox']")
        except NoSuchElementException as e:
            self.logger.error("Elemenent not found: %s", e)
            raise

        checkbox.click()

    def click_button(self):
        """Method to click the button"""
        try:
            button = self.driver.find_element(By.XPATH, "//button[text()='Click me!']")
        except NoSuchElementException as e:
            self.logger.error("Elemenent not found: %s", e)
            raise

        button.click()

    def validate_name_entered(self):
        """Method to validate that the name was entered"""
        # Click the button to submit the form
        self.click_button()

        # Wait for the validation message to appear
        time.sleep(2)

        # Check if the validation message is present and print the result
        try:
            self.driver.find_element(
                "xpath", "//label[text()='Please enter your name']"
            )
            result_flag = True
        except NoSuchElementException as e:
            self.logger.error("Elemenent not found: %s", e)
            result_flag = False
            print("Validation message for name NOT present")

        if result_flag:
            print("Validation message for name present")

    def check_url(self, url):
        """Method to check if the URL is correct

        Args:
            url (str): the URL to check

        Returns:
            _type_: bool
        """
        return self.driver.current_url == url

    def click_element(self, element_name):
        """Method to click an element

        Args:
            element_name (str): the XPATH locator
        """
        try:
            element = self.driver.find_element(By.XPATH, element_name)
        except NoSuchElementException as e:
            self.logger.error("Elemenent not found: %s", e)
            raise
        element.click()

    def hover_over_element(self, element_name):
        """Method to hover over an element

        Args:
            element_name (str): the XPATH locator
        """
        try:
            element = self.driver.find_element(By.XPATH, element_name)
        except NoSuchElementException as e:
            self.logger.error("Elemenent not found: %s", e)
            raise

        # Create an instance of ActionChains and move to the element
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def count_table_rows(self, table_name_locator):
        """Method to count the number of rows in a table

        Args:
            table_name_locator (str): the XPATH locator
        """
        try:
            table = self.driver.find_element(By.XPATH, table_name_locator)
        except NoSuchElementException as e:
            self.logger.error("Elemenent not found: %s", e)
            raise

        # Get all the rows in the table
        rows = table.find_elements(By.TAG_NAME, "tr")

        # Return the number of rows
        return len(rows)

    # parse the text within each cell of a table and return the text
    def parse_table_text(self, table_name_locator):
        """Method to parse the text within each cell of a table and return the text

        Args:
            table_name_locator (str): the XPATH locator
        """
        try:
            table = self.driver.find_element(By.XPATH, table_name_locator)
        except NoSuchElementException as e:
            self.logger.error("Elemenent not found: %s", e)
            raise

        # Get all the rows in the table
        rows = table.find_elements(By.TAG_NAME, "tr")

        # Create an empty list to store the text
        texts = []

        # Iterate over the rows and get the text from each cell
        for row in rows:
            # Get the cells in each row
            cells = row.find_elements(By.TAG_NAME, "td")

            # Iterate over the cells and get the text
            for cell in cells:
                texts.append(cell.text)

        # Return the text
        return texts

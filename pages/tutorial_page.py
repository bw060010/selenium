from selenium.webdriver.common.by import By

class TutorialPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_name(self, name):
        name_field = self.driver.find_element(By.XPATH, "//input[@id='name']")
        name_field.send_keys(name)

    def fill_email(self, email):
        email_field = self.driver.find_element(By.XPATH, "//input[@name='email']")
        email_field.send_keys(email)

    def fill_phone(self, phone):
        phone_field = self.driver.find_element(By.ID, "phone")
        phone_field.send_keys(phone)

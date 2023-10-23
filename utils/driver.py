# Import the webdriver module from selenium
from selenium import webdriver


def setup_driver():
    """Function to setup the webdriver

    Returns:
        obj: The webdriver object
    """

    driver = webdriver.Firefox()

    driver.get("http://qxf2.com/selenium-tutorial-main")

    return driver


def teardown_driver(driver):
    """Function to quit the webdriver

    Args:
        driver (obj): The webdriver object to quit
    """
    driver.quit()

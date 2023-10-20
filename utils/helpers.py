# Import necessary libraries
import random
import string
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def generate_random_string(length):
    """
    Generate a random string of a given length.

    Parameters:
    length (int): The length of the string to generate.

    Returns:
    str: A random string of the specified length.
    """
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def wait_for_element(driver, by, value):
    """
    Wait for an element to be present on the page.

    Parameters:
    driver (WebDriver): The WebDriver instance to use.
    by (By): The method to locate the element.
    value (str): The value for the method to locate the element.

    Returns:
    WebElement: The WebElement once it is located.
    """
    wait = WebDriverWait(driver, 10)
    return wait.until(EC.presence_of_element_located((by, value)))


def take_screenshot(driver, filename):
    """
    Take a screenshot of the current page.

    Parameters:
    driver (WebDriver): The WebDriver instance to use.
    filename (str): The name of the file to save the screenshot as.
    """
    driver.save_screenshot(filename)


def maximize_window(driver):
    """
    Maximize the window

    Parameters:
    driver (WebDriver): The WebDriver instance to use.
    """
    driver.maximize_window()

    import logging


def setup_logger(name, log_file, level=logging.ERROR):
    """Set up logger to log messages to console and file."""
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

    handler = logging.FileHandler("logs/" + log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

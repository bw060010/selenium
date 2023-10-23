# Import necessary libraries
import random
import string
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def generate_random_string(length):
    """Function to generate a random string

    Args:
        length (int): The length of the random string.

    Returns:
        str: The random string.
    """
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def wait_for_element(driver, by, value):
    """Function to wait for an element to be located

    Args:
        driver (WebDriver): The WebDriver instance to use.
        by (str): The type of selector to use.
        value (str): The selector value.

    Returns:
        WebElement: The located element.
    """
    wait = WebDriverWait(driver, 10)
    return wait.until(EC.presence_of_element_located((by, value)))


def take_screenshot(driver, filename):
    """Function to take a screenshot

    Args:
        driver (WebDriver): The WebDriver instance to use.
        filename (str): The name of the file to save.
    """
    driver.save_screenshot(filename)


def maximize_window(driver):
    """Function to maximize the window

    Args:
        driver (WebDriver): The WebDriver instance to use.
    """
    driver.maximize_window()

    import logging


def setup_logger(name, log_file, level=logging.ERROR):
    """Function setup as many loggers as you want

    Args:
        name (str): The name of the logger
        log_file (str): The name of the log file
        level (str): The log level

    Returns:
        logger: The logger object
    """
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

    handler = logging.FileHandler("logs/" + log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

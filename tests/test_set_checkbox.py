# Import necessary modules
from pages.tutorial_page import TutorialPage
from utils.driver import setup_driver, teardown_driver
from utils.helpers import maximize_window, take_screenshot, setup_logger


# Define the test function
def test_set_checkbox():
    # Set up the driver
    driver = setup_driver()

    # Set up logging
    logger = setup_logger("selenium_tests", "selenium_error.log")

    # Assert that the correct page is loaded
    try:
        assert "Qxf2 Services: Selenium training main" in driver.title
        print("Success: Qxf2 Tutorial page launched successfully")
    except AssertionError as e:
        logger.error("Page not found: %s", e)

    # Maximize window
    maximize_window(driver)

    # Create an instance of the TutorialPage class
    tutorial_page = TutorialPage(driver, logger)

    # Set the checkbox
    tutorial_page.set_checkbox()

    # Take a screenshot and save it as 'screenshot_checkbox.png'
    take_screenshot(driver, "screenshots\\screenshot_checkbox.png")

    # Tear down the driver
    teardown_driver(driver)

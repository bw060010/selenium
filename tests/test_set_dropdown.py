# Import necessary modules
from pages.tutorial_page import TutorialPage
from utils.driver import setup_driver, teardown_driver
from utils.helpers import take_screenshot
from utils.helpers import setup_logger


# Define the test function
def test_set_dropdown():
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
        raise

    # Create an instance of the TutorialPage class
    tutorial_page = TutorialPage(driver, logger)

    # Fill the male gender in the dropdown
    tutorial_page.click_gender("Male")

    # Take a screenshot and save it as 'screenshot.png'
    take_screenshot(driver, "screenshots\\screenshot_dropdown.png")

    # Tear down the driver
    teardown_driver(driver)

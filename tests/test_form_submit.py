# Import necessary modules
import time
from pages.tutorial_page import TutorialPage
from utils.driver import setup_driver, teardown_driver
from utils.helpers import generate_random_string, take_screenshot, setup_logger


# Define the test function
def test_form_submit():
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

    # Create an instance of the TutorialPage class
    tutorial_page = TutorialPage(driver, logger)

    # Fill the name field with a random string of length 10
    tutorial_page.fill_name(generate_random_string(10))
    tutorial_page.fill_email("avinash@qxf2.com")
    tutorial_page.fill_phone("9999999999")

    tutorial_page.click_button()

    time.sleep(1)

    try:
        assert "https://qxf2.com/selenium-tutorial-redirect" in driver.current_url
        print("Successfull redirect")
    except AssertionError as e:
        logger.error("Page not found: %s", e)
        raise

    # Take a screenshot and save it as 'screenshot_submit.png'
    take_screenshot(driver, "screenshots\\screenshot_submit.png")

    # Tear down the driver
    teardown_driver(driver)

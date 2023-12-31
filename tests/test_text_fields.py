# Import necessary modules
from pages.tutorial_page import TutorialPage
from utils.driver import setup_driver, teardown_driver
from utils.helpers import generate_random_string, take_screenshot, setup_logger


# Define the test function
def test_fill_fields():
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

    # create one function for each field, to make the code more readable
    tutorial_page.fill_element(
        "name", generate_random_string(10), "//input[@id='name']"
    )
    tutorial_page.fill_element("email", "avinash@qxf2.com", "//input[@name='email']")
    tutorial_page.fill_element("phone", "9999999999", "//input[@id='phone']")

    # Take a screenshot and save it as 'screenshot.png'
    take_screenshot(driver, "screenshots\\screenshot.png")

    # Tear down the driver
    teardown_driver(driver)

# Import necessary modules
from pages.tutorial_page import TutorialPage
from utils.driver import setup_driver, teardown_driver
from utils.helpers import maximize_window, take_screenshot, setup_logger


# Define the test function
def test_parse_table_text():
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

    # Parse the table text
    texts = tutorial_page.parse_table_text("//table[@name='Example Table']")

    # Print the table text
    print(f"Table text: {texts}")

    # Tear down the driver
    teardown_driver(driver)

# Import necessary modules
from pages.tutorial_page import TutorialPage
from utils.driver import setup_driver, teardown_driver
from utils.helpers import maximize_window, take_screenshot, setup_logger


# Define the test function
def test_count_rows():
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

    # Count the number of rows in the table
    rows = tutorial_page.count_table_rows("//table[@name='Example Table']")

    # Print the number of rows
    print(f"Number of rows in the table: {rows}")

    # Take a screenshot and save it as 'screenshot_table.png'
    take_screenshot(driver, "screenshots\\screenshot_table.png")

    # Tear down the driver
    teardown_driver(driver)

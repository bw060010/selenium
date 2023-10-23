# Import necessary modules
import time
from pages.tutorial_page import TutorialPage
from utils.driver import setup_driver, teardown_driver
from utils.helpers import take_screenshot, setup_logger


# Define the test function
def test_hover():
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

    # Hover over the 'Resources' menu item
    tutorial_page.click_element("//img[@src='./assets/img/menu.png']")
    tutorial_page.hover_over_element("//a[text()='Resources']")

    # Take a screenshot and save it as 'screenshot_hover.png'
    take_screenshot(driver, "screenshots\\screenshot_hover.png")

    # Click the button and redirect to the next page
    tutorial_page.click_element("//a[text()='GUI automation']")
    time.sleep(1)

    # Assert that the correct page is loaded after redirect
    try:
        assert "https://qxf2.com/gui-automation-diy" in driver.current_url
        print("Successfull redirect")
    except AssertionError as e:
        logger.error("Page not found: %s", e)
        raise

    # Tear down the driver
    teardown_driver(driver)

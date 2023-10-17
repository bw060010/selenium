# Import necessary modules
from pages.tutorial_page import TutorialPage
from utils.driver import setup_driver, teardown_driver
from utils.helpers import maximize_window, take_screenshot

# Define the test function
def test_set_checkbox():
    # Set up the driver
    driver = setup_driver()

    # Assert that the correct page is loaded
    assert "Qxf2 Services: Selenium training main" in driver.title
    print ("Success: Qxf2 Tutorial page launched successfully")

    # Maximize window
    maximize_window(driver)

    # Create an instance of the TutorialPage class
    tutorial_page = TutorialPage(driver)

    # Fill the male gender in the dropdown
    tutorial_page.set_checkbox()

    # Take a screenshot and save it as 'screenshot_checkbox.png'
    take_screenshot(driver, 'screenshot_checkbox.png')

    # Tear down the driver
    teardown_driver(driver)

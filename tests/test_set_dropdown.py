# Import necessary modules
from pages.tutorial_page import TutorialPage
from utils.driver import setup_driver, teardown_driver
from utils.helpers import generate_random_string, take_screenshot

# Define the test function
def test_set_dropdown():
    # Set up the driver
    driver = setup_driver()

    # Assert that the correct page is loaded
    assert "Qxf2 Services: Selenium training main" in driver.title
    print ("Success: Qxf2 Tutorial page launched successfully")

    # Create an instance of the TutorialPage class
    tutorial_page = TutorialPage(driver)

    # Fill the male gender in the dropdown
    tutorial_page.click_gender('Male')

    # Take a screenshot and save it as 'screenshot.png'
    take_screenshot(driver, 'screenshot_dropdown.png')

    # Tear down the driver
    teardown_driver(driver)

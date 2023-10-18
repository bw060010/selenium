# Import necessary modules
from pages.tutorial_page import TutorialPage
from utils.driver import setup_driver, teardown_driver
from utils.helpers import generate_random_string, take_screenshot


# Define the test function
def test_fill_fields():
    # Set up the driver
    driver = setup_driver()

    # Assert that the correct page is loaded
    assert "Qxf2 Services: Selenium training main" in driver.title
    print("Success: Qxf2 Tutorial page launched successfully")

    # Create an instance of the TutorialPage class
    tutorial_page = TutorialPage(driver)

    # Fill the name field with a random string of length 10
    tutorial_page.fill_name(generate_random_string(10))
    # Fill the email field
    tutorial_page.fill_email("avinash@qxf2.com")
    # Fill the phone field
    tutorial_page.fill_phone("9999999999")

    # Take a screenshot and save it as 'screenshot.png'
    take_screenshot(driver, "screenshot.png")

    # Tear down the driver
    teardown_driver(driver)

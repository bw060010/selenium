from pages.tutorial_page import TutorialPage
from utils.driver import setup_driver, teardown_driver
from utils.helpers import generate_random_string, take_screenshot

def test_fill_fields():

    driver = setup_driver()

    assert "Qxf2 Services: Selenium training main" in driver.title

    tutorial_page = TutorialPage(driver)

    tutorial_page.fill_name(generate_random_string(10))
    tutorial_page.fill_email('avinash@qxf2.com')
    tutorial_page.fill_phone('9999999999')

    take_screenshot(driver, 'screenshot.png')

    teardown_driver(driver)

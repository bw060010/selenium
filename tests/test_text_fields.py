from pages.tutorial_page import TutorialPage
from utils.driver import setup_driver, teardown_driver

def test_fill_fields():
    driver = setup_driver()
    tutorial_page = TutorialPage(driver)

    tutorial_page.fill_name('Avinash')
    tutorial_page.fill_email('avinash@qxf2.com')
    tutorial_page.fill_phone('9999999999')

    assert "Qxf2 Services: Selenium training main" in driver.title

    teardown_driver(driver)

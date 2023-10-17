from selenium import webdriver

def setup_driver():
    driver = webdriver.Firefox()
    driver.get("http://qxf2.com/selenium-tutorial-main")
    return driver

def teardown_driver(driver):
    driver.quit()

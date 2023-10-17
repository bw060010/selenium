# Import the webdriver module from selenium
from selenium import webdriver

# Function to setup the webdriver
def setup_driver():
    # Create a new instance of the Firefox driver
    driver = webdriver.Firefox()
    
    # Navigate to the desired webpage
    driver.get("http://qxf2.com/selenium-tutorial-main")
    
    # Return the driver instance
    return driver

# Function to teardown the webdriver
def teardown_driver(driver):
    # Close the browser window and end the webdriver session
    driver.quit()

import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def wait_for_element(driver, by, value):
    wait = WebDriverWait(driver, 10)
    return wait.until(EC.presence_of_element_located((by, value)))

def take_screenshot(driver, filename):
    driver.save_screenshot(filename)

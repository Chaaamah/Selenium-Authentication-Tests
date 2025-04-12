import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def browser():
    # Initialize the Firefox driver
    driver = webdriver.Firefox()

    # Open a website
    driver.get("https://www.saucedemo.com")

    # Fixture returns the driver instance to the test
    yield driver 

    # Teardown after test
    time.sleep(10) 

    # Properly close the browser after the test
    driver.quit()   

def test_authentication(browser):
    # Locate username and password fields
    userName = browser.find_element(By.ID, "user-name")
    password = browser.find_element(By.ID, "password")

    # Perform login
    userName.send_keys("standard_user")
    password.send_keys("secret_sauce")
    password.submit()

    # Assert redirect is successful
    assert browser.current_url == "https://www.saucedemo.com/inventory.html", "Login failed or incorrect redirect"

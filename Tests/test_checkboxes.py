import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from page_objects.checkbox_page import CheckBoxPage

@pytest.fixture
def browser():
    # Initialize the Firefox driver
    driver = webdriver.Firefox()

    # Open the website
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    # Provide the driver instance to the test
    yield driver

    # Wait for 10 seconds to visually confirm (optional)
    time.sleep(4)

    # Close the browser after the test
    driver.quit()

@pytest.mark.checkbox
def test_checkbox(browser):
    checkBoxPage = CheckBoxPage(browser)
    
    checkBoxPage.go_to()

    checkBoxPage.manage_checkbox("checkbox1", True)
    checkBoxPage.manage_checkbox("checkbox2", False)
    time.sleep(2)  # Small pause to ensure state is applied

    assert checkBoxPage.checkbox1.is_selected()
    assert not checkBoxPage.checkbox2.is_selected()
   
def manage_checkbox(checkbox, desired_state):
    # Change checkbox state only if needed
    if checkbox.is_selected() != desired_state:
        checkbox.click()

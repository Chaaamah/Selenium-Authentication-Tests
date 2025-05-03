import pytest
from selenium import webdriver
from page_objects.dropdown_page import DropdownPage

@pytest.fixture
def browser():
    # Initialize the Firefox driver
    driver = webdriver.Firefox()

    # Provide the driver instance to the test
    yield driver

    # Close the browser after the test
    driver.quit()

@pytest.mark.dropdown
def test_select_dropdown_option(browser):
    # Initialize the DropdownPage object
    dropdown_page = DropdownPage(browser)

    # Navigate to the dropdown page
    dropdown_page.go_to()

    # Select an option from the dropdown
    dropdown_page.select_option("2")  # Sélectionne l'option avec la valeur "2"

    # Assert that the correct option is selected
    selected_option = dropdown_page.dropdown.find_element_by_css_selector("option:checked").text
    assert selected_option == "Option 2", f"Expected 'Option 2', but got '{selected_option}'"
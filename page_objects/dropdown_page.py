from seleniumpagefactory import PageFactory
from selenium.webdriver.support.ui import Select
from selenium import webdriver

class DropdownPage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        "dropdown": ("id", "dropdown"),
    }

    def go_to(self):
        self.driver.get("https://the-internet.herokuapp.com/dropdown")

    def select_option(self, option_value: str):
        dropdown_element = self.dropdown
        select = Select(dropdown_element)
        select.select_by_value(option_value)
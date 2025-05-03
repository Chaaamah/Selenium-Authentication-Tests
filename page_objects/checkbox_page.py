from seleniumpagefactory import PageFactory
from selenium import webdriver

class CheckBoxPage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
    
    locators = {
        "checkbox1": ("xpath", '//*[@id="checkboxes"]/input[1]'),
        "checkbox2": ("xpath", '//*[@id="checkboxes"]/input[2]'),
    }

    def go_to(self):
        self.driver.get("https://the-internet.herokuapp.com/checkboxes")

    def manage_checkbox(self,checkbox : str, desired_state : bool):
        if checkbox == "checkbox1":
            if self.checkbox1.is_selected() != desired_state:
                self.checkbox1.click() 
        else:
            if self.checkbox2.is_selected() != desired_state:
                self.checkbox2.click()        

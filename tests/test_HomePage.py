import pytest
import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmition(self,getData):

        log = self.getLogger()

        homepage = HomePage(self.driver)
        log.info("first name is"+ getData['firstname'])
        homepage.get_Name().send_keys(getData['firstname'])

        # Using CSSselector for name populate.
        homepage.get_Email().send_keys(getData['lastname'])

        homepage.get_Password().send_keys(getData['password'])

        homepage.get_Checkbox().click()

        self.SelectByText(homepage.get_select(), getData['gender'])
        # You can directly provide the text present in the dropdown to specifially select it.
        # dropdown.select_by_index(1)  # Index values are starting from 0.
        # dropdown.select_by_value()

        # If you want to Xpath for any element, you have to write syntax like this, it will create a custom path for element of your choice.
        # //element_name[@attribute=”value”]
        # Consider for example you want to target a input element, and lets say you want to use type attribute, so the syntax will be
        #  //input[@type=”submit”] – Now this is your custom xpath, these two forward slashes are important.

        # Selecting a radio button with css selector with CSS syntax of selecting ID attribute, #id_name
        homepage.get_RadioBtn().click()

        # Lets create a Xpath to select the submit button to submit the form.

        homepage.get_submit().click()

        # After submitting the form we get a, messgae at the top,as confirmation to form being submited, we can verifiy that using assertion to make sure website test passed.,  but for now, we will just capture it.

        # Creating method for verify using class selector, now since it is a text we have to either store it in a variable or we can print it, to make sure
        # automation is completed succesfully.
        message = homepage.get_SuccessAlert().text
        print(message)

        assert ("success" in message)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getExcelData("Test2"))
    def getData(self,request):
        return request.param

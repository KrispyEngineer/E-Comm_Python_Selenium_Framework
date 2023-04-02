import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()  # Calling the logging method

        home_page = HomePage(self.driver)
        checkoutpage = home_page.shopItems()
        log.info("Getting all the card Titles.")
        self.driver.implicitly_wait(4)
        # Here in below code we have made use of REGEX for XPATH.
        # The REGEX syntax for CSS and XPATH is as follows.
        # "//a[contains(@href,'shop')]"          For CSS: "a[href*='shop']"

        # self.driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()  - We created a page object for this above.


        products = checkoutpage.getCardTitles()

        for i in products:
            log.info(i.find_element(By.XPATH, "div/h4").text)
            if i.find_element(By.XPATH, "div/h4").text == "Blackberry":
                i.find_element(By.XPATH, "div/button").click()

        # Finally we will do checkout.
        checkoutpage.get_checkout_btn().click()

        # Another Checkout Button.
        confirmpage = checkoutpage.get_confirm_checkout()
        log.info("Entering Country Name as ind")
        # Create object of ConfirmPage
        confirmpage.get_confirm_country().send_keys("ind")
        # Send Explicit Wait

        self.VerifyLinkPresence("India")
        confirmpage.get_select_country().click()

        confirmpage.get_confirm_checkbox().click()
        confirmpage.get_purchase_btn().click()
        success_message = confirmpage.get_validation().text
        log.info("Text received from application is" + success_message)
        assert "Success! Thank you! " in success_message

        self.driver.execute_script("console.log('helloWorld')")
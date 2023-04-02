from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self,driver):
        self.driver = driver
    # Firstly create  a variable object for the driver
    cardTitle = (By.XPATH, "//div[@class='card h-100']")

    # Checkout operation POM
    # driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkout_btn = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    # driver.find_elements(By.XPATH, "//div[@class='card h-100']")

    # Checkout Confirm Button POM
    # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']")
    confirm_checkout = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):

        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def get_checkout_btn(self):
        return self.driver.find_element(*CheckOutPage.checkout_btn)

    def get_confirm_checkout(self):
        self.driver.find_element(*CheckOutPage.confirm_checkout).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage

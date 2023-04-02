from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self,driver):
        self.driver = driver

    #  self.driver.find_element(By.ID, "country")
    confirm_country = (By.ID, "country")

    def get_confirm_country(self):
        return self.driver.find_element(*ConfirmPage.confirm_country)

    # Click on counry name
    # self.driver.find_element(By.LINK_TEXT, "India")
    select_country = (By.LINK_TEXT, "India")

    def get_select_country(self):
        return self.driver.find_element(*ConfirmPage.select_country)

    # Click on checkbox
    # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']")
    confirm_checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")

    def get_confirm_checkbox(self):
        return self.driver.find_element(*ConfirmPage.confirm_checkbox)

    # Purchase Button
    #  self.driver.find_element(By.CLASS_NAME, "btn-success")

    purchase_btn = (By.CLASS_NAME, "btn-success")

    def get_purchase_btn(self):
        return self.driver.find_element(*ConfirmPage.purchase_btn)

    # Validation message
    # self.driver.find_element(By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")
    validation = (By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")

    def get_validation(self):
        return  self.driver.find_element(*ConfirmPage.validation)

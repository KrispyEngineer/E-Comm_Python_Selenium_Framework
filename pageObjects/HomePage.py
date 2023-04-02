from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:
    # Declaring a class Variable
    # #self.driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()
    shop = (By.XPATH, "//a[contains(@href,'shop')]")

    def __init__(self, driver):
        self.driver = driver


    def shopItems(self):  # class variables can be called out with the class_name.var_name
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckOutPage(self.driver)
        return checkoutpage

    # driver.find_element(By.CSS_SELECTOR, "input[name= 'name']")
    name = (By.CSS_SELECTOR, "input[name= 'name']")

    def get_Name(self):
        return  self.driver.find_element(*HomePage.name)

    # driver.find_element(By.NAME, "email")
    email = (By.NAME, "email")

    def get_Email(self):
        return self.driver.find_element(*HomePage.email)

    # driver.find_element(By.ID, "exampleInputPassword1")
    passwd = (By.ID, "exampleInputPassword1")

    def get_Password(self):
        return self.driver.find_element(*HomePage.passwd)

    # driver.find_element(By.ID, "exampleCheck1")
    checkbox = (By.ID, "exampleCheck1")

    def get_Checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    # driver.find_element(By.CSS_SELECTOR, "#inlineRadio1")
    radio_btn = (By.CSS_SELECTOR, "#inlineRadio1")

    # self.driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1"
    select = (By.CSS_SELECTOR, "#exampleFormControlSelect1")

    def get_select(self):
        return self.driver.find_element(*HomePage.select)

    def get_RadioBtn(self):
        return self.driver.find_element(*HomePage.radio_btn)

    # driver.find_element()

    submit = (By.XPATH, "//input[@type='submit']")

    def get_submit(self):
        return self.driver.find_element(*HomePage.submit)

    # driver.find_element(By.CLASS_NAME, "alert-success")
    alert = (By.CLASS_NAME, "alert-success")

    def get_SuccessAlert(self):
        return self.driver.find_element(*HomePage.alert)
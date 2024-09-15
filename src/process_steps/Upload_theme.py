from selenium.webdriver.common.by import By

from src.driver.DriverManger import DriverManager
from src.exception.NotClickableException import NotClickableException

class Addtheme:
    def __init__(self, driver: DriverManager):
        self.driver = driver
    def wrapClickButton(self, element):
        try:
            element.click()
            self.driver.wait_for_page_load_random_sleep()
        except Exception as e:
            raise NotClickableException("the element is not clickable" + str(e))
    def onlinestore(self):
        onlinestorebutton = self.driver.find_element(By.XPATH, "//a[@href='/store/5dc23c-ad/themes']")
        self.wrapClickButton(onlinestorebutton)

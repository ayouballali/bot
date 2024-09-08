import logging
import traceback

from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By

from src.driver.DriverManger import DriverManager
from src.exception.NotClickableException import NotClickableException

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)


class SignIn:
    def __init__(self, driver: DriverManager, username, password):
        self.driver = driver
        self.username = username
        self.password = password

    def login(self):

        # Step 1
        self.startFreeTrial()
        # check if there is any introduction steps
        self.checkIfThereIsAnySkippedStep()
        # Step2
        self.SkipBusinessLocation()

        # Step3
        self.clickOnSignUpWithEmail()

        # Step4
        self.fillAccountCredentials()

        # Step5
        self.loginPage()

        # Step 6 : skip help section
        self.skipHelpSection()

        # we are in the store
        # click on orders
        self.driver.random_sleep(15, 20)

    def checkIfThereIsAnySkippedStep(self):
        try:
            skipAllButton = self.driver.find_element(By.ID, 'navigation-skip-all-button')
            self.wrapClickButton(skipAllButton)
            raise NotClickableException("the element is not clickable")
        except NotClickableException as es:
            raise es
        except Exception as e:
            print("Skip All button not found or not clickable." + str(e))

    def wrapClickButton(self, element):
        try:
            element.click()
            self.driver.wait_for_page_load_random_sleep()
        except Exception as e:
            raise NotClickableException("the element is not clickable" + str(e))

    def startFreeTrial(self):
        startFreeTrialButton = self.driver.find_element(By.LINK_TEXT, 'Start free trial')
        self.wrapClickButton(startFreeTrialButton)

    def SkipBusinessLocation(self):
        try:
            # Check if the "Next" button exists
            next_button = self.driver.find_element((By.XPATH, "//span[text()='Next']/.."))

            self.wrapClickButton(next_button)
            print("'Next' button found. Restarting the script...")
        except (TimeoutException, NoSuchElementException, Exception) as e:
            if isinstance(e, NotClickableException):
                raise NotClickableException("the element is not clickable" + str(e))
            else:
                print(str(traceback.print_exc()))
                pass

    # Step3
    def clickOnSignUpWithEmail(self):
        try:
            next_button = self.driver.find_element(By.CSS_SELECTOR, ".signup a.ui-button.ui-button--full-width")
            self.wrapClickButton(next_button)
        except Exception as e:
            print(f"Failed to click on the 'Next' button: {e}")

    def fillAccountCredentials(self):
        try:
            self.fillSignUpWithEmail()
            self.fillSignUpWithPassword()
            self.submitCredentials()
        except Exception as e:
            print(f"Failed to click on the 'Next' button: {e}")

    def fillSignUpWithEmail(self):
        emailInput = self.driver.find_element(By.CSS_SELECTOR, "input[id='account_email']")
        emailInput.send_keys(self.username)
        self.driver.random_sleep(1, 3)

    def loginPage(self):
        self.fillSignUpWithPassword()
        self.submitCredentials()

    def skipHelpSection(self):
        try:
            iDontNeedHelpButton = self.driver.find_element(By.CSS_SELECTOR,
                                                           "button[aria-label='I don\\'t want help setting up']")
            self.wrapClickButton(iDontNeedHelpButton)
        except Exception as e:
            print(f"Failed to click on the 'I don't want help setting up' button: {e}")

    def fillSignUpWithPassword(self):
        password = self.driver.find_element(By.CSS_SELECTOR, "input[id='account_password']")
        password.send_keys(self.password)
        self.driver.random_sleep(1, 3)

    def submitCredentials(self):
        submitButton = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        self.wrapClickButton(submitButton)

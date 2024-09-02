import random
import traceback
from telnetlib import EC
import subprocess
from urllib.parse import urlparse, parse_qs

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Set up the webdriver (Make sure the path to your webdriver is correct)
driver = webdriver.Chrome()
EMAIL = "jkh_jlop69@hotmail.com"
PASSWORD = "pptproject12345"


def checkIfThereIsAnySkippedStep():
    isThereAnySkipElement = True
    while isThereAnySkipElement:
        try:
            skipAllButton = driver.find_element(By.ID, 'navigation-skip-all-button')
            wrapClickButton(skipAllButton)
        except Exception as e:
            print("Skip All button not found or not clickable.")
            isThereAnySkipElement = False


def wrapClickButton(element):
    random_sleep()
    element.click()
    random_sleep(6, 10)
    checkIfThereIsAnySkippedStep()


def startFreeTrial():
    startFreeTrialButton = driver.find_element(By.LINK_TEXT, 'Start free trial')
    wrapClickButton(startFreeTrialButton)


def SkipBusinessLocation():
    try:
        global driver
        # Check if the "Next" button exists
        next_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Next']/.."))
        )
        wrapClickButton(next_button)
        print("'Next' button found. Restarting the script...")
    except (TimeoutException, NoSuchElementException) as e:
        print("'Next' button not found. Continuing with the script...")
        # Continue with the rest of the script
        driver.quit()
        driver = webdriver.Chrome()
        main()

#Step3
def clickOnSignUpWithEmail():
    # driver.quit()
    # raise Exception("Email not found")
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, ".signup a.ui-button.ui-button--full-width")
        wrapClickButton(next_button)
    except Exception as e:
        print(f"Failed to click on the 'Next' button: {e}")


def fillAccountCredentials():
    try:
        fillSignUpWithEmail()
        fillSignUpWithPassword()
        submitCredentials()
    except Exception as e:
        print(f"Failed to click on the 'Next' button: {e}")


#Step4
def fillSignUpWithEmail():
    emailInput = driver.find_element(By.CSS_SELECTOR, "input[id='account_email']")
    emailInput.send_keys(EMAIL)
    random_sleep(1, 3)


def fillSignUpWithPassword():
    password = driver.find_element(By.CSS_SELECTOR, "input[id='account_password']")
    password.send_keys(PASSWORD)
    random_sleep(1, 3)


def submitCredentials():
    submitButton = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    wrapClickButton(submitButton)


def loginPage():
    fillSignUpWithPassword()
    submitCredentials()


def skipHelpSection():
    try:
        iDontNeedHelpButton = driver.find_element(By.CSS_SELECTOR,
                                                  "button[aria-label='I don\\'t want help setting up']")
        wrapClickButton(iDontNeedHelpButton)
    except Exception as e:
        print(f"Failed to click on the 'I don't want help setting up' button: {e}")


def random_sleep(min_time=2, max_time=5):
    """Pause for a random amount of time between actions."""
    time.sleep(random.uniform(min_time, max_time))


def clickOrdersButton():
    oredersButton = driver.find_element(By.XPATH, "//span[text()='Orders']")
    wrapClickButton(oredersButton)


def main():
    # Open the webpage
    driver.get('https://www.shopify.com/')
    random_sleep(8, 12)
    checkIfThereIsAnySkippedStep()
    #Step 1
    startFreeTrial()
    # // check if there is the rid 
    #Step2
    SkipBusinessLocation()

    #Step3
    clickOnSignUpWithEmail()

    #Step4
    fillAccountCredentials()

    #Step5
    loginPage()

    #Step 6 : skip help section
    skipHelpSection()

    #we are in the store
    #click on orders
    random_sleep(15, 20)
    clickOrdersButton()

def main_loop():
    global driver
    try:
        main()
        print("Main script completed. Starting secondary script loop.")
        driver.quit()
    except Exception as e:
        print(f"An error occurred: {traceback.format_exc()}")
        print("Restarting the main script...")
        driver.quit()


if __name__ == "__main__":
    main_loop()



# there is two option to solve the next button in location check :
    #1st option: get the rid from url and use it to skip the location step
        # https://accounts.shopify.com/signup?rid=6fc79cdc-e465-45a7-9437-883f289c76c8
    #2nd option : so if the next button not clickable just restart the whole script over till it doesn't appear .
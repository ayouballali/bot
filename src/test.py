import random
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# Wait for the page to load (you can adjust the sleep time as needed)
import time

from selenium.webdriver.support.wait import WebDriverWait

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
        # Wait for the "Next" button to be clickable
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Next')]/ancestor::button"))
        )

        # Scroll the button into view
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)

        # Click the button using JavaScript
        driver.execute_script("arguments[0].click();", next_button)

        print("Clicked on the 'Next' button.")

    except Exception as e:
        print(f"Failed to click on the 'Next' button: {e}")


#Step3
def clickOnSignUpWithEmail():
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
        iDontNeedHelpButton = driver.find_element(By.CSS_SELECTOR,"button[aria-label='I don\'t want help setting up']")
        wrapClickButton(iDontNeedHelpButton)
    except Exception as e:
        print(f"Failed to click on the 'I don't want help setting up' button: {e}")
def random_sleep(min_time=2, max_time=5):
    """Pause for a random amount of time between actions."""
    time.sleep(random.uniform(min_time, max_time))


def main():
    # Open the webpage
    driver.get('https://www.shopify.com/')
    random_sleep(8, 12)
    checkIfThereIsAnySkippedStep()
    #Step 1
    startFreeTrial()
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
    while True:
        time.sleep(5)

main()

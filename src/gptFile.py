import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

EMAIL = "jkh_jlop69@hotmail.com"
PASSWORD = "pptproject12345"

# Set up the webdriver with options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-extensions")

# Set up a random user agent
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 "
    "Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
]
chrome_options.add_argument(f"user-agent={random.choice(user_agents)}")

# Initialize the driver
driver = webdriver.Chrome()


def random_sleep(min_time=2, max_time=5):
    """Pause for a random amount of time between actions."""
    time.sleep(random.uniform(min_time, max_time))


def wrapClickButton(element):
    random_sleep()
    element.click()
    random_sleep(6, 10)
    checkIfThereIsAnySkippedStep()


def checkIfThereIsAnySkippedStep():
    isThereAnySkipElement = True
    while isThereAnySkipElement:
        try:
            skipAllButton = driver.find_element(By.ID, 'navigation-skip-all-button')
            wrapClickButton(skipAllButton)
        except Exception:
            isThereAnySkipElement = False


def startFreeTrial():
    startFreeTrialButton = driver.find_element(By.LINK_TEXT, 'Start free trial')
    wrapClickButton(startFreeTrialButton)


def SkipBusinessLocation():
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Next')]/ancestor::button"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        driver.execute_script("arguments[0].click();", next_button)
    except Exception as e:
        print(f"Failed to click on the 'Next' button: {e}")


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
        print(f"Failed to fill account credentials: {e}")


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
        iDontNeedHelpButton = driver.find_element(By.CSS_SELECTOR, "button[aria-label='I don\\'t want help setting up']")
        wrapClickButton(iDontNeedHelpButton)
    except Exception as e:
        print(f"Failed to click on the 'I don't want help setting up' button: {e}")


def main():
    # Open the webpage
    driver.get('https://www.shopify.com/')
    random_sleep(8, 12)
    checkIfThereIsAnySkippedStep()

    startFreeTrial()
    SkipBusinessLocation()
    clickOnSignUpWithEmail()
    fillAccountCredentials()
    loginPage()
    skipHelpSection()

    while True:
        random_sleep(5, 10)


main()

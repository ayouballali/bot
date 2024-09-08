import logging
import random
import time
import webbrowser

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)
class DriverManager(webdriver.Chrome):
    def __init__(self):
        super().__init__()

    def get_url(self, url):
        self.get(url)
        self.wait_for_page_load_random_sleep()

    def wait_for_page_load_random_sleep(self, timeout=10):
        WebDriverWait(self, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
        self.random_sleep()

    def random_sleep(self, min_time=2, max_time=5):
        """Pause for a random amount of time between actions."""
        time.sleep(random.uniform(min_time, max_time))



from driver.DriverManger import DriverManager
from process_steps.SignUpAndLogin.SignIn import SignIn
from src.exception.NotClickableException import NotClickableException

url = "https://www.shopify.com/"

EMAIL = "jkh_jlop69@hotmail.com"
PASSWORD = "pptproject12345"


def main():
    driver: DriverManager = DriverManager()
    #first we need to get the parameters from parameter Manager
    # second initiate driver

    #SignIn
    signIn = SignIn(driver, EMAIL, PASSWORD)
    try:
        signIn.login()
    except Exception as e:
        if isinstance(e, NotClickableException):
            reset_and_run(driver)
            return

    driver.get_url(url)


def reset_and_run(driver):
    driver.quit()
    main()


if __name__ == '__main__':
    main()

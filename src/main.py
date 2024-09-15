from driver.DriverManger import DriverManager
from src.accountParameters.AccountParameters import AccountParameters
from src.process_steps.SignIn import SignIn
from src.exception.NotClickableException import NotClickableException



def main():
    #first we need to get the parameters from parameter Manager
    parameters = AccountParameters()
    account_list = parameters.getAccounts()

    for account in account_list:
        #  initiate driver for each account
        driver: DriverManager = DriverManager()

        #Sign in
        signIn = SignIn(driver, account.email, account.password)
        driver.get_url(parameters.geturl())
        try:
            signIn.login()
        except Exception as e:
            if isinstance(e, NotClickableException):
                reset_and_run(driver)
                return


def reset_and_run(driver):
    driver.quit()
    main()


if __name__ == '__main__':
    main()

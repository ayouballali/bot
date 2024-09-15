import json
import logging
import os

from src.accountParameters.Account import Account


class AccountParameters:
    json_path = "parameters.json"

    def __init__(self):
        self.accounts = []
        self.config_data = {}
        self.load_parameters()

    def load_parameters(self):
        """Load account parameters from the JSON file."""
        try:
            # Ensure the file exists
            if not os.path.exists(AccountParameters.json_path):
                logging.error(f"JSON file not found at: {AccountParameters.json_path}")
                return

            # Open and load the JSON file
            with open(AccountParameters.json_path, "r") as json_file:
                logging.info(f"Loading parameters from {AccountParameters.json_path}")
                self.config_data = json.load(json_file)

            # Validate the presence of the 'accounts' key in JSON
            if "accounts" not in self.config_data:
                logging.error(f"'accounts' key not found in JSON file.")
                return

            # Load account data using list comprehension
            self.accounts = [Account(account) for account in self.config_data["accounts"]]
            logging.info(f"Successfully loaded {len(self.accounts)} accounts.")

        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON: {e}")
        except Exception as e:
            logging.error(f"Unexpected error occurred while loading parameters: {e}")

    def getConfigData(self):
        return self.config_data

    def getAccounts(self):
        return self.accounts

    def geturl(self):
        return self.config_data["url"]


if __name__ == '__main__':
    myAccount = AccountParameters()

    print(myAccount.getAccounts()[0])

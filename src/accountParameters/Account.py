class Account:
    def __init__(self, account_data):
        self.account_name = account_data["account_name"]
        self.email = account_data["email"]
        self.password = account_data["password"]

    def __str__(self):
        return f"Account(Name: {self.account_name}, Email: {self.email}, password: {self.password})"

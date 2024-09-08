class NotClickableException(Exception):
    def __init__(self, message):
        super().__init__(message)  # Initialize the base Exception with the message

    def __str__(self):
        return f"{self.args[0]} "

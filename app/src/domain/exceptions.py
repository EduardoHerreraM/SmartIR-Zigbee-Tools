class ConnectionNotEstablishedException(Exception):
    def __init__(self) -> None:
        super().__init__(
            "Connection cannot be established. Most likely, the username and password are not correct."
        )

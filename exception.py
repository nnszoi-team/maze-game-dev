import exception

class UndefinedOptionError(BaseException):
    def __init__(self, args) -> None:
        self.args = args

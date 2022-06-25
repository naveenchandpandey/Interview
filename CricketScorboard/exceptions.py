from static import CustomExceptions


class DataMismatchException(Exception):
    pass


class InvalidValueException(Exception):
    def __init__(self, run):
        super().__init__(CustomExceptions.InvalidValueException.value + ": " + str(run))



class DataCaptureException(Exception):
    pass


class StatsException(Exception):
    pass


class CLIException(Exception):
    pass


class InvalidCommandError(CLIException):
    pass


class InvalidArgumentError(CLIException):
    pass


class MissingValueError(CLIException):
    pass


class InvalidValueError(CLIException):
    pass

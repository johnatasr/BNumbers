class DataCaptureException(Exception):
    """
    Exception raised for errors related to data capture.

    Inherits:
    - Exception: Python's base exception class.

    Usage Example:
    try:
        # Code that may raise DataCaptureException
    except DataCaptureException as e:
        print(f"DataCaptureException occurred: {e}")
    """

    pass


class StatsException(Exception):
    """
    Exception raised for errors related to statistical operations.

    Inherits:
    - Exception: Python's base exception class.

    Usage Example:
    try:
        # Code that may raise StatsException
    except StatsException as e:
        print(f"StatsException occurred: {e}")
    """

    pass


class CLIException(Exception):
    """
    Exception raised for errors related to the Command Line Interface (CLI).

    Inherits:
    - Exception: Python's base exception class.

    Usage Example:
    try:
        # Code that may raise CLIException
    except CLIException as e:
        print(f"CLIException occurred: {e}")
    """

    pass

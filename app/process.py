from app.exceptions import DataCaptureException, StatsException


class Stats:
    """
    A class to perform statistical operations on captured data.

    Attributes:
    - capture: DataCapture object containing the captured data.

    Methods:
    - less(value) -> int: Calculates the count of numbers less than the given value.
    - greater(value) -> int: Calculates the count of numbers greater than the given value.
    - between(low, high) -> int: Calculates the count of numbers between the given range.
    """

    def __init__(self, data, counts):
        """
        Initialize Stats object.

        Args:
            data (list): The list of captured data.
            counts (list): Counts of numbers in the captured data.
        """
        self.data = data
        self.counts = counts

    def less(self, value) -> int:
        """
        Get the count of numbers less than a specified value.

        Args:
            value (int): The value to compare against.

        Returns:
            int: Count of numbers less than the specified value.
        """
        if not isinstance(value, (int, float)):
            raise StatsException("Invalid input: Value should be an integer or float.")
        return sum(self.counts[:value])

    def greater(self, value) -> int:
        """
        Get the count of numbers greater than a specified value.

        Args:
            value (int): The value to compare against.

        Returns:
            int: Count of numbers greater than the specified value.
        """
        if not isinstance(value, (int, float)):
            raise StatsException("Invalid input: Value should be an integer or float.")
        return sum(self.counts[value + 1:])

    def between(self, low, high) -> int:
        """
        Get the count of numbers within a specified range.

        Args:
            low (int): The lower bound of the range (inclusive).
            high (int): The upper bound of the range (inclusive).

        Returns:
            int: Count of numbers within the specified range.
        """
        if not isinstance(low, (int, float)) or not isinstance(high, (int, float)):
            raise StatsException(
                "Invalid input: Low and high values should be integers or floats."
            )
        if low >= high:
            raise StatsException(
                "Invalid input: Low value should be less than high value in 'between'."
            )
        return sum(self.counts[low:high + 1])


class DataCapture:
    """
    A class to capture and manipulate data.

    Attributes:
    - numbers: List containing captured numbers.

    Methods:
    - add(num): Adds a number to the captured data list.
    - build_stats() -> Stats: Returns a Stats object for statistical operations.
    """

    def __init__(self):
        """Initialize DataCapture object."""
        self.data = []
        self.counts = [0] * 1001

    def add(self, num):
        """
         Add a new number to the captured data.

         Args:
             num (int): The small positive integer to add.
        """
        if not isinstance(num, (int, float)):
            raise DataCaptureException(
                "Invalid input: Only integers or floats are allowed."
            )
        if num < 0:
            raise DataCaptureException(
                "Invalid input: Only positive numbers are allowed."
            )
        self.data.append(num)
        self.counts[num] += 1

    def build_stats(self) -> Stats:
        """
         Build statistics object based on captured data.

         Returns:
             Stats: A Stats object to query statistics about the captured data.
        """
        return Stats(self.data, self.counts)

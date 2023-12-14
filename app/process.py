from typing import List

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

    def __init__(self, capture):
        """
        Initializes Stats with the provided DataCapture object.

        Args:
        - capture: DataCapture object containing the captured data.
        """
        self.capture = capture

    def less(self, value) -> int:
        """
        Counts the numbers less than the provided value.

        Raises:
        - StatsException: If the value is not an integer or float.

        Returns:
        - int: Count of numbers less than the provided value.
        """
        if not isinstance(value, (int, float)):
            raise StatsException("Invalid input: Value should be an integer or float.")
        return sum(1 for num in self.capture.numbers if num < value)

    def greater(self, value) -> int:
        """
        Counts the numbers greater than the provided value.

        Raises:
        - StatsException: If the value is not an integer or float.

        Returns:
        - int: Count of numbers greater than the provided value.
        """
        if not isinstance(value, (int, float)):
            raise StatsException("Invalid input: Value should be an integer or float.")
        return sum(1 for num in self.capture.numbers if num > value)

    def between(self, low, high) -> int:
        """
        Counts the numbers between the provided range.

        Raises:
        - StatsException: If low or high values are not integers or floats or if low >= high.

        Returns:
        - int: Count of numbers between the provided range.
        """
        if not isinstance(low, (int, float)) or not isinstance(high, (int, float)):
            raise StatsException(
                "Invalid input: Low and high values should be integers or floats."
            )
        if low >= high:
            raise StatsException(
                "Invalid input: Low value should be less than high value in 'between'."
            )
        return sum(1 for num in self.capture.numbers if low < num < high)


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
        """Initializes DataCapture with an empty list to store numbers."""
        self.numbers: List = []

    def add(self, num):
        """
        Adds a number to the captured data list.

        Args:
        - num: Number to be added to the captured data list.

        Raises:
        - DataCaptureException: If the provided input is not an integer or float.
        """
        if not isinstance(num, (int, float)):
            raise DataCaptureException(
                "Invalid input: Only integers or floats are allowed."
            )
        self.numbers.append(num)

    def build_stats(self) -> Stats:
        """
        Creates and returns a Stats object for statistical operations.

        Returns:
        - Stats: A Stats object initialized with the current DataCapture object.
        """
        return Stats(self)

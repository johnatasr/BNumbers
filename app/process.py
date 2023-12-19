from typing import Union

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
        Initialize the Stats object with precomputed cumulative counts.

        Args:
            capture (DataCapture): A DataCapture containing precomputed cumulative counts.
        """
        self.capture = capture

    def less(self, value: Union[int, float]) -> int:
        """
        Calculates the count of numbers less than the given value.

        Args:
            value (Union[int, float]): The value to compare against.

        Returns:
            int: Count of numbers less than the specified value.
        Raises:
            StatsException: If the value is not an integer or float or if an index error occurs.
        """
        if not isinstance(value, (int, float)):
            raise StatsException("Invalid input: Value should be an integer or float.")
        try:
            return self.capture.prefix_sum[value + self.capture.offset]
        except IndexError:
            raise StatsException("An index error occurred in 'less' operation.")

    def greater(self, value: Union[int, float]) -> int:
        """
        Calculates the count of numbers greater than the given value.

        Args:
            value (Union[int, float]): The value to compare against.

        Returns:
            int: Count of numbers greater than the specified value.
        Raises:
            StatsException: If the value is not an integer or float or if an index error occurs.
        """
        if not isinstance(value, (int, float)):
            raise StatsException("Invalid input: Value should be an integer or float.")
        try:
            return (
                self.capture.prefix_sum[2 * self.capture.offset]
                - self.capture.prefix_sum[value + self.capture.offset + 1]
            )
        except IndexError:
            raise StatsException("An index error occurred in 'greater'.")

    def between(self, low: Union[int, float], high: Union[int, float]) -> int:
        """
        Calculates the count of numbers within a specified range.

        Args:
            low (Union[int, float]): The lower bound of the range (inclusive).
            high (Union[int, float]): The upper bound of the range (inclusive).

        Returns:
            int: Count of numbers within the specified range.
        Raises:
            StatsException: If low/high values are not integers or floats or if an index error occurs.
        """
        if not isinstance(low, (int, float)) or not isinstance(high, (int, float)):
            raise StatsException(
                "Invalid input: Low and high values should be integers or floats."
            )
        if low >= high:
            raise StatsException(
                "Invalid input: Low value should be less than high value in 'between'."
            )
        try:
            return (
                self.capture.prefix_sum[high + self.capture.offset + 1]
                - self.capture.prefix_sum[low + self.capture.offset]
            )
        except IndexError:
            raise StatsException("An index error occurred in 'between'.")


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
        """
        Initialize the DataCapture object with counts for captured numbers. Allowed only numbers to 1000
        """
        self.prefix_sum = None
        self.offset = 1000
        self.data = [0] * (2 * self.offset)

    def add(self, num: Union[int, float]):
        """
        Adds a new number to the captured data.

        Args:
            num (Union[int, float]): The small positive integer to add.
        Raises:
            DataCaptureException: If the number is not an integer or float.
            DataCaptureException: If the number is not positive.
        """
        if not isinstance(num, (int, float)):
            raise DataCaptureException(
                "Invalid input: Only integers or floats are allowed."
            )
        if num < 0:
            raise DataCaptureException(
                "Invalid input: Only positive numbers are allowed."
            )
        self.data[num + self.offset] += 1

    def build_stats(self) -> Stats:
        """
        Builds a Stats object for statistical operations.

        Returns:
            Stats: A Stats object for querying statistics about the captured data.
        """
        self.prefix_sum = [0] * (2 * self.offset + 1)
        for i in range(1, 2 * self.offset + 1):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + self.data[i - 1]
        return Stats(self)

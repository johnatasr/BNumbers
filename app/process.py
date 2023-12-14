from typing import List

from app.exceptions import DataCaptureException, StatsException


class Stats:
    def __init__(self, capture):
        self.capture = capture

    def less(self, value) -> int:
        if not isinstance(value, (int, float)):
            raise StatsException("Invalid input: Value should be an integer or float.")
        return sum(1 for num in self.capture.numbers if num < value)

    def greater(self, value) -> int:
        if not isinstance(value, (int, float)):
            raise StatsException("Invalid input: Value should be an integer or float.")
        return sum(1 for num in self.capture.numbers if num > value)

    def between(self, low, high) -> int:
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
    def __init__(self):
        self.numbers: List = []

    def add(self, num):
        if not isinstance(num, (int, float)):
            raise DataCaptureException(
                "Invalid input: Only integers or floats are allowed."
            )
        self.numbers.append(num)

    def build_stats(self) -> Stats:
        if not self.numbers:
            raise DataCaptureException("No numbers to generate statistics.")
        return Stats(self)

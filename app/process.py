from typing import Dict, List


class Stats:
    def __init__(self, capture: object):
        self.capture = capture

    def less(self, value: int):
        return sum(1 for num in self.capture.numbers if num < value)

    def greater(self, value: int):
        return sum(1 for num in self.capture.numbers if num > value)

    def between(self, low: int, high: int):
        return sum(1 for num in self.capture.numbers if low < num < high)


class DataCapture:
    def __init__(self):
        self.counts: Dict = {'less': 0, 'greater': 0, 'within': 0}
        self.numbers: List = []

    def add(self, num):
        self.numbers.append(num)
        if num < self.counts['less']:
            self.counts['less'] += 1
        elif num > self.counts['greater']:
            self.counts['greater'] += 1
        elif self.counts['less'] < num < self.counts['greater']:
            self.counts['within'] += 1

    def build_stats(self) -> Stats:
        return Stats(self)

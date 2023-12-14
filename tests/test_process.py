import pytest

from app.process import DataCapture
from app.exceptions import DataCaptureException


def test_empty_stats():
    capture = DataCapture()
    stats = capture.build_stats()

    assert stats.less(4) == 0
    assert stats.between(3, 6) == 0
    assert stats.greater(4) == 0


def test_single_value_stats():
    capture = DataCapture()
    capture.add(5)
    stats = capture.build_stats()

    assert stats.less(4) == 0
    assert stats.between(3, 6) == 1
    assert stats.greater(4) == 1


def test_negative_numbers():
    with pytest.raises(DataCaptureException) as exp:
        capture = DataCapture()
        capture.add(-3)
        capture.add(-1)
        capture.add(0)
        capture.add(2)
        stats = capture.build_stats()
        stats.less(-2)

    assert str(exp.value) == "Invalid input: Only positive numbers are allowed."


def test_repeated_values():
    capture = DataCapture()
    capture.add(5)
    capture.add(5)
    capture.add(5)
    capture.add(5)
    stats = capture.build_stats()

    assert stats.less(6) == 4
    assert stats.between(4, 6) == 4
    assert stats.greater(4) == 4


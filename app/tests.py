import subprocess
from app.process import DataCapture


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
    assert stats.greater(4) == 0


def test_negative_numbers():
    capture = DataCapture()
    capture.add(-3)
    capture.add(-1)
    capture.add(0)
    capture.add(2)
    stats = capture.build_stats()

    assert stats.less(-2) == 2
    assert stats.between(-2, 1) == 2
    assert stats.greater(1) == 1


def test_repeated_values():
    capture = DataCapture()
    capture.add(5)
    capture.add(5)
    capture.add(5)
    capture.add(5)
    stats = capture.build_stats()

    assert stats.less(6) == 4
    assert stats.between(4, 6) == 4
    assert stats.greater(4) == 0


# CLI tests
def test_add_operation_with_valid_value():
    # Testing adding numbers to DataCapture with valid value
    process = subprocess.run(['python', 'your_script.py', 'add', '--value', '5'], capture_output=True, text=True)
    assert process.stdout.strip() == 'Added 5 to DataCapture.'


def test_add_operation_with_missing_value():
    # Testing adding numbers to DataCapture with missing value
    process = subprocess.run(['python', 'your_script.py', 'add'], capture_output=True, text=True)
    assert process.stdout.strip() == 'CLI Error: Please provide a value to add.'


def test_invalid_command():
    # Testing invalid command scenario
    process = subprocess.run(['python', 'your_script.py', 'invalid'], capture_output=True, text=True)
    assert 'Invalid command' in process.stderr


def test_invalid_argument():
    # Testing invalid argument scenario
    process = subprocess.run(['python', 'your_script.py', 'add', '--value', 'string'], capture_output=True, text=True)
    assert 'Invalid input' in process.stderr

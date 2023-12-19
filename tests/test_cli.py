import pytest

from app.cli import _get_input, _process_add_command, _process_stats_command
from app.process import DataCapture


@pytest.fixture
def capture():
    return DataCapture()


def test_get_input_integer(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "42")
    result = _get_input("Enter value: ")
    assert result == 42


def test_get_input_string(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "test")
    result = _get_input("Enter value: ", str)
    assert result == "test"


def test_process_add_command(capture, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "10")
    _process_add_command(capture)
    assert type(capture.data) is list


@pytest.mark.parametrize(
    "inputs, expected_output",
    [
        (["less", "3"], "Count of numbers less than 3: 2"),
        (["greater", "3"], "Count of numbers greater than 3: 2"),
        (["between", "2", "4"], "Count of numbers between 2 and 4: 3"),
    ],
)
def test_process_stats_command(capture, monkeypatch, capsys, inputs, expected_output):
    for number in range(5):
        capture.add(number + 1)
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    _process_stats_command(capture)
    captured = capsys.readouterr()
    assert captured.out.strip() == f"'{expected_output}'"

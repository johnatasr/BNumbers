from enum import Enum
from pprint import pprint
from typing import Type, Union

from app.process import DataCapture, Stats


class Args(Enum):
    """
    Enumeration representing command options for the CLI.

    Members:
    - ADD: Represents the 'add' command.
    - STATS: Represents the 'stats' command.
    - LESS: Represents the 'less' command.
    - GREATER: Represents the 'greater' command.
    - BETWEEN: Represents the 'between' command.
    """

    ADD = "add"
    STATS = "stats"
    LESS = "less"
    GREATER = "greater"
    BETWEEN = "between"


def _get_input(
    prompt: str, value_type: Union[Type[int], Type[str]] = int
) -> Union[str, int]:
    """
    Get user input from the command line.

    Args:
    - prompt: A string prompt for the user.
    - value_type: Type hint for the input value (int or str).

    Returns:
    - Union[str, int]: The input value, either as a string or integer.
    """
    while True:
        try:
            user_input: str = input(prompt)
            if user_input.lower() == "exit":
                return "exit"

            if value_type == int:
                return int(user_input)
            else:
                return user_input.strip()

        except ValueError:
            pprint("Invalid input. Please enter a valid value.")


def _process_add_command(capture: DataCapture):
    """
    Process the 'add' command.

    Adds a value to the DataCapture object.

    Args:
    - capture: DataCapture object to add the value to.
    """
    value = _get_input("Enter value to add: ")
    capture.add(value)
    pprint(f"Added {value} to DataCapture.")


def _process_stats_command(capture: DataCapture):
    """
    Process the 'stats' command.

    Performs statistical operations based on user inputs.

    Args:
    - capture: DataCapture object to perform statistical operations on.
    """
    stats: Stats = capture.build_stats()
    stat_type: str = _get_input("Enter stats type (less/greater/between): ", str)

    if stat_type == Args.BETWEEN.value:
        low: int = _get_input("Enter low value: ")
        high: int = _get_input("Enter high value: ")
        result: int = stats.between(low, high)
        pprint(f"Count of numbers between {low} and {high}: {result}")
    elif stat_type == Args.LESS.value:
        value: int = _get_input("Enter value for less: ")
        result: int = stats.less(value)
        pprint(f"Count of numbers less than {value}: {result}")
    elif stat_type == Args.GREATER.value:
        value: int = _get_input("Enter value for greater: ")
        result: int = stats.greater(value)
        pprint(f"Count of numbers greater than {value}: {result}")
    else:
        pprint(f"Invalid command. {stat_type}")
        _process_stats_command(capture)


def start_cli():
    """
    Start the Command Line Interface (CLI) application.

    Allows users to interact with the DataCapture object by entering commands.
    """
    pprint("----- BNumbers CLI -------")

    # Call DataCapture Object
    capture = DataCapture()

    while True:
        command: str = _get_input("Enter command (add/stats/exit): ", str)

        if command == "exit":
            break
        elif command == Args.ADD.value:
            _process_add_command(capture)
        elif command == Args.STATS.value:
            _process_stats_command(capture)
        else:
            pprint("Invalid command.")
            continue

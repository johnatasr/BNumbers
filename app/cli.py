from app.process import DataCapture
from app.exceptions import MissingValueError, CLIException
from pprint import pprint


def start_cli(args):
    capture = DataCapture()
    try:
        if args.operation == 'add':
            if args.value is None:
                raise MissingValueError("Please provide a value to add.")
            capture.add(args.value)
            pprint(f"Added {args.value} to DataCapture.")
        elif args.operation == 'stats':
            stats = capture.build_stats()
            if args.value is not None:
                if args.value == 'less':
                    result = stats['less'](args.value)
                    pprint(f"Count of numbers less than {args.value}: {result}")
                elif args.value == 'greater':
                    result = stats['greater'](args.value)
                    pprint(f"Count of numbers greater than {args.value}: {result}")
                else:
                    low, high = map(int, args.value.split(','))
                    result = stats['between'](low, high)
                    pprint(f"Count of numbers between {low} and {high}: {result}")
    except CLIException as e:
        pprint(f"CLI Error: {e}")


def start_interactively():
    while True:
        command = input("Enter command (add/stats): ")
        if command == 'exit':
            break
        elif command not in ['add', 'stats']:
            pprint("Invalid command.")
            continue

        value, low, high = None, None, None

        if command == 'add':
            value = int(input("Enter value to add: "))
        elif command == 'stats':
            stat_type = input("Enter stats type (less/greater/between): ")
            if stat_type not in ['less', 'greater', 'between']:
                pprint("Invalid stats type.")
                continue
            if stat_type == 'between':
                low = int(input("Enter low value: "))
                high = int(input("Enter high value: "))

        capture = DataCapture()

        try:
            if command == 'add':
                if value is None:
                    raise MissingValueError("Please provide a value to add.")
                capture.add(value)
                pprint(f"Added {value} to DataCapture.")
            elif command == 'stats':
                stats = capture.build_stats()
                if value is not None:
                    if value == 'less':
                        result = stats['less'](int(input("Enter value for less: ")))
                        pprint(f"Count of numbers less than {value}: {result}")
                    elif value == 'greater':
                        result = stats['greater'](int(input("Enter value for greater: ")))
                        pprint(f"Count of numbers greater than {value}: {result}")
                    else:
                        if low is None or high is None:
                            raise MissingValueError("Please provide both low and high values for between.")
                        result = stats['between'](int(low), int(high))
                        pprint(f"Count of numbers between {low} and {high}: {result}")

            again = input("Do you want try again ? [y,n]")

            if again.lower() in ["yes", "y"]:
                start_interactively()
            else:
                return

        except CLIException as e:
            pprint(f"CLI Error: {e}")

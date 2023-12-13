from app.cli import start_cli, start_interactively
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='DataCapture Numbers CLI')
    parser.add_argument('operation', choices=['add', 'stats'], help='Operation to perform')
    parser.add_argument('--value', help='Value for the operation')
    parser.add_argument("--exec", help="Execute the application in one shot")

    args = parser.parse_args()

    while True:
        if args.exec:
            start_cli(args)
            break

        start_interactively(args)

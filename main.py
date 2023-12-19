from app.cli import start_cli
from app.process import DataCapture
from pprint import pprint

if __name__ == "__main__":
    """
    Entry point of the application.
    
    If executed as the main module:
    - The CLI is initiated by calling 'start_cli()' to interactively process commands.
    
    Usage Examples:
    - You can also directly use the 'process' module for testing purposes:
    """
    # Uncomment the lines below to test without CLI:
    # Test the code
    # capture = DataCapture()
    # capture.add(1)
    # capture.add(1)
    # capture.add(2)
    # capture.add(3)
    # capture.add(4)
    # capture.add(5)
    # capture.add(10)
    # capture.add(6)
    # stats = capture.build_stats()
    # pprint(stats.less(0))  # should return 0
    # pprint(stats.greater(1))  # should return 6
    # pprint(stats.between(2, 5))  # should return 4

    start_cli()

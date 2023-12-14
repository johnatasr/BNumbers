from app.cli import start_cli
# from app.process import DataCapture

if __name__ == "__main__":
    """
    Entry point of the application.
    
    If executed as the main module:
    - The CLI is initiated by calling 'start_cli()' to interactively process commands.
    
    Usage Examples:
    - You can also directly use the 'process' module for testing purposes:
    """
    # Uncomment the lines below and DataCapture import to test without CLI:
    # capture = DataCapture()
    # capture.add(5)
    # capture.add(10)
    # capture.add(8)
    #
    # stats = capture.build_stats()
    # pprint(stats.less(11))

    start_cli()

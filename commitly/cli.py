import argparse
from .main import run

def main():
    """
    The main entry point for the Commitly CLI.
    """
    parser = argparse.ArgumentParser(
        description="Generate a Git commit message using AI."
    )
    # Will Add arguments like --type, --edit here later.
    args = parser.parse_args()

    # Execute the main application logic
    run()

if __name__ == "__main__":
    main()
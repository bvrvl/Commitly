import argparse
from .main import run

def main():
    """
    The main entry point for the Commitly CLI.
    """
    parser = argparse.ArgumentParser(
        description="Generate a Git commit message using AI."
    )
    parser.add_argument(
        '--edit',
        '-e', # Add a convenient shortcut
        action='store_true', # Makes it a flag, e.g., `commitly --edit`
        help="Open the generated message in your default editor before committing."
    )
    args = parser.parse_args()

    # Pass the parsed arguments to the main run function
    run(args)

if __name__ == "__main__":
    main()
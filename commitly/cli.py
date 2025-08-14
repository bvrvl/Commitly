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
        '-e',
        action='store_true',
        help="Open the generated message in your default editor before committing."
    )
    parser.add_argument(
        '--type',
        '-t',
        type=str,
        choices=['feat', 'fix', 'docs', 'style', 'refactor', 'test', 'chore'],
        help="Force a specific commit type for the message."
    )
    args = parser.parse_args()

    run(args)

if __name__ == "__main__":
    main()
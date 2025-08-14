import subprocess
import sys

def get_staged_diff():
    """
    Retrieves the staged changes (diff) from the Git repository.

    Returns:
        str: The git diff output, or None if an error occurs or the diff is empty.
    """
    try:
        # The command to get staged changes
        command = ["git", "diff", "--cached"]

        # Execute the command
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
            encoding='utf-8' # Ensure consistent encoding
        )

        # Return the output if there are any changes
        if result.stdout:
            return result.stdout
        else:
            print("No staged changes found. Use 'git add' to stage your files.")
            return None

    except FileNotFoundError:
        print("Error: 'git' command not found. Is Git installed and in your PATH?")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running git diff: {e.stderr}")
        sys.exit(1)


def commit(message: str):
    """
    Commits the staged changes with the given message.

    Args:
        message (str): The commit message.
    """
    try:
        # Using -m flag expects the entire message as a single argument.
        # For multi-line messages, we pass it as one string.
        subprocess.run(
            ["git", "commit", "-m", message],
            check=True,
            encoding='utf-8'
        )
        print("✅ Commit created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during commit: {e.stderr}", file=sys.stderr)
        sys.exit(1)
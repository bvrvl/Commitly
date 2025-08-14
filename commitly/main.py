from .git_utils import get_staged_diff, commit
from .ai_client import generate_commit_message
import sys

def get_user_choice():
    """Prompts the user for their choice and returns it."""
    while True:
        choice = input("Accept, Edit, or Regenerate? [A/E/R]: ").upper()
        if choice in ['A', 'E', 'R']:
            return choice
        print("Invalid choice. Please enter 'A', 'E', or 'R'.")


def run():
    """
    Main function to run the commit message generation and interaction process.
    """
    diff = get_staged_diff()
    if not diff:
        print("Exiting.")
        sys.exit(0)

    commit_message = None
    while True:
        if not commit_message:
            print("⏳ Generating commit message with AI...")
            commit_message = generate_commit_message(diff)
            print("\nSuggested commit:\n")
            print("----------------------------------------")
            print(commit_message)
            print("----------------------------------------")

        choice = get_user_choice()

        if choice == 'A':
            # Accept and commit
            commit(commit_message)
            break
        elif choice == 'R':
            # Regenerate
            commit_message = None # Clear the message to trigger regeneration
            print("\n🔄 Regenerating...")
            continue
        elif choice == 'E':
            # Edit
            # A real editor integration will be added in a future step.
            print("\nEditing is not yet implemented. Please manually edit the commit for now:")
            print("git commit -m \"Your message\"")
            break # Exit the loop
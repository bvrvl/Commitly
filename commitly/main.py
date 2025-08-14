from .git_utils import get_staged_diff, commit
from .ai_client import generate_commit_message
from .editor import open_in_editor
import sys

def get_user_choice():
    """Prompts the user for their choice and returns it."""
    while True:
        choice = input("Accept, Edit, or Regenerate? [A/E/R]: ").upper()
        if choice in ['A', 'E', 'R']:
            return choice
        print("Invalid choice. Please enter 'A', 'E', or 'R'.")

def run(args):
    """
    Main function to run the commit message generation and interaction process.
    """
    diff = get_staged_diff()
    if not diff:
        print("Exiting.")
        sys.exit(0)

    commit_message = None
    is_editing_flow = args.edit

    while True:
        if not commit_message:
            print("⏳ Generating commit message with AI...")
            commit_message = generate_commit_message(diff)
            print("\nSuggested commit:\n")
            print("----------------------------------------")
            print(commit_message)
            print("----------------------------------------")

        if is_editing_flow:
            edited_message = open_in_editor(commit_message)
            if not edited_message:
                print("Aborting commit due to empty message.")
                break
            commit(edited_message)
            break

        choice = get_user_choice()

        if choice == 'A':
            commit(commit_message)
            break
        elif choice == 'R':
            commit_message = None
            print("\n🔄 Regenerating...")
            continue
        elif choice == 'E':
            is_editing_flow = True
            continue
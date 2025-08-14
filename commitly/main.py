from .git_utils import get_staged_diff
from .ai_client import generate_commit_message

def run():
    """
    Main function to run the commit message generation process.
    """
    diff = get_staged_diff()

    if diff:
        print("⏳ Generating commit message with AI...")
        commit_message = generate_commit_message(diff)
        print("\nSuggested commit:\n")
        print("----------------------------------------")
        print(commit_message)
        print("----------------------------------------")
    else:
        print("Exiting.")

if __name__ == "__main__":
    run()
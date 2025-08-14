from .git_utils import get_staged_diff

def run():
    """
    Main function to run the commit message generation process.
    """
    diff = get_staged_diff()

    if diff:
        print("----- Staged Diff -----")
        print(diff)
        print("-----------------------")
    else:
        print("Exiting.")

if __name__ == "__main__":
    run()
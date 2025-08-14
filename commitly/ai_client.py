import os
import google.generativeai as genai
from dotenv import load_dotenv

def configure_api():
    """Loads API key from .env and configures the Gemini API."""
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found. Please set it in your .env file.")
    genai.configure(api_key=api_key)

def generate_commit_message(diff: str, commit_type: str = None) -> str:
    """
    Generates a commit message using the Gemini API.

    Args:
        diff (str): The staged git diff.
        commit_type (str, optional): The type of commit to generate.

    Returns:
        str: The generated commit message.
    """
    configure_api()
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Dynamically change the main instruction based on whether a type was provided
    if commit_type:
        prompt_instruction = f"Your task is to write a high-quality Git commit message with the type '{commit_type}'."
    else:
        prompt_instruction = "Your task is to write a high-quality Git commit message, automatically detecting the correct type from the following list: feat, fix, docs, style, refactor, test, chore."

    prompt = f"""
    As an expert software developer, {prompt_instruction}
    Analyze the following git diff and generate a concise, professional commit message that follows the Conventional Commits specification.

    The commit message must start with the type, followed by a colon and a space.
    The title should be succinct (max 50 chars).
    If necessary, provide an optional body explaining the 'what' and 'why' of the changes.

    Do not include any extra text, commentary, or the 'git commit -m' command.

    Git Diff:
    ```diff
    {diff}
    ```
    """

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating commit message: {e}"
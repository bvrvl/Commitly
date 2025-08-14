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

def generate_commit_message(diff: str) -> str:
    """
    Generates a commit message using the Gemini API.

    Args:
        diff (str): The staged git diff.

    Returns:
        str: The generated commit message.
    """
    configure_api()
    model = genai.GenerativeModel('gemini-1.5-flash')

    prompt = f"""
    As an expert software developer, your task is to write a high-quality Git commit message.
    Analyze the following git diff and generate a concise, professional commit message that follows the Conventional Commits specification.

    The commit message should have a clear and succinct title (max 50 chars).
    If necessary, provide an optional body explaining the 'what' and 'why' of the changes.

    Do not include any explanatory text like "Here is the commit message:", backticks, or the 'git commit -m' command itself.

    Git Diff:
    ```diff
    {diff}
    ```
    """

    try:
        response = model.generate_content(prompt)
        # Clean up the response to ensure it's just the message.
        return response.text.strip()
    except Exception as e:
        return f"Error generating commit message: {e}"
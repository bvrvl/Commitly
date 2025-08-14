import os
import google.generativeai as genai
from dotenv import load_dotenv

def configure_api():
    """Loads API key from .env and configures the Gemini API."""
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        # This is the friendly message for new users
        print("--- Welcome to Git-Scribe! ---")
        print("To get started, you need a Gemini API key.")
        print("1. Get your key from Google AI Studio: https://aistudio.google.com/app/apikey")
        print("2. In your project's root directory, create a file named .env")
        print("3. Add the following line to the .env file, replacing with your actual key:")
        print("\nGEMINI_API_KEY=\"YOUR_API_KEY_HERE\"\n")
        raise ValueError("API key configuration not found.")

    genai.configure(api_key=api_key)

def generate_commit_message(diff: str, commit_type: str = None, history: str = None, language: str = 'English') -> str:
    """
    Generates a commit message using the Gemini API.

    Args:
        diff (str): The staged git diff.
        commit_type (str, optional): The type of commit to generate.
        history (str, optional): A string of recent commit messages.
        language (str, optional): The target language for the message.

    Returns:
        str: The generated commit message.
    """
    configure_api()
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Build the prompt dynamically
    prompt_parts = [
        "As an expert software developer, your task is to write a high-quality Git commit message."
    ]
    if commit_type:
        prompt_parts.append(f"The commit message must have the type '{commit_type}'.")
    else:
        prompt_parts.append("Automatically detect the correct commit type from this list: feat, fix, docs, style, refactor, test, chore.")

    prompt_parts.append(f"The commit message must be written in {language}.")
    prompt_parts.append("Analyze the following git diff and generate a concise, professional commit message that follows the Conventional Commits specification.")
    
    if history:
        prompt_parts.append("\nFor context, here are the last few commit messages:")
        prompt_parts.append(f"```\n{history}\n```")

    prompt_parts.append("\nGit Diff:")
    prompt_parts.append(f"```diff\n{diff}\n```")

    prompt_parts.append("\nDo not include any extra text, commentary, or the 'git commit -m' command in your response. Just provide the raw commit message.")

    prompt = "\n".join(prompt_parts)

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating commit message: {e}"
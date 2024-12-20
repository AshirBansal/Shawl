import re

def strip_formatting(text):
    """
    Removes bolding and header formatting from the text.
    """
    # Remove bolding asterisks
    text = text.replace("**", "")

    # Remove headers (e.g., "## Header")
    text = re.sub(r"#{2,}\s*(.*?)\n", "", text)

    return text
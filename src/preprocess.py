import re

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    # ... (any other preprocessing steps here)
    return text


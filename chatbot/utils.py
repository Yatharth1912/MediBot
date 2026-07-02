import re
import json
import os

def preprocess_text(text):
    """Clean and normalize user input"""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s]', '', text)  # remove punctuation
    text = re.sub(r'\s+', ' ', text)     # remove extra spaces
    return text


def load_json(filepath):
    """Safely load JSON file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: {filepath} not found!")
        return {}
    except json.JSONDecodeError:
        print(f"Warning: {filepath} has invalid JSON!")
        return {}
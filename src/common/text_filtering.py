#\src\common\text_filtering.py

import re
import string

def remove_special_characters(text):
    """
    Removes special characters from the given text.
    """
    # Define the pattern for special characters
    pattern = r"[^\w\s]"
    
    # Remove special characters using regex
    filtered_text = re.sub(pattern, "", text)
    
    return filtered_text

def remove_punctuation(text):
    """
    Removes punctuation from the given text.
    """
    # Remove punctuation using string.punctuation
    filtered_text = text.translate(str.maketrans("", "", string.punctuation))
    
    return filtered_text

def lowercase(text):
    """
    Converts the given text to lowercase.
    """
    filtered_text = text.lower()
    
    return filtered_text

def filter_text(text):
    """
    Filters the given text by applying various filtering steps.
    """
    # Apply preprocessing steps
    filtered_text = remove_special_characters(text)
    filtered_text = remove_punctuation(filtered_text)
    filtered_text = lowercase(filtered_text)
    
    return filtered_text

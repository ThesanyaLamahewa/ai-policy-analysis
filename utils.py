# utils.py
# This file cleans and prepares policy text before summarization

import re
import nltk

# Download required NLTK data (only runs once)
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('punkt_tab', quiet=True)

from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords


def clean_text(text):
    """Cleans raw policy text by removing noise."""
    
    # Remove page numbers
    text = re.sub(r'\bPage\s+\d+\b', '', text, flags=re.IGNORECASE)
    
    # Remove extra whitespace and newlines
    text = re.sub(r'\s+', ' ', text)
    
    # Remove special characters but keep punctuation
    text = re.sub(r'[^\w\s\.\,\!\?\;\:\-\(\)]', '', text)
    
    # Strip leading/trailing spaces
    text = text.strip()
    
    return text


def split_into_sentences(text):
    """Splits cleaned text into a list of sentences."""
    
    sentences = sent_tokenize(text)
    
    # Remove very short sentences — they are usually just headings
    sentences = [s for s in sentences if len(s.split()) >= 10]
    
    return sentences


def get_stopwords():
    """Returns English stopwords to ignore during scoring."""
    return set(stopwords.words('english'))
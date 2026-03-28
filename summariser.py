# summariser.py
# This module performs two-layer policy summarization
# Layer 1: Extractive - NLP finds the most important sentences
# Layer 2: Abstractive - AI rewrites them into a clean summary
# Improvement: Sentence scores are normalized by length for better accuracy

import spacy
from collections import Counter
from utils import clean_text, split_into_sentences, get_stopwords

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")


def score_sentences(sentences):
    """
    Scores each sentence based on keyword frequency.
    IMPROVED: Normalized by sentence length to avoid bias toward longer sentences.
    This is the core NLP technique — Frequency-Based Extractive Summarization.
    """
    # Step 1: Join all sentences into one text for analysis
    full_text = ' '.join(sentences)

    # Step 2: Process with spaCy
    doc = nlp(full_text)

    # Step 3: Count word frequencies (ignoring stopwords and punctuation)
    stop_words = get_stopwords()
    word_frequencies = Counter()

    for token in doc:
        word = token.text.lower()
        if word not in stop_words and token.is_alpha:
            word_frequencies[word] += 1

    # Step 4: Normalize frequencies (divide by the highest frequency)
    max_frequency = max(word_frequencies.values()) if word_frequencies else 1
    for word in word_frequencies:
        word_frequencies[word] /= max_frequency

    # Step 5: Score each sentence — normalized by sentence length
    # This prevents long sentences from always winning unfairly
    sentence_scores = {}
    for sentence in sentences:
        score = 0
        word_count = 0
        for token in nlp(sentence):
            word = token.text.lower()
            if word in word_frequencies:
                score += word_frequencies[word]
                word_count += 1
        # Divide by word count to normalize by length
        if word_count > 0:
            sentence_scores[sentence] = score / word_count
        else:
            sentence_scores[sentence] = 0

    return sentence_scores


def extractive_summarize(text, num_sentences=10):
    """
    Picks the top N most important sentences from the policy.
    This is purely NLP-based — no AI involved here.
    """
    # Clean the text first
    cleaned = clean_text(text)

    # Split into sentences
    sentences = split_into_sentences(cleaned)

    if not sentences:
        return []

    # Score all sentences
    scores = score_sentences(sentences)

    # Sort by score and pick the top sentences
    top_sentences = sorted(scores, key=scores.get, reverse=True)[:num_sentences]

    # Return them in original document order for readability
    ordered = [s for s in sentences if s in top_sentences]

    return ordered


def extract_text_from_pdf(pdf_path):
    """
    Reads and extracts all text from a PDF file.
    """
    import fitz  # PyMuPDF library

    doc = fitz.open(pdf_path)
    full_text = ""

    for page in doc:
        full_text += page.get_text()

    doc.close()
    return full_text


def extract_keywords(sentences, top_n=15):
    """
    Extracts the most important keywords from the policy sentences.
    Uses spaCy NLP to filter out stopwords and short words.
    Returns top N keywords with their frequency counts.
    """
    stop_words = get_stopwords()
    all_text = ' '.join(sentences)
    doc = nlp(all_text)

    keywords = Counter()
    for token in doc:
        if (token.is_alpha and
                token.text.lower() not in stop_words and
                len(token.text) > 3):
            keywords[token.text.lower()] += 1

    return keywords.most_common(top_n)
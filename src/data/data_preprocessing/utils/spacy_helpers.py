import spacy
from typing import List
import pandas as pd

nlp_model = spacy.load('en_core_web_sm')


def text_to_tokens_text(text: str) -> List[str]:
    """Tokenize a text into a list of strings using the spacy model."""
    tokens_with_attributes = nlp_model(text)
    tokens_text = [token.text for token in tokens_with_attributes]

    return tokens_text


def get_lemmatized_text(text: str) -> str:
    """Tokenize a text and return tokens and relevant attributes"""
    doc = nlp_model(text)

    tokens = [t.lemma_ for t in doc]

    lemmatized_text = ' '.join(tokens)
    return lemmatized_text


def is_stop_word(token_word):
    """Return True if word is not stop word."""
    lexeme = nlp_model.vocab[token_word]

    if lexeme.is_stop is False:
        return True

    return False


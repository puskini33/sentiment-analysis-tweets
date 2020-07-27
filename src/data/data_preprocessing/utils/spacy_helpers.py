import spacy
from typing import List


nlp_model = spacy.load('en_core_web_sm')


def remove_unnecessary_pos(text: str) -> str:
    """Function keeps only substantive, verbs, adjectives."""
    tokens_with_attributes = nlp_model(text)
    tokens_text = [token.text for token in tokens_with_attributes if (token.pos_ == 'VERB') or
                   (token.pos_ == 'NOUN') or (token.pos_ == 'ADV')or (token.pos_ == 'ADJ')]
    text_with_pos = ' '.join(tokens_text)

    return text_with_pos


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
    """Return True if word is stop word."""
    lexeme = nlp_model.vocab[token_word]

    if lexeme.is_stop is True:
        return True

    return False


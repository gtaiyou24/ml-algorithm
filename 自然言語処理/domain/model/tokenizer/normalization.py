import re
import unicodedata

import nltk
from nltk.corpus import wordnet


def normalize(text: str) -> str:
    normalized_text = normalize_unicode(text)
    normalized_text = normalize_number(normalized_text)
    normalized_text = lower_text(normalized_text)
    return normalized_text


def lower_text(text: str) -> str:
    """小文字に変換."""
    return text.lower()


def normalize_unicode(text: str, form='NFKC') -> str:
    """unicode正規化."""
    normalized_text = unicodedata.normalize(form, text)
    return normalized_text


def lemmatize_term(term, pos=None):
    """単語の見出し語化."""
    if pos is None:
        synsets = wordnet.synsets(term)
        if not synsets:
            return term
        pos = synsets[0].pos()
        if pos == wordnet.ADJ_SAT:
            pos = wordnet.ADJ
    return nltk.WordNetLemmatizer().lemmatize(term, pos=pos)


def normalize_number(text: str) -> str:
    """
    pattern = r'\d+'
    replacer = re.compile(pattern)
    result = replacer.sub('0', text)
    """
    # 連続した数字を0で置換
    replaced_text = re.sub(r'\d+', '0', text)
    return replaced_text

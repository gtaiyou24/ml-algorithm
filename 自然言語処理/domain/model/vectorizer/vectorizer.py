"""
vectorizer = Vectorizer('/usr/local/lib/mecab/dic/mecab-ipadic-neologd', '/path/to/stop_word.txt')

train_doc_ser = pd.Series([])
transform_doc_ser = pd.Series([])
vectorizer.fit(train_doc_ser)
文書ベクトル = vectorizer.transform(transform_doc_ser)
"""
import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer

from domain.model.tokenizer.cleaning import clean_text, clean_url, clean_html_and_js_tags
from domain.model.tokenizer.normalization import normalize, lemmatize_term
from domain.model.tokenizer.tokenizer import MeCabTokenizer
from domain.model.tokenizer.stopwords import maybe_download, create_stopwords


class Vectorizer:

    def __init__(self, tokenizer_path: str, stopwords_path: str):
        self.tokenizer = MeCabTokenizer(tokenizer_path)
        maybe_download(stopwords_path)
        self.stop_words = create_stopwords(stopwords_path)
        self.vectorizer = TfidfVectorizer(stop_words=self.stop_words, min_df=0)

    def fit(self, doc_ser: pd.Series):
        self.vectorizer.fit(self.preprocessing(doc_ser))
        return

    def transform(self, doc_ser: pd.Series):
        return self.vectorizer.transform(self.preprocessing(doc_ser)).toarray()

    def preprocessing(self, doc_ser: pd.Series):
        """前処理"""
        doc_ser = self.cleaning(doc_ser)
        words_list = self.tokenize(doc_ser)
        normalized_words_list = self.normalize(words_list)
        return np.array([' '.join(words) for words in normalized_words_list])

    def cleaning(self, doc_ser: pd.Series) -> pd.Series:
        """テキストのクリーニング"""
        return doc_ser.map(lambda doc: self._cleaning(str(doc)))

    def _cleaning(self, text: str) -> str:
        cleaned_text = clean_text(text)
        cleaned_text = clean_url(cleaned_text)
        cleaned_text = clean_html_and_js_tags(cleaned_text)
        return cleaned_text

    def tokenize(self, doc_ser: pd.Series) -> list:
        """形態素解析"""
        return [[token.surface for token in self.tokenizer.filter_by_pos(doc, ('名詞',))] for doc in doc_ser]

    def normalize(self, words_list: list) -> list:
        """単語の正規化"""
        normalized_words_list = []
        for words in words_list:
            words = [normalize(word) for word in words]
            words = [lemmatize_term(word) for word in words]
            normalized_words_list.append(words)

        return normalized_words_list
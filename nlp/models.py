from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd
from typing import List

class LoadData:

    def __init__(self, corpus: pd.DataFrame) -> None:
        self.corpus = corpus

    def binary(self, ngram:List):
        binary_vectorizer = CountVectorizer()
        pass

    def frequency(self, ngram:List):
        frequency_vectorizer = CountVectorizer()
        pass

    def tfidf(self, ngram:List):
        tfidf__vectorizer = TfidfVectorizer()
        pass
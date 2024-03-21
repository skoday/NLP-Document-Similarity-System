from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
from typing import List
import re
import numpy as np

class Create_model:

    def __init__(self, corpus: pd.DataFrame, ngrams: int) -> None:
        self.ngrams = ngrams
        self.corpus = corpus.copy()
        self.corpus["Título-Contenido"] = self.corpus["Título"] + " - " + self.corpus["Contenido"]
        self.token_pattern = r'\w+|[^\w\s]|\d+(?:\.\d+)?%?'

    def binary(self, ngram:List):
        binary_vectorizer = CountVectorizer(binary=True, token_pattern=self.token_pattern, ngram_range = (self.ngrams,self.ngrams))
        return binary_vectorizer.fit(self.corpus)

    def frequency(self, ngram:List):
        frequency_vectorizer = CountVectorizer(token_pattern=self.token_pattern, ngram_range = (self.ngrams,self.ngrams))
        return frequency_vectorizer.fit(self.corpus)

    def tfidf(self, ngram:List):
        tfidf__vectorizer = TfidfVectorizer(token_pattern=self.token_pattern, ngram_range = (self.ngrams,self.ngrams))
        return tfidf__vectorizer.fit(self.corpus)
    
class Adjust_Document:

    def __init__(self, model, documet, corpus, compare) -> None:
        self.model = model
        self.document = documet
        self.corpus = corpus
        self.compare = compare
        self.feature_vectors = model.transform(self.corpus[compare]) #self corpues es un Dframe
        self.features_document = model.transform(self.document)

    def compare_documents(self):

        similarities_list = []

        for element in self.features_document.toarray():
            similarities = cosine_similarity(self.feature_vectors, [element])
            similarities = np.array(similarities)
            similarities.sort()
            similarities = similarities[::-1]

            similarities_list.append(similarities[:10])

        return similarities_list
        
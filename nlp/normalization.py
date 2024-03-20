import pandas as pd
import spacy

class Normalization:

    def __init__(self, data) -> None:
        self.data = data
        self.nlp = spacy.load("es_core_news_sm")
        self.stopwords = ["DET", "ADP", "CCONJ", "PRON"]

    def normalize(self):
        if isinstance(self.data, pd.Series):
            print("Normalizando serie")
            normalized_input = self.normalize_series()
            return normalized_input

        if isinstance(self.data, pd.DataFrame):
            print("Normalizando df")
            normalized_input = self.normalize_dataframe()
            return normalized_input
    
    def normalize_series(self):
        aux_data = self.data.copy()
        aux_data = aux_data.apply(self.traverse_entity)
        return aux_data

    def normalize_dataframe(self):
        aux_data = self.data.copy()
        aux_data["Documento"] = aux_data["Documento"].apply(self.nlp)
        aux_data["Documento"] = aux_data["Documento"].apply(self.traverse_entity)
        return aux_data

    def traverse_entity(self, doc):
            result = " "
            for item in doc:
                if item.pos_ not in self.stopwords:
                    #result.append(item.lemma_)
                    result = result + item.lemma_ + " "
            return result.strip()
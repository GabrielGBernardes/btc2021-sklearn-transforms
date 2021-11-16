import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class EncodeColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        data = X.copy()       
        return pd.get_dummies(data=data, columns=self.columns)
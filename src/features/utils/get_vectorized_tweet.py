from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import TfidfVectorizer
from pandas import DataFrame


# Compute n grams from a dataframe for a given variable
class Ngrams(BaseEstimator, TransformerMixin):

    def __init__(self, df):
        pass

    def transform(self, df: DataFrame):
        # Save name of column to analyze
        name = df.columns
        vectorized_tweet = TfidfVectorizer(strip_accents='unicode', use_idf=True,
                                           stop_words='english', analyzer='word',
                                           ngram_range=(2, 4), max_features=100)

        # Fit to data
        x_train = vectorized_tweet.fit_transform(df[name[0]].values.astype(str))
        # X_train = X_train.toarray()
        # is this needed? how do I address mismatching shape problem

        # Return sparse matrix
        return x_train

    def fit(self, df, y=None):
        ### Unless error returns self
        return self
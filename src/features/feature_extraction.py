"""# sklearn implementation of TF-IDF
vectorizer = TfidfVectorizer(ngram_range=(2, 3), max_features=100)
vectors = vectorizer.fit_transform(company_files)
feature_names = vectorizer.get_feature_names()
dense = vectors.todense()
denselist = dense.tolist()
df_tf_idf = pd.DataFrame(denselist, columns=feature_names,
                         index=['Uline', 'Home_Depot', 'Taco_Bell', 'Bang_Energy', 'Patagonia', 'Microsoft',
                                'Merriam_Webster', 'Fox_News', 'CNN'])

# TODO: for feature extraction: call to the variable values

# Write df to file
tf_idf_file = get_processed_path_file('tf_idf_feature_extraction')
create_file_with_headers(tf_idf_file, [])
df_tf_idf.to_csv(tf_idf_file)

rare_words_bigger_than_0 = []
rare_words_bigger_than_001 = []
# Get the scores that are  > 0 for all 5 companies
for header in list(df_tf_idf.columns.values):  # TODO: Ask here
    values = []
    for index, row in df_tf_idf.iterrows():
        values.append(row[header])
    if (values[0] > 0) and (values[1] > 0) and (values[2] > 0) and (values[3] > 0) and (values[4] > 0):  # if all values are bigger that 0
        rare_words_bigger_than_0.append(header)

    else:
        values = []

print(rare_words_bigger_than_0)
print(len(rare_words_bigger_than_0))"""

# Code from https://towardsdatascience.com/natural-language-processing-feature-engineering-using-tf-idf-e8b9d00e7e76

from sklearn.feature_extraction.text import TfidfVectorizer
from src.data.file_preparation.prepare_data_file import get_processed_path_file, create_file_with_headers, write_to_csv
from src.data.data_preprocessing.utils.spacy_helpers import text_to_tokens_text
import pandas as pd
import csv


labeled_tweet = {'tweet': '', 'label': ''}

processed_file_path = get_processed_path_file('labeled_data')

with open(processed_file_path, 'r', encoding='utf-8', newline='') as file:
    labeled_df = pd.read_csv(file)

# Random Selection from negative tweets
df_with_all_negative_tweets = labeled_df.loc[(labeled_df['label'] == 'negative')]

df_negative_final = df_with_all_negative_tweets.apply(lambda x: x.sample(n=18382, random_state=1))


df_positive_final = labeled_df.loc[(labeled_df['label'] == 'positive')]

df_tweets = pd.concat([df_negative_final, df_positive_final])  # df with equal number of positive and negative tweets


from pathlib import Path
import os.path

import warnings

warnings.filterwarnings("ignore")

### Import packages for data manipulation

import pandas as pd
import numpy as np
import re

### Import packages to visualize data
import matplotlib.pyplot as plt
import seaborn as sns

### Import packages for feature extraction

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import TfidfVectorizer

### Import packages for modeling
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
### from xgboost import XGBClassifier

### Import packages for model selection and performance assessment
from sklearn import model_selection
from sklearn.model_selection import train_test_split, KFold, StratifiedKFold, cross_val_score, RandomizedSearchCV, \
    GridSearchCV, learning_curve
from sklearn.metrics import accuracy_score, log_loss, classification_report, precision_recall_fscore_support
from sklearn.metrics import roc_curve, roc_auc_score, confusion_matrix, mean_squared_error, f1_score
from pandas import DataFrame
from src.features.utils.get_vectorized_tweet import Ngrams


# Print data set for overview
# print(df_tweets.head())
# print(df_tweets.info())


# Define function to count number of words in a tweet
def word_counter(tweet: str) -> int:
    count = len(re.findall(r'\w+', str(tweet)))
    return count


# Feature Extraction Script
# Get word count of tweets
df_tweets['number_of_words'] = df_tweets['text'].apply(word_counter)

# Make labels numeric
# df_tweets['label'] = df_tweets.cat.codes

# Split into predictors and outcome data
y = df_tweets['label']
x = df_tweets.drop(
    ['label', 'number_of_words'], axis=1).values



# TODO: put in another folder: training data
# Split into train and test data
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
# TODO: same number of positive and negative
print(X_train.shape)
print(X_test)
print(y_train.shape)
print(y_test)




# Model selection process: Create list of different classifiers/algorithms to try out

classifiers = [
    KNeighborsClassifier(),
    RandomForestClassifier(random_state=1),
    GradientBoostingClassifier(random_state=1)
    ## XGBClassifier(random_state=1)
]

#Model selection process: Loop through the different classifiers using the pipeline

for classifier in classifiers:
    model_pipeline = Pipeline([
        ('feats', FeatureUnion([
            # Ngrams
            ('ngram_all', Ngrams(X_train[['text']]))])),
        # Classifier
        ('classifier', classifier)])
    model_pipeline.fit(X_train, y_train)
    y_predict = model_pipeline.predict(X_test)
    print(classifier)
    print(y_predict)
    print("model score: %.3f" % model_pipeline.score(y_predict, y_test))

#confusion_matrix(y_test, grid_search.predict(X_test))

#confm_hold = confusion_matrix(y_test, y_predict)
#print(confm_hold)

# np.array(s)
## confm_hold_df = pd.DataFrame(confm_hold, index = ['No Medal', 'Medal'],
# columns = ['No Medal', 'Medal'])
## plt.figure(figsize=(5,4))
## sns.heatmap(confm_hold_df, annot=True, fmt=".4f", linewidths=.5, square = True)

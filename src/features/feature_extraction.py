from src.data.file_preparation.prepare_data_file import get_processed_path_file
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from src.features.utils.get_vectorized_tweet import Ngrams
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import pandas as pd
import re


labeled_tweet = {'tweet': '', 'label': ''}

processed_file_path = get_processed_path_file('labeled_data')

with open(processed_file_path, 'r', encoding='utf-8', newline='') as file:
    labeled_df = pd.read_csv(file)

# Random Selection from negative tweets
df_with_all_negative_tweets = labeled_df.loc[(labeled_df['label'] == 'negative')]

df_negative_final = df_with_all_negative_tweets.apply(lambda x: x.sample(n=18382, random_state=1))


df_positive_final = labeled_df.loc[(labeled_df['label'] == 'positive')]

df_tweets = pd.concat([df_negative_final, df_positive_final])  # df with equal number of positive and negative tweets


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

# Split into predictors and outcome data
y = df_tweets['label']
x = df_tweets.drop(
    ['label', 'number_of_words'], axis=1)


# Split into train and test data
X_train, X_test, y_train, y_test = train_test_split(x, y, train_size=0.65,test_size=0.35, random_state=101)
# TODO: same number of positive and negative


# Model selection process: Create list of different classifiers/algorithms to try out
classifiers = [
    KNeighborsClassifier(),
    RandomForestClassifier(random_state=1),
    GradientBoostingClassifier(random_state=1)
]

# Model selection process: Loop through the different classifiers using the pipeline
for classifier in classifiers:
    model_pipeline = Pipeline([
        # N-grams
        ('feats', Ngrams(X_train)),
        # Classifier
        ('classifier', classifier)])

    model_pipeline.fit(X_train, y_train)
    y_predict = model_pipeline.predict(X_test)
    print(classifier)
    print(y_predict)

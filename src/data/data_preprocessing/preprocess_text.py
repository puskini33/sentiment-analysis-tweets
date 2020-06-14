from src.data.data_preparation.prepare_data_file import get_raw_path_file, get_processed_path_file,\
    create_file_with_headers, write_to_csv
from src.data.data_preprocessing.utils.spacy_helpers import text_to_tokens_text, is_stop_word, get_lemmatized_text
import pandas as pd
import emoji
import re


def replace_emoji_with_text(token):
    positive_emojis = [':smiley:', ':smile:', ':relaxed:', ':stuck_out_tongue_winking_eye:', ':stuck_out_tongue:', ':heart:',
                      ':two_hearts:', ':simple_smile:', ':heart_eyes:', ':laughing:', ':relieved:', ':grin:', ':kissing_smiling_eyes:',
                      ':purple_heart:', ':green_heart:', ':person_raising_hand:', ':face_savoring_food:',
                       ':chocolate_bar:', ':cherries:', ':pineapple:', ':beaming_face_with_smiling_eyes:']
    negative_emojis = [':sleepy_face:', ':frowning:', ':unamused:', ':fearful:', ':cry:', ':scream:', ':sob:',
                       ':angry:', ':rage:', ':broken_heart:', ':person_facepalming:']

    if token in positive_emojis:
        token = 'EMO POS'
    elif token in negative_emojis:
        token = 'EMO NEG'

    return token


# Raw Data Preparation
raw_path_file = get_raw_path_file()
raw_df = pd.read_csv(raw_path_file)

# Processed Data File Preparation
processed_file_path = get_processed_path_file()
processed_tweet_headers = ["full_text"]
create_file_with_headers(processed_file_path, processed_tweet_headers)


def preprocess_text_before_demojize(text):
    text = re.sub(r'((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*',
                  'url', text)  # Replaces URLs with url

    text = re.sub(r'(RT|retweet|from|via)((?:\b\W*@\w+)+)', 'usermention', text)  # Replace @handle with usermention

    text = re.sub(r'@([A-Za-z0-9_]+)', 'usermention', text)  # Replace @user_mention with usermention

    text = re.sub(r'(?:(?<=\s)|^)#(\w*[A-Za-z_]+\w*)', r' \1 ', text)  # Replaces #hashtag with hashtag

    text = re.sub(r'(-|\[|]|\'|\"|&|,|_|\||:|\.|;)', '', text)  # Remove punctuation and other signs

    text = text.lower()  # Lower letters word

    text = re.sub(r'(.)\1+', r'\1\1', text)  # Convert more than 2 letter repetitions to 2 letter

    text = get_lemmatized_text(text)

    return text


# Transform raw text of tweet to processed text
for value in raw_df['full_text'].values:
    value = preprocess_text_before_demojize(value)

    tokenized_text = text_to_tokens_text(value)  # Tokenize the full_text of the tweet

    valid_tokens = [word for word in tokenized_text if is_stop_word(word)]  # keep only valid words

    for index_token in range(0, len(tokenized_text)-1):

        tokenized_text[index_token] = emoji.demojize(tokenized_text[index_token])  # Demojize text
        tokenized_text[index_token] = replace_emoji_with_text(tokenized_text[index_token])  # replace emoji with text


    processed_tweet = {}
    processed_tweet['full_text'] = tokenized_text

    write_to_csv(processed_file_path, processed_tweet)

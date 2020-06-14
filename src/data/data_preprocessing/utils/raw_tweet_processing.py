
def process_tweet(tweet: dict) -> dict:
    """Function filters out unwanted data and saves the hashtag, user name, text, location in a tweet dictionary."""

    raw_tweet = {}

    raw_tweet['created_at'] = tweet.get('created_at', '')  # when the tweet was posted

    if 'entities' in tweet and 'hashtags' in tweet['entities']:  # each hashtag in the tweet
        raw_tweet['hashtags'] = [hashtag['text'] for hashtag in
                                       tweet['entities']['hashtags']]

    if 'retweeted_status'in tweet and 'extended_tweet' in tweet['retweeted_status']:  # if full_text of tweet is available
        raw_tweet['text'] = tweet['retweeted_status']['extended_tweet']['full_text']
    elif 'text' in tweet:
        raw_tweet['text'] = tweet.get('text', '')

    if 'user' in tweet and 'screen_name' in tweet['user']:
        raw_tweet['user_screen_name'] = tweet['user']['screen_name']

    if 'user' in tweet and 'name' in tweet['user']:
        raw_tweet['user_name'] = tweet['user']['name']

    if 'user' in tweet and 'location' in tweet['user']:
        raw_tweet['user_loc'] = tweet['user']['location']

    if 'user' in tweet and 'description' in tweet['user']:
        raw_tweet['description'] = tweet['user']['description']

    if 'entities' in tweet and 'urls' in tweet['entities']:  # each url posted in the tweet
        raw_tweet['urls'] = [url['url'] for url in tweet['entities']['urls']]

    return raw_tweet

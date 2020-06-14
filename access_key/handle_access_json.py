from access_key.credentials import get_credentials


class Credentials(object):

    twitter_credentials = get_credentials()
    consumer_key = twitter_credentials['CONSUMER_KEY']
    consumer_secret = twitter_credentials['CONSUMER_SECRET']
    access_key = twitter_credentials['ACCESS_TOKEN']
    access_secret = twitter_credentials['ACCESS_SECRET']

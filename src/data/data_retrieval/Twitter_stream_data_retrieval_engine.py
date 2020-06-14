from twython import TwythonStreamer
from access_key.handle_access_json import Credentials
from src.data.data_preprocessing.utils.raw_tweet_processing import process_tweet
from src.data.data_preparation.prepare_data_file import write_to_csv
import datetime


class MyStreamer(TwythonStreamer):

    def __init__(self, file_path) -> None:
        super().__init__(Credentials.consumer_key, Credentials.consumer_secret,
                         Credentials.access_key, Credentials.access_secret)
        self.file_path = file_path
        self.streaming_minutes: float or None = None
        self.number_wanted_tweets: int or None = None
        self.number_saved_tweets: int = 0
        self.streaming_time: int or None = None

    def stream_data(self, keyword: str) -> None:
        """Update the streaming time and start streaming with the given keyword."""
        self.update_streaming_time()
        self.statuses.filter(track=keyword, language='en', tweet_mode='extended')

    # received data
    def on_success(self, data: dict) -> None:
        """If tweet was found send it further for processing and saving."""
        if self.streaming_minutes is not None:
            self.verify_streaming_time()
        if self.number_wanted_tweets is not None:
            self.verify_number_streamed_tweets()

        tweet_data = process_tweet(data)
        write_to_csv(self.file_path, tweet_data)
        self.number_saved_tweets += 1

    # Problem with the API
    def on_error(self, status_code: str, data: dict, headers=True) -> None:
        """If problems with the connection or the tweet were found, disconnect from Twython."""
        print(status_code, data)
        self.disconnect()

    def verify_streaming_time(self) -> None:
        """Verify if the streaming time ran out."""
        if datetime.datetime.now() > self.streaming_time:
            print("Streaming time passed.")
            self.disconnect()

    def verify_number_streamed_tweets(self) -> None:
        """ Verify if the given number of tweets was already saved."""
        if self.number_saved_tweets == self.number_wanted_tweets:
            print('Requested number of tweets saved')
            self.disconnect()

    def update_streaming_time(self):
        """ If a streaming time was given, set the time when the streamer should stop streaming."""
        if self.streaming_minutes is not None:
            self.streaming_time = datetime.datetime.now() + datetime.timedelta(minutes=self.streaming_minutes)

from pathlib import Path
import csv
import typing
import pathlib

raw_file_headers = ["created_at", "hashtags", "full_text", "user_screen_name", "user_name", "location",
                    "description", "urls"]


def get_raw_path_file(user_file_name: str) -> typing.Union[str, pathlib.Path]:
    """Return the raw file path."""
    base_path = Path(__file__).parent
    file_name = 'raw_tweets_' + user_file_name + '.csv'
    raw_tweets_csv_path = (base_path / f"../../../data/raw/{file_name}").resolve()
    return raw_tweets_csv_path


def get_processed_path_file(user_file_name: str) -> typing.Union[str, pathlib.Path]:
    """Return the processed file path."""
    base_path = Path(__file__).parent
    file_name = 'processed_tweets_' + user_file_name + '.csv'
    processed_tweets_csv_path = (base_path / f"../../../data/processed/{file_name}").resolve()
    return processed_tweets_csv_path


def create_file_with_headers(file_path: typing.Union[str, pathlib.Path], headers: list) -> None:
    """Function creates the file for first time and writes the headers."""

    try:
        file_path.resolve(strict=True)
    except FileNotFoundError:
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers, lineterminator='\n')
            writer.writeheader()


def write_to_csv(file_path, tweet: dict) -> None:
    """Function opens the raw_tweets_csv file and saves the tweet in it."""
    with open(file_path, 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(list(tweet.values()))

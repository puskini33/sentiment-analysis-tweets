from src.data.data_retrieval.Twitter_stream_data_retrieval_engine import MyStreamer
from src.data.data_preparation.prepare_data_file import get_raw_path_file, create_file_with_headers, raw_file_headers


raw_file_path = get_raw_path_file()
create_file_with_headers(raw_file_path, raw_file_headers)
streamer = MyStreamer(raw_file_path)
# streamer.streaming_minutes = 1
streamer.number_wanted_tweets = 10
streamer.stream_data('chocolate')




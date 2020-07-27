from src.data.data_retrieval.Twitter_stream_data_retrieval_engine import MyStreamer
from src.data.file_preparation.prepare_data_file import get_raw_path_file, create_file_with_headers, raw_file_headers


keywords_search = ['Trump']
companies = ['Uline', 'Home_Depot', 'CNN', 'Taco_Bell', 'Bang_Energy', 'Patagonia', 'Microsoft', 'Merriam_Webster', 'Fox_News']

# 'CNN': 759251,
company_twitter_id = {
                      'Uline': 15756141,
                      'Patagonia': 16191793,
                      'Microsoft': 74286565,
                      'Merriam_Webster': 97040343,
                      'CNN': 759251,
                      'Fox_News': 1367531,
                      'Home_Depot': 14791918,
                      'Taco_Bell': 7831092,
                      'Bang_Energy': 2875373609,
                      }


for company in companies:
    # Data Retrieval
    raw_file_path = get_raw_path_file(company)
    create_file_with_headers(raw_file_path, raw_file_headers)
    streamer = MyStreamer(raw_file_path)
    # streamer.streaming_minutes = 1
    streamer.number_wanted_tweets = 10000
    streamer.stream_data('Trump', company_twitter_id[company])




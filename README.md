
# Sentiment Analysis of Tweets

## Quick Links
* [Installation Guide](#installation-guide)
    * [Install dependencies](#install-dependencies)
* [Introduction](#introduction)
* [File Preparation](#data-preparation)
* [Data Retrieval](#data-retrieval)
* [Data Preprocessing](#data-preprocessing)
* [Data Labeling](#data-labeling)
* [Feature Extraction](#feature-extraction)
* [Modeling](#modeling)

## Installation Guide
### Install dependencies
To set up your local environment before starting to work on the project, follow the steps:<br>
   
   1. Install venv library. Type in the terminal: `pip install venv`

   2. Create virtual environment venv inside the root folder:  `python -m venv venv`


   3. Activate venv

        Linux and MacOs: `source venv/bin/activate`
        
        Windows: `venv/Scripts/Activate.ps1` or cd to Scripts folder and type `activate`

   4. Upgrade pip:  `python -m pip install --upgrade pip`


   5. Install requirements: `pip install -r requirements.txt`
 
   6. Install the spacy model: `python -m spacy download en_core_web_sm`
   
   
## Introduction
This project is part of the [Frauenloop](https://www.frauenloop.org/) Course Curriculum in Data Science. The course was taught over the course of 3 months and presumed the organization of a project in natural language processing (NLP).
I choose to focus on the sentiment analysis of tweets that were retrieved with the Twitter API [Twython](https://twython.readthedocs.io/en/latest/).
## File Preparation
The scripts for file preparation can be found in `src.data.file_preparation`. The file contains functions to create a new raw_ and/or processed_file with headers, to write to .csv file, and to get relative file path.
## Data Retrieval
The scripts for data retrieval can be found in `src.data.data_retrieval`. You can stream data specifying the keyword of the search, the id of the tweeter page, the number of minutes you want to stream, and the number of tweets you want.
The data is saved in `data.raw`.
## Data Preprocessing
The script for data preprocessing can be found in `src.data.data_preprocessing`. The processed .csv files can be found in `data.processed`. Stop words, urls, handles, punctuation are removed, the emoji is transformed to a string according to the category it belongs to: EPOS or ENEG. The valence of the emoji is subjectively set by me. I separated positive and negative emojis in 2 lists.
## Data Labeling
The script for data labeling can be found in `src.data.data_labeling`. The .csv file with labeled data can be found in `data.processed`. I set 2 labels to evaluate the sentiment of the tweet: positive and negative. I first did a TF-IDF analysis on the corpus of words, then I manually categorized the most frequent words into a positive words list and a negative words list. I set the label of the tweet based on the max count of positive and negative words within the tweet. The tweets with no or equal number of positive/negative words in the tweet were discarded.
## Feature Extraction
## Modeling






# Import necessary modules
import os
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from src.logger import logging
from src.entity import DataTransformationConfig

# Download NLTK resources
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Class definition for DataTransformation
class DataTransformation:
    def __init__(self, raw_text_path, config: DataTransformationConfig):
        # Initialize the DataTransformation class with a raw text path and a configuration object
        self.raw_text_path = raw_text_path
        self.config = config

    # Clean text by removing symbols, extra spaces, numbers, alphanumerics, etc., and convert into lowercase
    def clean_text(self, text):
        # Convert the whole text into lowercase
        text = text.lower()
        # Remove unwanted characters from text using regex patterns
        pattern1 = re.compile(r'[^a-zA-Z\s]')
        pattern2 = re.compile(r'\n')
        # Replace matched characters with an empty string and space
        text = pattern1.sub('', text)
        cleaned_text = pattern2.sub(' ', text)
        return cleaned_text

    # Tokenize the texts for removing stopwords, convert text into tokens
    def tokenize_text(self, text):
        words = word_tokenize(text)
        return words

    # Remove stopwords from tokenized text
    def remove_stopwords(self, tokens):
        # English language stopwords
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [word for word in tokens if word not in stop_words]
        return filtered_tokens

    # Stem the tokens
    def stem_tokens(self, tokens):
        # Porter stemmer
        stemmer = PorterStemmer()
        stemmed_tokens = [stemmer.stem(word) for word in tokens]
        return stemmed_tokens

    # Get filtered text after above cleaning processes
    def filtered_text(self, tokens_list):
        text = ' '.join(tokens_list)
        return text

    def transform_text(self):
        # Load the dataset from the CSV file
        df = pd.read_csv(self.raw_text_path)
        logging.info("Data cleaning starts...")
        # Apply the cleaning and transformation processes to the 'text' column
        logging.info("Removing punctuations, symbols etc. from text and converting to lowercase...")
        df['text'] = df['text'].apply(self.clean_text)
        logging.info("Converting text into tokens...")
        df['text'] = df['text'].apply(self.tokenize_text)
        logging.info("Removing stopwords from tokenized text...")
        df['text'] = df['text'].apply(self.remove_stopwords)
        logging.info("Performing steming on tokenized text...")
        df['text'] = df['text'].apply(self.stem_tokens)
        logging.info("Getting filtered text from tokenized text...")
        df['text'] = df['text'].apply(self.filtered_text)
        logging.info("Data cleaning/transformation end...")
        # Save the cleaned text to a new CSV file
        logging.info(f"Cleaned text saved at {self.config.cleaned_text_file}...")
        df.to_csv(self.config.cleaned_text_file, index=False)

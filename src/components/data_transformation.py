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

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')


# Class definition for DataIngestion
class DataTransformation:
    def __init__(self, raw_text_path, config: DataTransformationConfig):
        # Initialize the DataTransformationConfig class with a configuration object
        self.raw_text_path = raw_text_path
        self.config = config

    # remove symbols, extra spaces, numbers, alphanumberics etc. from text
    # and convert into lower case
    def clean_text(self, text):
        # convert the whole text into lowercase
        text = text.lower()
        # remove unwanted characters from text
        # patterns 
        pattern1 = re.compile(r'[^a-zA-Z\s]')
        pattern2 = re.compile(r'\n')
        # replace matched characters with an empty string and space
        text = pattern1.sub('', text)
        cleaned_text = pattern2.sub(' ', text)
        return cleaned_text
    

    # Tokenize the texts for removing stopwords
    # convert text into tokens
    def tokenize_text(self, text):
        words = word_tokenize(text)
        return words


    # remove stopwords from tokenized text
    def remove_stopwords(self, tokens):
        # english language stopwords
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [word for word in tokens if word not in stop_words]
        return filtered_tokens


    # stem the tokens
    def stem_tokens(self, tokens):
        # porter stemmer 
        stemmer = PorterStemmer()
        stemmed_tokens = [stemmer.stem(word) for word in tokens]
        return stemmed_tokens
    

    # filtered text after above cleaning processes
    def filtered_text(self, tokens_list):
        text = ' '.join(tokens_list)
        return text

    def transform_text(self):
        # load the dataset from csv file
        df = pd.read_csv(self.raw_text_path)

        df['text'] = df['text'].apply(self.clean_text)

        df['text'] = df['text'].apply(self.tokenize_text)

        df['text'] = df['text'].apply(self.remove_stopwords)

        df['text'] = df['text'].apply(self.stem_tokens)
        
        df['text'] = df['text'].apply(self.filtered_text)

        df.to_csv(self.config.cleaned_text_file)



        

from gensim.parsing.preprocessing import *
import requests
import os
from bs4 import BeautifulSoup
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def get_key_words(file_name):
    infile = open(file_name, encoding="utf8")
    contents = infile.read()
    CUSTOM_FILTERS = [lambda x: x.lower(), strip_tags, strip_punctuation, strip_multiple_whitespaces,
                   strip_numeric, remove_stopwords, strip_short, strip_non_alphanum]
    doc = preprocess_string(contents, CUSTOM_FILTERS)
    doc = list(map(lambda x: lemmatizer.lemmatize(x),doc))
    infile.close()
    return list(set(doc))




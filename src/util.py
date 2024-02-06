import json
import os
def read_stopwords(file):
    with open(file, 'r') as file:
        return json.load(file)

def hu_stopwords():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    stopwords_file = os.path.join(current_dir, '../stopwords/stopwords-hu.json')
    return read_stopwords(stopwords_file)

def ro_stopwords():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    stopwords_file = os.path.join(current_dir, '../stopwords/stopwords-ro.json')
    return read_stopwords(stopwords_file)

def de_stopwords():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    stopwords_file = os.path.join(current_dir, '../stopwords/stopwords-de.json')
    return read_stopwords(stopwords_file)

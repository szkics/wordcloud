import json

def read_stopwords(file):
    with open(file, 'r') as file:
        return json.load(file)

def hu_stopwords():
    return read_stopwords('stopwords-hu.json')

def ro_stopwords():
    return read_stopwords('stopwords-ro.json')

def de_stopwords():
    return read_stopwords('stopwords-de.json')
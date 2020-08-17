from boilerpy3 import extractors
import spacy
from spacy.lang.en import English
from nltk.corpus import wordnet as wn
import pandas as pd
pd.set_option("max_columns", None)
import numpy as np

# Use Spacy package model
nlp = spacy.load("en_core_web_md")
parser = English()

# Use boilerpy3 ArticleExtractor()
extractor = extractors.ArticleExtractor()
content = extractor.get_content_from_url('https://www.nytimes.com/2020/08/16/us/migrant-children-hotels-coronavirus.html')

# Topic are the topics of interest - user should first decide which topics to be included for analysis
topics = ["automotive", "travel", "science", "technology",
          "nature", "sports", "business", "beauty", "fashion", "music", "art",
          "movie", "entertainment", "media", "children", "health", "gambling", 
          "religion", "education", "politics", "history", "war", "news",
          "food", "literature", "crime"]

# Function for removing irrelevant parts of the extracted text
def remove_trash(text):
    cleaned = ''
    for i in text.split('\n'):
        if len(i.split()) <= 4:
            continue
        else:
            cleaned += (i)
    return cleaned

# Function for tokenising and lammetization of the relevant text
def to_token(text):
    token_list = []
    tokens = parser(text)
    for token in tokens:
        if token.orth_.isspace():
            continue
        elif token.like_url: #skip if looks like url
            continue
        elif token.orth_.startswith('@'): #skip if looks like tag
            continue
        elif token.orth_.startswith('#'): #skip if looks like tag
            continue
        elif token.is_punct: #skip if looks like punctuation
            continue
        elif token.like_num: #skip if looks like number
            continue
        elif token.is_stop: #skip if looks like stop words
            continue
        else:
            token_list.append(token.lower_)
            
        token_list = [wn.morphy(x) if wn.morphy(x) != None else x for x in token_list]
    return token_list

# Function that takes url and topics (long string of single word topics separated by space) and return topic relevancy scores
def classify_web(url, topics = topics):
    # Extract content from web url
    content = extractor.get_content_from_url(url)
    
    # Join the tokens back up for Spacy nlp function
    token_join = ' '.join(to_token(remove_trash(content)))
    
    # doc is the content
    doc = nlp(token_join)
    
    # topics are the user defined topics
    topics = ' '.join(topics)
    topic = nlp(topics)
    
    # Calculate similarity between content and topics
    topic_similarity = []
    for token in topic:
        topic_similarity.append(nlp(token_join).similarity(token))
    
    # Table to capture results
    data = {'topics':topics.split(), 'similarity':topic_similarity}
    result = pd.DataFrame(data=data).sort_values(['similarity'], ascending=[False]).reset_index(drop=True)
    
    return(result)
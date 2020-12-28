from fastapi import APIRouter

# Importing Eland and low-level Elasticsearch clients for comparison
import eland as ed
from eland.conftest import *
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q

# Import pandas and numpy for data wrangling
import pandas as pd
import numpy as np

# For pretty-printing
import json
from transformers import pipeline 


router = APIRouter()

@router.post('/sentiment/{sentiment_analysis}')
async def viz(text: str):
    # name of the index we want to query
    index_name = 'twinttweets' 

    # instantiating client connect to localhost by default
    es = Elasticsearch()

    # loading the data into Eland dataframe: 
    ed_stocks = ed.read_es('localhost', index_name)   #note: will need to change localhost when deploying to aws 
    #convert query for snap into a pandas dataframe 
    data = ed.eland_to_pandas(ed_stocks[ed_stocks['tweet'].es_match(text)])
    #grab a single index from that data frame 
    tweet = data['tweet'][80]
    nlp = pipeline("sentiment-analysis")
    result = nlp(tweet)[0]
    return print(f"label: {result['label']}, with score: {round(result['score'], 4)}")



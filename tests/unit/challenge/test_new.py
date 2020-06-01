from datetime import date
import pytest
from dags import challenge as c
import os.path

NEWS_KEY = os.environ.get('NEWS_KEY')     #api key for newsapi.org
news = c.News(NEWS_KEY)                   #constructor from challenge
bucket, sourceName = os.environ.get('s3bucket'), os.environ.get('soureName')

class TestSample:

    def test_flatten_top(self):
        news.flatten(bucket, sourceName)
        expectedFile = '{}_top_headlines.csv'.format(date.today())
        assert os.path.isfile(expectedFile)

    def test_flatten_topic(self, topic):
        news.flatten(bucket, sourceName, topic)
        expectedFile = '{}_{}.csv'.format(date.today(), topic)
        assert os.path.isfile(expectedFile)
        
        

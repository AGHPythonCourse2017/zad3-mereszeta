import article_parser
import requests
from

class SentimentChecker:
    def __init__(self, url):
        self.art = article_parser.ArticleParser(url)
        self.sentiment = 'neutral'

    def check_sentiment(self):
        req = requests.post('http://text-processing.com/api/sentiment/', data=self.art.content)
        js = req.json()
        self.sentiment = js['label']

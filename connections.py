import article_parser
import requests
from file_parser import KeyProvider
from apiclient.discovery import build


class SentimentChecker:
    def __init__(self, url):
        self.art = article_parser.ArticleParser(url)
        self.sentiment = 'neutral'

    def check_sentiment(self):
        req = requests.post('http://text-processing.com/api/sentiment/', data=self.art.content)
        js = req.json()
        self.sentiment = js['label']


class GoogleApiProvider:
    def __init__(self, path):
        self.kp = KeyProvider(path)
        self.links = []

    def make_search(self, topic):
        search = build(self.kp.name, self.kp.key)
        results = search.cse().list(q=topic, cx=self.kp.name).execute()
        for result in results:
            self.links.append(result['link'])

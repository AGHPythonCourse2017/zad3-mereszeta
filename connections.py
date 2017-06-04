import article_parser
import requests
from file_parser import KeyProvider
from apiclient.discovery import build


class SentimentChecker:
    def __init__(self, url, content):
        self.art = content
        self.sentiment = 'neutral'

    def check_sentiment(self):
        req = requests.post('http://text-processing.com/api/sentiment/', data=self.art)
        js = req.json()
        self.sentiment = js['label']

    def show_info_about_sentiment(self):
        self.check_sentiment()
        if self.sentiment == 'pos' or self.sentiment == 'neg':
            print('your article seems to be biased in some way')
        else:
            print('your article seems to be objective')


class GoogleApiProvider:
    def __init__(self, path):
        self.kp = KeyProvider(path)
        self.links = []

    def make_search(self, topic):
        search = build(self.kp.name, self.kp.key)
        results = search.cse().list(q=topic, cx=self.kp.name).execute()
        for result in results:
            self.links.append(result['link'])

from .article_parser import ArticleParser
from .connections import SentimentChecker,GoogleApiProvider
from .file_parser import ListOfWebsitesProvider


class TruthChecker:
    def __init__(self, url, path_to_csv, path_to_key=''):
        self.url = url
        self.path_to_key = path_to_key
        self.lp = ListOfWebsitesProvider(path_to_csv)
        self.topic = ''

    def check_one(self):
        self.lp.compare(self.url)
        ap = ArticleParser(self.url)
        self.topic = ap.title
        ap.check_if_author()
        sc = SentimentChecker(self.url, ap.content)
        sc.show_info_about_sentiment()
        print('this algorithm will not tell you is it a fake news, but previous information could be helpful')

    def check_with_search(self):
        if self.path_to_key == '':
            print('you have to provide your own google api key and search id in separate file')
            return
        gp = GoogleApiProvider(self.path_to_key)
        self.check_one()
        gp.make_search(self.topic)
        for link in gp.links:
            print('checking articles from google search')
            ap = ArticleParser(link)
            ap.check_if_author()
            sc= SentimentChecker(link, ap.content)
            sc.show_info_about_sentiment()
            print('you have recieved additional info about articles connected with your, use it wisely')

from newspaper import Article
from urllib.parse import urlparse


class ArticleParser:
    def __init__(self, url):
        base_art = Article(url, language='en')
        base_art.download()
        base_art.parse()
        self.content = base_art.text
        self.title=base_art.title
        self.auth = base_art.authors
        self.domain = '{uri.netloc}'.format(uri=urlparse(url))

    def check_if_author(self):
        if self.auth=='':
            print('your article has no author')
        else:
            print('author of your article is named, you can google him if he is trustworthy')

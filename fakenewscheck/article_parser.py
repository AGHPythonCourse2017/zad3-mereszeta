from newspaper import Article
from urllib.parse import urlparse
from pprint import PrettyPrinter


class ArticleParser:
    def __init__(self, url):
        base_art = Article(url, language='en')
        base_art.download()
        base_art.parse()
        self.content = base_art.text
        self.title = base_art.title
        self.auth = base_art.authors
        self.domain = '{uri.netloc}'.format(uri=urlparse(url))

    def check_if_author(self):
        pp=PrettyPrinter()
        if len(self.auth)==0:
            pp.pprint('your article has no author')
        else:
            pp.pprint('name of author is:')
            pp.pprint(self.auth)
            pp.pprint('author of your article is named , you can google him if he is trustworthy')

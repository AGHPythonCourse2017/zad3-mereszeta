
from fakenewscheck.file_parser import ListOfWebsitesProvider
from fakenewscheck.article_parser import ArticleParser
from fakenewscheck.connections import SentimentChecker
import unittest


class TestFakeCheckNews(unittest.TestCase):
    def test_file_parser(self):
        lp = ListOfWebsitesProvider('sources.csv')

        self.assertEqual(len(lp.list_of_sites), 833)
        self.assertIn({'Website': 'conservativetribune.com', 'Tags': ['bias', 'conspiracy', 'unreliable'], 'Desc': ''},
                      lp.list_of_sites)
        self.assertNotIn({'Website': 'consetivetribune.com', 'Tags': ['bias', 'conspiracy', 'unreliable'], 'Desc': ''},
                         lp.list_of_sites)

    def test_parsing(self):
        ap = ArticleParser('http://www.bbc.com/news/uk-40148737')
        self.assertEqual(ap.auth, [])
        self.assertEqual(ap.domain, 'www.bbc.com')
        self.assertEqual(ap.title, 'London attack: 12 arrested in Barking after van and knife attack')

    def test_connection(self):
        ap = ArticleParser('http://www.bbc.com/news/uk-40148737')
        sc = SentimentChecker('http://www.bbc.com/news/uk-40148737', ap.content)
        sc.check_sentiment()
        self.assertEqual(sc.sentiment, 'neutral')


if __name__ == '__main__':
    unittest.main()

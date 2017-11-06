from unittest import TestCase
from server import app
import count
import server
from model import db, connect_to_db, User, Site, FaveSite, example_data



class MyAppUnitTestCase(TestCase):
    """class for unittests"""

    def setUp(self):
        """Done at beginning of every test"""

        connect_to_db(app, "postgresql:///testdb")
        db.create_all()
        example_data()
    
    def tearDown(self):
        """Done at end of every test."""

        db.session.close()
        db.drop_all()
        
  
    def test_count_words(self):
        """tests count_words function"""

        site = Site.query.filter_by(url='https://www.foxnews.com').first()
        site2 = Site.query.filter_by(url='http://www.buzzfeednews.com').first()

        self.assertDictEqual({'important': 1, 'words': 2, 'places': 1}, count.count_words(site))
        self.assertDictContainsSubset({"they're": 1, 'about': 1, 'people': 1, 'always': 1, 'silly': 2, 'things': 1}, count.count_words(site2))
    

    def test_count_one_word(self):
        """tests count_one_word function"""

        sites = Site.query.all()

        expect_1 = {'Fox News': 0, 'BuzzFeed': 2}
        self.assertDictEqual(expect_1, count.count_one_word("Silly", sites))
        expect_2 = {'Fox News': 2, 'BuzzFeed': 0}
        self.assertDictEqual(expect_2, count.count_one_word("WORDS", sites))
        expect_3 = {'Fox News': 0, 'BuzzFeed': 0}
        self.assertDictEqual(expect_3, count.count_one_word("impossible", sites))




if __name__ == "__main__":
    import unittest

    unittest.main()

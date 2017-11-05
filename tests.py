from unittest import TestCase
# from model import (User, Sites, connect_to_db, db, example_data)
from server import app
import count
import server



class MyAppUnitTestCase(TestCase):
    """class for unittests"""

    def setUp(self):
        """Do at beginning of every test"""

        def _mock_open_file(file_name):
            return {'https://www.foxnews.com': "Fox News uses a lot of words many times. Words are important and places too.",
                    'http://www.buzzfeednews.com': 'People think buzzfeed only talks about silly things, but they\'re not always silly'}

        count.open_file = _mock_open_file
        
  
    def test_count_words(self):
        """tests count_words function"""

        self.assertDictEqual({'important': 1, 'words': 2, 'places': 1}, count.count_words('https://www.foxnews.com'))
        self.assertDictContainsSubset({"they're": 1, 'about': 1, 'people': 1, 'always': 1, 'silly': 2, 'things': 1}, count.count_words('http://www.buzzfeednews.com'))
    
    def test_count_one_word(self):
        """tests count_one_word function"""

        sites = ['http://www.buzzfeednews.com', 'https://www.foxnews.com']
        expect_1 = {'https://www.foxnews.com': 0, 'http://www.buzzfeednews.com': 2}
        self.assertDictEqual(expect_1, count.count_one_word("Silly", sites))
        expect_2 = {'https://www.foxnews.com': 2, 'http://www.buzzfeednews.com': 0}
        self.assertDictEqual(expect_2, count.count_one_word("WORDS", sites))
        expect_3 = {'https://www.foxnews.com': 0, 'http://www.buzzfeednews.com': 0}
        self.assertDictEqual(expect_3, count.count_one_word("impossible", sites))




if __name__ == "__main__":
    import unittest

    unittest.main()

from unittest import TestCase
from books import grab_headers


class Test(TestCase):
    def test_grab_headers_proper(self):
        test_book = {'Author': 'Suess', 'Category': 'Fiction', 'Publisher': 'None', 'Shelf': 'widepeepoHappy',
                     'Subject': 'Picture Book', 'Title': 'Green Eggs and Ham'}
        expected = "Author	Category	Publisher	Shelf	Subject	Title"
        actual = grab_headers(test_book)
        self.assertEqual(expected, actual)

    def test_grab_headers_different_order(self):
        test_book = {'Author': 'Suess', 'Title': 'Green Eggs and Ham', 'Publisher': 'None', 'Shelf': 'widepeepoHappy',
                     'Category': 'Fiction', 'Subject': 'Picture Book'}
        expected = "Author	Title	Publisher	Shelf	Category	Subject"
        actual = grab_headers(test_book)
        self.assertEqual(expected, actual)

    def test_grab_headers_extra_key(self):
        test_book = {'Author': 'Suess', 'Title': 'Green Eggs and Ham', 'Publisher': 'None', 'Shelf': 'widepeepoHappy',
                     'Category': 'Fiction', 'Subject': 'Picture Book', 'Year': "1960"}
        expected = "Author	Title	Publisher	Shelf	Category	Subject	Year"
        actual = grab_headers(test_book)
        self.assertEqual(expected, actual)

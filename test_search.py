from unittest import TestCase
from books import search
from books import open_file


class TestSearch(TestCase):

    def test_search_within_author(self):
        expected = [{'Author': 'Dupre', 'Category': 'Architecture', 'Publisher': 'BD&L', 'Shelf': '12',
                     'Subject': '20th Century', 'Title': 'Skyscrapers'}]
        actual = search(open_file("wheredidallmybooksgo.txt"), "Author", "dupre")
        self.assertEqual(expected, actual)

    def test_search_within_title(self):
        expected = [{'Author': 'Preston', 'Category': 'Fiction', 'Publisher': 'Warner', 'Shelf': '11',
                    'Subject': 'Thriller', 'Title': 'Riptide'}]
        actual = search(open_file("wheredidallmybooksgo.txt"), "Title", "riptide")
        self.assertEqual(expected, actual)

    def test_search_within_publisher(self):
        expected = [{'Author': 'Shields', 'Category': 'Mathematics', 'Publisher': 'Worth', 'Shelf': '27',
                     'Subject': 'Algebra', 'Title': 'Elementary Linear Algebra 3e'}]
        actual = search(open_file("wheredidallmybooksgo.txt"), "Publisher", "worth")
        self.assertEqual(expected, actual)

    def test_search_within_shelf(self):
        expected = [{'Author': 'Eyewitness Travel', 'Category': 'Travel', 'Publisher': 'DK', 'Shelf': '21',
                     'Subject': 'Italy', 'Title': 'Top 10 Florence and Tuscany'}]
        actual = search(open_file("wheredidallmybooksgo.txt"), "Shelf", "21")
        self.assertEqual(expected, actual)

    def test_search_within_category(self):
        expected = [{'Author': 'Shields', 'Category': 'Mathematics', 'Publisher': 'Worth', 'Shelf': '27',
                     'Subject': 'Algebra', 'Title': 'Elementary Linear Algebra 3e'}]
        actual = search(open_file("wheredidallmybooksgo.txt"), "Category", "mathematics")
        self.assertEqual(expected, actual)

    def test_search_within_subject(self):
        expected = [{'Author': 'Gaventa', 'Category': 'Architecture', 'Publisher': 'Mitchell Beazley', 'Shelf': '16',
                     'Subject': 'Design', 'Title': 'Concrete Design'}]
        actual = search(open_file("wheredidallmybooksgo.txt"), "Subject", "design")
        self.assertEqual(expected, actual)

    def test_search_partial_keyword(self):
        expected = [{'Author': 'Eddings', 'Category': 'Fiction', 'Publisher': 'None', 'Shelf': '34',
                     'Subject': 'Fantasy', 'Title': "Magician's Gambit"},
                    {'Author': 'Hardy', 'Category': 'Fiction', 'Publisher': 'Del Rey', 'Shelf': '14',
                     'Subject': 'Fantasy', 'Title': 'Secret of the Sixth Magic'},
                    {'Author': 'Ambroziak', 'Category': 'Architecture', 'Publisher': 'Princeton Architectural Press',
                     'Shelf': '1', 'Subject': 'Architectural History',
                     'Title': 'Michael Graves Images of a Grand Tour'}]
        actual = search(open_file("wheredidallmybooksgo.txt"), "Title", "mag")
        self.assertEqual(expected, actual)

    def test_search_numbered_shelf(self):
        expected = [{'Author': 'Ambroziak', 'Category': 'Architecture', 'Publisher': 'Princeton Architectural Press',
                     'Shelf': '1', 'Subject': 'Architectural History',
                     'Title': 'Michael Graves Images of a Grand Tour'}]
        actual = search(open_file("wheredidallmybooksgo.txt"), "Shelf", "1")
        self.assertEqual(expected, actual)

    def test_search_no_keyword(self):
        expected = []
        actual = search(open_file("wheredidallmybooksgo.txt"), "Author", "i messed up")
        self.assertEqual(expected, actual)

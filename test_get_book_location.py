from unittest import TestCase
from unittest.mock import patch
from books import get_book_location
import io


class TestGetBookLocation(TestCase):

    @patch("builtins.input", side_effect=["1"])
    def test_get_book_location_working(self, mock_input):
        list_of_matching_books = [{'Author': 'Eddings', 'Category': 'Fiction', 'Publisher': 'None', 'Shelf': '34',
                                   'Subject': 'Fantasy', 'Title': "Magician's Gambit"},
                                  {'Author': 'Hardy', 'Category': 'Fiction', 'Publisher': 'Del Rey', 'Shelf': '14',
                                   'Subject': 'Fantasy', 'Title': 'Secret of the Sixth Magic'}]
        expected = {'Author': 'Eddings', 'Category': 'Fiction', 'Publisher': 'None', 'Shelf': '34',
                    'Subject': 'Fantasy', 'Title': "Magician's Gambit"}
        actual = get_book_location(list_of_matching_books)
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["2"])
    def test_get_book_location_nonexistent(self, mock_input, mock_stdout):
        list_of_matching_books = [{'Author': 'Shields', 'Category': 'Mathematics', 'Publisher': 'Worth',
                                   'Shelf': '27', 'Subject': 'Algebra', 'Title': 'Elementary Linear Algebra 3e'}]
        expected = {}
        expected_print = "\nThere is no book in that location.\n\n"
        actual = get_book_location(list_of_matching_books)
        self.assertEqual(expected, actual)
        self.assertEqual(mock_stdout.getvalue(), expected_print)

from unittest import TestCase
from unittest.mock import patch
import io
from books import format_book_to_line


class TestFormatBookToLine(TestCase):

    def test_format_book_to_line_working(self):
        test_book = {'Author': 'Eddings', 'Category': 'Fiction', 'Publisher': 'None', 'Shelf': '34',
                     'Subject': 'Fantasy', 'Title': 'Pawn of Prophecy'}
        expected = "Eddings	Fiction	None	34	Fantasy	Pawn of Prophecy"
        actual = format_book_to_line(test_book)
        self.assertEqual(expected, actual)

    def test_format_book_to_line_different_order(self):
        test_book = {'Author': 'Eddings', 'Title': 'Pawn of Prophecy', 'Publisher': 'None', 'Shelf': '34',
                     'Subject': 'Fantasy', 'Category': 'Fiction'}
        expected = "Eddings	Pawn of Prophecy	None	34	Fantasy	Fiction"
        actual = format_book_to_line(test_book)
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_format_book_to_line_empty(self, mock_stdout):
        format_book_to_line({"empty": ""})
        expected = ""
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_format_book_to_line_not_dict(self, mock_stdout):
        format_book_to_line(["wrong book"])
        expected = "These aren't the droids you are looking for\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

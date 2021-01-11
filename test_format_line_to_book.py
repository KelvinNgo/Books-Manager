from unittest import TestCase
from books import format_line_to_book


class TestFormatLineToBook(TestCase):
    def test_format_line_to_book_proper(self):
        test_book_column_tag = ["Author", "Title", "Publisher", "Shelf", "Category", "Subject"]
        test_line = "Suess\tGreen Eggs and Ham\t\twidepeepoHappy\tFiction\tPicture Book"
        expected = {'Author': 'Suess', 'Category': 'Fiction', 'Publisher': 'None', 'Shelf': 'widepeepoHappy',
                    'Subject': 'Picture Book', 'Title': 'Green Eggs and Ham'}
        actual = format_line_to_book(test_book_column_tag, test_line)
        self.assertEqual(expected, actual)

    def test_format_line_to_book_empty(self):
        test_book_column_tag = ["Author", "Title", "Publisher", "Shelf", "Category", "Subject"]
        test_line = ""
        expected = {"oh": "shit", "a": "rat"}
        actual = format_line_to_book(test_book_column_tag, test_line)
        self.assertEqual(expected, actual)

    def test_format_line_to_book_extra_category(self):
        test_book_column_tag = ["Author", "Title", "Publisher", "Shelf", "Category", "Subject", "Year"]
        test_line = "Suess\tGreen Eggs and Ham\t\twidepeepoHappy\tFiction\tPicture Book\t1960"
        expected = {'Author': 'Suess', 'Category': 'Fiction', 'Publisher': 'None', 'Shelf': 'widepeepoHappy',
                    'Subject': 'Picture Book', 'Title': 'Green Eggs and Ham', 'Year': '1960'}
        actual = format_line_to_book(test_book_column_tag, test_line)
        self.assertEqual(expected, actual)

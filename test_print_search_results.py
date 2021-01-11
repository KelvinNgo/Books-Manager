from unittest import TestCase
from unittest.mock import patch
from books import print_search_results
import io


class TestPrintSearchResults(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_search_results_working(self, mock_stdout):
        print_search_results([{'Author': 'Dupre', 'Category': 'Architecture', 'Publisher': 'BD&L',
                               'Shelf': '12', 'Subject': '20th Century', 'Title': 'Skyscrapers'}])
        expected = "\nBook 1\n+++++++++++++++++++++++++\nAuthor:   Dupre" \
                   "\n+++++++++++++++++++++++++\nCategory:   Architecture\n" \
                   "+++++++++++++++++++++++++\nPublisher:   BD&L\n+++++++++++++++++++++++++\n" \
                   "Shelf:   12\n+++++++++++++++++++++++++\nSubject:   20th Century\n" \
                   "+++++++++++++++++++++++++\nTitle:   Skyscrapers\n+++++++++++++++++++++++++\n" \
                   "\nThere are 1 matching result(s)\n\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_search_results_no_results(self, mock_stdout):
        print_search_results([])
        expected = "\nThere are 0 matching result(s)\n\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

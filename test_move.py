from unittest import TestCase
from unittest.mock import patch
from books import move
import io


class TestMove(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["4"])
    def test_move_valid_shelf_numeric(self, mock_input, mock_stdout):
        valid_shelves = ["1", "2", "3", "4", "5", "6", 'Gaby', 'Island', 'Lego', 'Noguchi', 'Reading', 'Students']
        valid_book = {'Author': 'Preston', 'Category': 'Fiction', 'Publisher': 'Warner',
                      'Shelf': '11', 'Subject': 'Thriller', 'Title': 'Riptide'}
        expected = "Here are your current shelves\n\n" \
                   "['1', '2', '3', '4', '5', '6', 'Gaby', 'Island', 'Lego', 'Noguchi', 'Reading', 'Students']\n\n" \
                   "Congratulations, you have successfully moved the book to Shelf 4\n\n"
        move(valid_shelves, valid_book)
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["Lego"])
    def test_move_valid_shelf_alphabetic(self, mock_input, mock_stdout):
        valid_shelves = [1, 2, 3, 4, 5, 6, 'Gaby', 'Island', 'Lego', 'Noguchi', 'Reading', 'Students']
        valid_book = {'Author': 'Shields', 'Category': 'Mathematics', 'Publisher': 'Worth',
                      'Shelf': '27', 'Subject': 'Algebra', 'Title': 'Elementary Linear Algebra 3e'}
        expected = "Here are your current shelves\n\n" \
                   "[1, 2, 3, 4, 5, 6, 'Gaby', 'Island', 'Lego', 'Noguchi', 'Reading', 'Students']\n\n" \
                   "Congratulations, you have successfully moved the book to Shelf Lego\n\n"
        move(valid_shelves, valid_book)
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["Quilting Room"])
    def test_move_nonexistent_shelf(self, mock_input, mock_stdout):
        valid_shelves = [1, 2, 3, 4, 5, 6, 'Gaby', 'Lego', 'Noguchi', 'Reading', 'Students']
        valid_book = {'Author': 'Shields', 'Category': 'Mathematics', 'Publisher': 'Worth',
                      'Shelf': '27', 'Subject': 'Algebra', 'Title': 'Elementary Linear Algebra 3e'}
        expected = "Here are your current shelves\n\n" \
                   "[1, 2, 3, 4, 5, 6, 'Gaby', 'Lego', 'Noguchi', 'Reading', 'Students']\n\n" \
                   "That shelf does not exist.\n\n"
        move(valid_shelves, valid_book)
        self.assertEqual(mock_stdout.getvalue(), expected)

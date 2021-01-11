from unittest import TestCase
from unittest.mock import patch
from books import menu


class TestMenu(TestCase):

    @patch("builtins.input", side_effect=["1"])
    def test_menu_search(self, mock_input):
        expected = "search"
        actual = menu()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["2"])
    def test_menu_move(self, mock_input):
        expected = "move"
        actual = menu()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["3"])
    def test_menu_quit(self, mock_input):
        expected = "False"
        actual = menu()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["invalid input"])
    def test_menu_invalid_input(self, mock_input):
        expected = "not quite my tempo"
        actual = menu()
        self.assertEqual(expected, actual)

from unittest import TestCase
from unittest.mock import patch
from books import search_parameter


class TestSearchParameter(TestCase):

    @patch("builtins.input", side_effect=["1", "eddings"])
    def test_search_by_author(self, mock_input):
        expected = ('Author', 'eddings')
        actual = search_parameter()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["2", "skyscrapers"])
    def test_search_by_title(self, mock_input):
        expected = ('Title', 'skyscrapers')
        actual = search_parameter()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["3", "fake_publisher"])
    def test_search_by_publisher(self, mock_input):
        expected = ('Publisher', 'fake_publisher')
        actual = search_parameter()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["4", "a broken shelf"])
    def test_search_by_shelf(self, mock_input):
        expected = ('Shelf', 'a broken shelf')
        actual = search_parameter()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["5", "Fiction"])
    def test_search_by_category(self, mock_input):
        expected = ('Category', 'Fiction')
        actual = search_parameter()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["6", "SF"])
    def test_search_by_subject(self, mock_input):
        expected = ('Subject', 'SF')
        actual = search_parameter()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["asdf", "asdf"])
    def test_search_invalid(self, mock_input):
        expected = ()
        actual = search_parameter()
        self.assertEqual(expected, actual)

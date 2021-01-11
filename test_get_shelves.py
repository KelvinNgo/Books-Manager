from unittest import TestCase
from books import open_file
from books import get_shelves


class TestGetShelves(TestCase):

    def test_get_shelves_numbered_only(self):
        expected = ['1', '11', '12', '13', '14', '16', '21', '27', '34']
        actual = get_shelves(open_file("wheredidallmybooksgo.txt"))
        self.assertEqual(expected, actual)

    def test_get_shelves_alpha_and_numeric(self):
        expected = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                    '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33',
                    '34', '35', '36', '37', '38', 'Gaby', 'Island', 'Lego', 'Noguchi', 'Reading', 'Students']
        actual = get_shelves(open_file("Books_UTF.txt"))
        self.assertEqual(expected, actual)

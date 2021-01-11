from unittest import TestCase
from unittest.mock import patch
import io
from books import open_file


class TestOpenFile(TestCase):

    def test_open_file(self):
        test_txt_file = "wheredidallmybooksgo.txt"
        expected = ({'Author': 'Dupre', 'Category': 'Architecture', 'Publisher': 'BD&L', 'Shelf': '12',
                     'Subject': '20th Century', 'Title': 'Skyscrapers'},
                    {'Author': 'Gaventa', 'Category': 'Architecture', 'Publisher': 'Mitchell Beazley',
                     'Shelf': '16', 'Subject': 'Design', 'Title': 'Concrete Design'},
                    {'Author': 'Eddings', 'Category': 'Fiction', 'Publisher': 'None', 'Shelf': '34',
                     'Subject': 'Fantasy', 'Title': 'Belgarath the Sorcerer'},
                    {'Author': 'Eddings', 'Category': 'Fiction', 'Publisher': 'None',
                     'Shelf': '34', 'Subject': 'Fantasy', 'Title': 'Castle of Wizardry'},
                    {'Author': 'Eddings', 'Category': 'Fiction', 'Publisher': 'None', 'Shelf': '34',
                     'Subject': 'Fantasy', 'Title': 'Demon Lord of Karanda'},
                    {'Author': 'Eddings', 'Category': 'Fiction', 'Publisher': 'None',
                     'Shelf': '34', 'Subject': 'Fantasy', 'Title': "Enchanter's End Game"},
                    {'Author': 'Eddings', 'Category': 'Fiction', 'Publisher': 'None', 'Shelf': '34',
                     'Subject': 'Fantasy', 'Title': 'Guardians of the West'},
                    {'Author': 'Eddings', 'Category': 'Fiction', 'Publisher': 'None', 'Shelf': '34',
                     'Subject': 'Fantasy', 'Title': 'King of the Murgos'},
                    {'Author': 'Eddings', 'Category': 'Fiction', 'Publisher': 'None', 'Shelf': '34',
                     'Subject': 'Fantasy', 'Title': "Magician's Gambit"},
                    {'Author': 'Eddings', 'Category': 'Fiction', 'Publisher': 'None', 'Shelf': '34',
                     'Subject': 'Fantasy', 'Title': 'Pawn of Prophecy'},
                    {'Author': 'Eddings', 'Category': 'Fiction', 'Publisher': 'None', 'Shelf': '34',
                     'Subject': 'Fantasy', 'Title': 'Queen of Sorcery'},
                    {'Author': 'Eddings', 'Category': 'Fiction', 'Publisher': 'None', 'Shelf': '34',
                     'Subject': 'Fantasy', 'Title': 'The Seeress of Kell'},
                    {'Author': 'Eddings', 'Category': 'Fiction', 'Publisher': 'None', 'Shelf': '34',
                     'Subject': 'Fantasy', 'Title': 'The Sorceress of Darshiva'},
                    {'Author': 'Graham', 'Category': 'Fiction', 'Publisher': 'Orbit', 'Shelf': '13',
                     'Subject': 'Fantasy', 'Title': 'Black Ships'},
                    {'Author': 'Hardy', 'Category': 'Fiction', 'Publisher': 'Del Rey', 'Shelf': '14',
                     'Subject': 'Fantasy', 'Title': 'Secret of the Sixth Magic'},
                    {'Author': 'Preston', 'Category': 'Fiction', 'Publisher': 'Warner',
                     'Shelf': '11', 'Subject': 'Thriller', 'Title': 'Riptide'},
                    {'Author': 'Shields', 'Category': 'Mathematics',
                     'Publisher': 'Worth', 'Shelf': '27', 'Subject': 'Algebra',
                     'Title': 'Elementary Linear Algebra 3e'},
                    {'Author': 'Eyewitness Travel', 'Category': 'Travel', 'Publisher': 'DK', 'Shelf': '21',
                     'Subject': 'Italy', 'Title': 'Top 10 Florence and Tuscany'},
                    {'Author': 'Ambroziak','Category': 'Architecture', 'Publisher': 'Princeton Architectural Press',
                     'Shelf': '1', 'Subject': 'Architectural History',
                     'Title': 'Michael Graves Images of a Grand Tour'})

        actual = open_file(test_txt_file)
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_open_file_not_found(self, mock_stdout):
        expected = "File not found\n"
        open_file("fakefile.txt")
        self.assertEqual(mock_stdout.getvalue(), expected)

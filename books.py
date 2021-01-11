import doctest

"""
Kelvin Ngo
A01086182
COMP 1510
Assignment 2 - Book manager
"""


def open_file(txt_file: str) -> tuple:
    """Open and read lines of a file into dictionaries representing books, then place it into library tuple.

    This function opens a text file containing books and turns the first line into a list representing
    tags that can be used as keys in a dictionary. The following lines are then turned into lists,
    and using dictionary comprehension, the list is matched with the tag list to create key: value pairs
    stored in a dictionary representing a book. The "book" is then stored into a list until the for loop
    is complete, then the list is transfigured into a tuple.

    :param txt_file: A text file, encoded in UTF-16 where each line is a book and the tags identifying it.
    The first line of the text file contains the headers for each column of information separated by a tab.
    The subsequent lines contain information matching the header separated by a tab.
    :precondition: The text file passed to the function is in the correct format. The format is each
    line contains information separated by a tab.
    :postcondition: The text file will be turned into a tuple containing dictionaries representing each
    line of the text file. These dictionaries will have their key: value pairs arranged by matching tag and names.
    :return: A library of books represented by dictionaries inside a tuple.

    >>> open_file("wheredidallmybooksgo.txt")
    ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12', 'Category': 'Architecture', '\
Subject': '20th Century'}, {'Author': 'Gaventa', 'Title': 'Concrete Design', 'Publisher': 'Mitchell Beazley', 'Shelf\
': '16', 'Category': 'Architecture', 'Subject': 'Design'}, {'Author': 'Eddings', 'Title': 'Belgarath the Sorcerer\
', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title\
': 'Castle of Wizardry', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author\
': 'Eddings', 'Title': 'Demon Lord of Karanda', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject\
': 'Fantasy'}, {'Author': 'Eddings', 'Title': "Enchanter's End Game", 'Publisher': 'None', 'Shelf': '34', 'Category\
': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': 'Guardians of the West', 'Publisher': 'None\
', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': 'King of the Murgos\
', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title\
': "Magician's Gambit", 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author\
': 'Eddings', 'Title': 'Pawn of Prophecy', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': '\
Fantasy'}, {'Author': 'Eddings', 'Title': 'Queen of Sorcery', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction\
', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': 'The Seeress of Kell', 'Publisher': 'None', 'Shelf': '34\
', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': 'The Sorceress of Darshiva', '\
Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Graham', 'Title': '\
Black Ships', 'Publisher': 'Orbit', 'Shelf': '13', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Hardy\
', 'Title': 'Secret of the Sixth Magic', 'Publisher': 'Del Rey', 'Shelf': '14', 'Category': 'Fiction', 'Subject\
': 'Fantasy'}, {'Author': 'Preston', 'Title': 'Riptide', 'Publisher': 'Warner', 'Shelf': '11', 'Category': 'Fiction\
', 'Subject': 'Thriller'}, {'Author': 'Shields', 'Title': 'Elementary Linear Algebra 3e', 'Publisher': 'Worth', 'Shelf\
': '27', 'Category': 'Mathematics', 'Subject': 'Algebra'}, {'Author': 'Eyewitness Travel', 'Title': '\
Top 10 Florence and Tuscany', 'Publisher': 'DK', 'Shelf': '21', 'Category': 'Travel', 'Subject': 'Italy'}, {'Author\
': 'Ambroziak', 'Title': 'Michael Graves Images of a Grand Tour', 'Publisher': 'Princeton Architectural Press', '\
Shelf': '1', 'Category': 'Architecture', 'Subject': 'Architectural History'})

    >>> open_file("nonexistent.txt")
    File not found
    """
    filename = txt_file
    list_representing_library = []
    try:
        with open(filename, "r", encoding="utf-16") as file_object:
            book_column_tag = file_object.readline().strip().split("\t")

            for line in file_object:
                a_single_book = format_line_to_book(book_column_tag, line)
                list_representing_library.append(a_single_book)

        tolarian_academy_library = tuple(list_representing_library)
        return tolarian_academy_library

    except FileNotFoundError:
        print("File not found")


def format_line_to_book(book_column_tag: list, line: str) -> dict:
    """Format line of a text file representing a book into a dictionary.

    :param book_column_tag: A list containing keys to use for the dictionary.
    :param line: A line in a text file to be converted into values for the dictionary.
    :precondition: book_column_tag is a list containing keys to be used for the dictionary and line is
    a line of a text file containing values separated by a tab to be used in the dictionary.
    :postcondition: This function will take book_column_tag and line to use in dictionary comprehension.
    A dictionary representing a book will be created with key: value pairs representing the book's information.
    :return: A dictionary representing a book.

    >>> test_line = "Herbert\\tDune\\t\\t33\\tFiction\\tSF"
    >>> test_book_column_tag = ["Author", "Title", "Publisher", "Shelf", "Category", "Subject"]
    >>> format_line_to_book(test_book_column_tag, test_line)
    {'Author': 'Herbert', 'Title': 'Dune', 'Publisher': 'None', 'Shelf': '33', 'Category': 'Fiction', 'Subject': 'SF'}
    """
    try:
        book_list = line.strip().split("\t")
        book_list = ["None" if info == "" else info for info in book_list]

        a_single_book = {book_column_tag[column]: book_list[column] for column in range(len(book_column_tag))}
        return a_single_book

    except IndexError:
        return {"oh": "shit", "a": "rat"}


def search_parameter() -> tuple:
    """Ask user for category they wish to search in and the keyword they are searching for.

    :postcondition: Ask user for the category they wish to search in and the keyword they are searching for.
    :return: The user inputs entered for search category and search keyword if correct, else returns empty tuple.
    """
    search_types = {
        "1": "Author",
        "2": "Title",
        "3": "Publisher",
        "4": "Shelf",
        "5": "Category",
        "6": "Subject"
    }

    search_by = input("You can search by:\n\n"
                      "1 for Author\n"
                      "2 for Title\n"
                      "3 for Publisher\n"
                      "4 for Shelf\n"
                      "5 for Category\n"
                      "6 for Subject\n\n"
                      "Enter the number you wish to search by: ")

    if search_by not in search_types:
        print("\nThat search category doesn't exist\n")
        return ()

    search_for = input(f"\nLooking in [{search_types.get(search_by)}], "
                       f"Please enter the keyword you are looking for: ")

    if search_for.strip() == "":
        return search_types.get(search_by), "i messed up"

    else:
        return search_types.get(search_by), search_for.lstrip().rstrip()


def search(library: tuple, search_category: str, keyword: str) -> list:
    """Search the library by a category to find matching results based upon keyword

    :param library: A library represented by a tuple. The tuple contains books represented by dictionaries with
    key: values representing the book's information.
    :param search_category: A string representing the category you wish to search within.
    :param keyword: A string representing the what you wish to search with. Search pull up results that contain
    the string passed. The string passed must be in lowercase.
    :precondition: The library must be the correct data structures and the search parameter must match at least
    one book.
    :postcondition: Any book matching the search parameters will be placed into a list that will be returned.
    :return: A list containing books that match the search parameters.

    >>> search(open_file("wheredidallmybooksgo.txt"), "Author", "edd")
    [{'Author': 'Eddings', 'Title': 'Belgarath the Sorcerer', 'Publisher': 'None', 'Shelf': '34', 'Category': '\
Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': 'Castle of Wizardry', 'Publisher': 'None', 'Shelf\
': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': 'Demon Lord of Karanda', '\
Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': "\
Enchanter's End Game", 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author\
': 'Eddings', 'Title': 'Guardians of the West', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject\
': 'Fantasy'}, {'Author': 'Eddings', 'Title': 'King of the Murgos', 'Publisher': 'None', 'Shelf': '34', 'Category\
': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': "Magician's Gambit", 'Publisher': 'None', '\
Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': 'Pawn of Prophecy', '\
Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': '\
Queen of Sorcery', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': '\
Eddings', 'Title': 'The Seeress of Kell', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction', 'Subject': '\
Fantasy'}, {'Author': 'Eddings', 'Title': 'The Sorceress of Darshiva', 'Publisher': 'None', 'Shelf': '34', '\
Category': 'Fiction', 'Subject': 'Fantasy'}]
    >>> search(open_file("wheredidallmybooksgo.txt"), "Title", "b")
    [{'Author': 'Eddings', 'Title': 'Belgarath the Sorcerer', 'Publisher': 'None', 'Shelf': '34', 'Category': 'Fiction\
', 'Subject': 'Fantasy'}, {'Author': 'Eddings', 'Title': "Magician's Gambit", 'Publisher': 'None', 'Shelf': '34\
', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Graham', 'Title': 'Black Ships', 'Publisher': 'Orbit\', '\
Shelf': '13', 'Category': 'Fiction', 'Subject': 'Fantasy'}, {'Author': 'Shields', 'Title': '\
Elementary Linear Algebra 3e', 'Publisher': 'Worth', 'Shelf': '27', 'Category': 'Mathematics', 'Subject': 'Algebra'}]
    >>> search(open_file("wheredidallmybooksgo.txt"), "Publisher", "None")
    []
    >>> search(open_file("wheredidallmybooksgo.txt"), "Shelf", "12")
    [{'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12', 'Category': 'Architecture\
', 'Subject': '20th Century'}]
    >>> search(open_file("wheredidallmybooksgo.txt"), "Category", "archi")
    [{'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12', 'Category': 'Architecture\
', 'Subject': '20th Century'}, {'Author': 'Gaventa', 'Title': 'Concrete Design', 'Publisher': 'Mitchell Beazley\
', 'Shelf': '16', 'Category': 'Architecture', 'Subject': 'Design'}, {'Author': 'Ambroziak', 'Title': '\
Michael Graves Images of a Grand Tour', 'Publisher': 'Princeton Architectural Press', 'Shelf': '1', 'Category': '\
Architecture', 'Subject': 'Architectural History'}]
    >>> search(open_file("wheredidallmybooksgo.txt"), "Subject", "italy")
    [{'Author': 'Eyewitness Travel', 'Title': 'Top 10 Florence and Tuscany', 'Publisher': 'DK', 'Shelf\
': '21', 'Category': 'Travel', 'Subject': 'Italy'}]
    """
    if keyword == "i messed up":
        return []

    def search_filter() -> list:
        """
        Filter through given books in library to retrieve ones matching category and keyword searched.

        If the category is Shelf and the search is for a numbered shelf, only retrieves for the exact keyword.

        :precondition: search() is being used and the correct parameters are passed to it.
        :postcondition: Comb through a library of books to find matching books.
        :return: A list of matching books.
        """
        try:
            if search_category == "Shelf" and keyword.isdigit():
                list_of_matching_books = [book for book in library if keyword == book["Shelf"]]

            else:
                list_of_matching_books = [book for book in library if keyword in book[search_category].lower()]

            return list_of_matching_books

        except KeyError:
            return []

    return search_filter()


def print_search_results(matching_books: list) -> None:
    """Print the results after searching for books in a library.

    :param matching_books: A list of matching books after a search, where the books are dictionaries with key
    values representing the book's information.
    :precondition: matching_books must be a list object
    :postcondition: If matching_books contains books, they will be printed out in a neat format. Else,
    the function will print out "There are 0 matching result(s)".

    >>> matching_results = search(open_file("wheredidallmybooksgo.txt"), "Category", "architecture")
    >>> print_search_results(matching_results)
    <BLANKLINE>
    Book 1
    +++++++++++++++++++++++++
    Author:   Dupre
    +++++++++++++++++++++++++
    Title:   Skyscrapers
    +++++++++++++++++++++++++
    Publisher:   BD&L
    +++++++++++++++++++++++++
    Shelf:   12
    +++++++++++++++++++++++++
    Category:   Architecture
    +++++++++++++++++++++++++
    Subject:   20th Century
    +++++++++++++++++++++++++
    <BLANKLINE>
    Book 2
    +++++++++++++++++++++++++
    Author:   Gaventa
    +++++++++++++++++++++++++
    Title:   Concrete Design
    +++++++++++++++++++++++++
    Publisher:   Mitchell Beazley
    +++++++++++++++++++++++++
    Shelf:   16
    +++++++++++++++++++++++++
    Category:   Architecture
    +++++++++++++++++++++++++
    Subject:   Design
    +++++++++++++++++++++++++
    <BLANKLINE>
    Book 3
    +++++++++++++++++++++++++
    Author:   Ambroziak
    +++++++++++++++++++++++++
    Title:   Michael Graves Images of a Grand Tour
    +++++++++++++++++++++++++
    Publisher:   Princeton Architectural Press
    +++++++++++++++++++++++++
    Shelf:   1
    +++++++++++++++++++++++++
    Category:   Architecture
    +++++++++++++++++++++++++
    Subject:   Architectural History
    +++++++++++++++++++++++++
    <BLANKLINE>
    There are 3 matching result(s)
    <BLANKLINE>
    """
    if len(matching_books) == 0:
        print("\nThere are 0 matching result(s)\n")

    else:
        for number, result in enumerate(matching_books, 1):
            print(f"\nBook {number}\n+++++++++++++++++++++++++")

            for header, description in result.items():
                print(f"{header}:   {description}\n+++++++++++++++++++++++++")

        print(f"\nThere are {len(matching_books)} matching result(s)\n")


def get_shelves(library: tuple) -> list:
    """Create a list containing the shelves of a library

    :param library: A library represented by a tuple, containing books represented by dictionaries.
    :precondition: A tuple containing dictionaries representing a library full of books is passed into the function.
    :postcondition: This function will add the value of each "Shelf" key into a set to prevent duplicates.
    The value will be placed into different sets depending on if it is a number or word. Then the sets are turned
    into sorted lists and concatenated to each other.
    :return: An ordered list containing the different shelves in the library.

    >>> get_shelves(open_file("wheredidallmybooksgo.txt"))
    ['1', '11', '12', '13', '14', '16', '21', '27', '34']
    """
    set_of_shelves_num = set()
    set_of_shelves_alpha = set()

    for book in library:

        if book.get("Shelf").isalpha():
            set_of_shelves_alpha.add(book.get("Shelf"))

        else:
            set_of_shelves_num.add(int(book.get("Shelf")))

    book_shelves = [str(number) for number in sorted(set_of_shelves_num)] + sorted(list(set_of_shelves_alpha))
    return book_shelves


def get_book_location(list_of_books: list) -> dict:
    """Grab a book from a list of books by the title.

    :param list_of_books: A list of books that are represented by dictionaries.
    :precondition: The list passed into the function contains dictionaries representing books.
    :postcondition: Asks the user to enter the number of the book they wish to choose. Then, the number entered
    will be subtracted by one and used as an index to grab the book from a the list.
    :return: Either the dictionary representing a book or an empty dictionary representing a non-existent book
    """
    get_book = input("\nPlease enter the number of the book you wish to choose: ")

    try:
        return list_of_books[int(get_book) - 1]

    except (IndexError, ValueError):
        print("\nThere is no book in that location.\n")
        return {}


def move(shelves: list, book: dict) -> None:
    """Move a book from one shelf to another.

    :param shelves: A list containing different shelves of a library
    :param book: A book represented by a dictionary containing the information of the book.
    :precondition: The parameters passed are a list and dictionary representing a library's shelves and a book.
    :postcondition: Asks the user which shelf they would like to move the book to. Then the dictionary representing
    the book will have the value of the "Shelf" key changed to the new shelf.
    """
    print(f"Here are your current shelves\n\n{shelves}")
    new_shelf = input("\nWhat shelf would you like to move your book to?"
                      " Use proper capitalization for worded shelves: ")

    if new_shelf not in shelves:
        print("\nThat shelf does not exist.\n")

    else:
        book["Shelf"] = new_shelf
        print(f"\nCongratulations, you have successfully moved the book to Shelf {new_shelf}\n")


def menu() -> str:
    """Display a menu with options user can choose from.

    :postcondition: Prints out the options a user can choose from. Then the user inputs a number representing their
    chosen menu option. The input will be passed to grab the correct option from the dictionary of options by key.
    :return: A string representing the chosen option unless it is quit. Quit will return False instead.
    """
    menu_options = {
        "1": "search",
        "2": "move",
        "3": "False"
    }

    menu_select = input("Here are your menu options:\n\n"
                        "1 to SEARCH for books\n"
                        "2 to MOVE a single book to a new shelf\n"
                        "3 to QUIT and save changes to your current library\n\n"
                        "Please enter a number that matches the option you wish to select: ")

    if menu_select in menu_options.keys():
        return menu_options.get(menu_select)

    else:
        print("\nThat command doesn't exist, try again.\n")
        return "not quite my tempo"


def format_book_to_line(book: dict) -> str:
    """Format a dictionary of books into a string with values separated by a tab.

    :param book: A dictionary representing a book, containing key value pairs that show the book's information.
    :precondition: The dictionary representing the book has the key: value pairs representing the book's
    information.
    :postcondition: Creates a string where each value is separated by a tab. If the parameter passed is not a
    dict containing the correct key: value pairs, a silly message is outputted.
    :return: A string that represents the information of a book in a single line.

    >>> test_book = {'Author': 'Eddings', 'Title': 'Belgarath the Sorcerer', 'Publisher': 'None', 'Shelf': '34'\
    , 'Category': 'Fiction', 'Subject': 'Fantasy'}
    >>> format_book_to_line(test_book)
    'Eddings\\tBelgarath the Sorcerer\\tNone\\t34\\tFiction\\tFantasy'
    """
    try:
        a_book = [str(value) for value in book.values()]
        return "\t".join(a_book)

    except (TypeError, IndexError, AttributeError):
        print("These aren't the droids you are looking for")


def grab_headers(book: dict) -> str:
    """Format the keys of a dictionary of books into a header with elements separated by a tab.

    :param book: A dictionary representing a book, containing key value pairs that show the book's information
    :precondition: The dictionary representing the book has the key: value pairs representing the book's
    information.
    :postcondition: Creates a string where each key is separated by a tab. If the parameter passed is not a
    dict containing the correct key: value pairs, a silly message is outputted.
    :return: A string that represents the headers of information columns for a library of books.

    >>> test_book = {'Author': 'Suess', 'Category': 'Fiction', 'Publisher': 'None', 'Shelf': 'widepeepoHappy'\
    , 'Subject': 'Picture Book', 'Title': 'Green Eggs and Ham'}
    >>> grab_headers(test_book)
    'Author\\tCategory\\tPublisher\\tShelf\\tSubject\\tTitle'
    """
    try:
        the_header = [key for key in book.keys()]
        return "\t".join(the_header)

    except (TypeError, IndexError, AttributeError):
        print("These aren't the droids you are looking for")


def quit_book_program(library: tuple[dict], current_file):
    """Dump data from library of books into a plaintext file.

    :param library: A tuple data structure representing a library containing dictionaries representing books.
    :param current_file: The name of the text file currently being edited.
    :precondition: Library is a tuple containing dictionaries with the correct keys to represent a book.
    :postcondition: The function will write the headers for the first line. Then, in each matching column below,
    the values of the dictionary will be written into the text file ordered by keys that match the header.
    The current text file being used will be overwritten by any changes made while moving books to new shelves.
    Then a farewell message is printed
    """
    filename = current_file

    with open(filename, "w", encoding="utf-16") as file_object:
        file_object.write(f"{grab_headers(library[0])}\n")

        for book in library[:-1]:
            file_object.write(f"{format_book_to_line(book)}\n")

        file_object.write(format_book_to_line(library[-1]))
        print("\nProgram shutting down...")


def books():
    """Execute a program to let you search for books and move them.

    This function contains all the helper functions necessary to allow the user to manipulate a library of books.
    These books will be represented by dictionaries with ordered key: value pairs representing the book's information
    When you run the function, it will open a plain text file that contains books. The plaintext file should be
    encoded in "utf-16".The text inside the file should have the first line contain text representing keys for the
    information values The subsequent lines will have the information of the book as values matching the
    keys in the first line. Pass your chosen plaintext library as a parameter into open_file() and the function
    will turn it into a tuple containing each line (book) represented by a dictionary. The menu options are placed
    in a while loop so the function will continue running until you input 3 (which represents QUIT),
    into the main menu prompt.

    :postcondition: After running the function, the user will be able to access a program that allows them
    to search for books by category and keyword(s), move a book to a different shelf, and quit the program.
    Quitting the program will create a new plaintext file that represents the library of books including any changes
    made by moving the books to different shelves.
    """
    library_of_alexandria = open_file("Books UTF-16.txt")
    i_am_sentinel = "True"
    list_of_shelves = get_shelves(library_of_alexandria)
    print("Welcome to The Library. Please read the following prompts carefully.\n")

    while i_am_sentinel != "False":
        lemme_check_if_you_wanna_quit = menu()

        if lemme_check_if_you_wanna_quit == "search":
            search_for = search_parameter()

            if search_for == ():
                continue

            print_search_results(search(library_of_alexandria, *search_for))

        elif lemme_check_if_you_wanna_quit == "move":
            retrieve_books = search_parameter()

            if retrieve_books == ():
                continue

            list_of_books = search(library_of_alexandria, *retrieve_books)
            print_search_results(list_of_books)

            if len(list_of_books) == 0:
                continue

            book_location = get_book_location(list_of_books)

            if book_location == {}:
                continue

            move(list_of_shelves, book_location)

        elif lemme_check_if_you_wanna_quit == "False":
            quit_book_program(library_of_alexandria, "Books UTF-16.txt")
            i_am_sentinel = lemme_check_if_you_wanna_quit


def main():
    """Execute file."""
    doctest.testmod()
    books()


if __name__ == "__main__":
    main()

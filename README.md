# Books Manager

Books Manager is a program built in Python that allows a user to search for and edit books stored in a plain text file. Below the first line containing the headers,
each line contains a book's information such as title, author name, etc. separated by tab and allows the user to seach for books by one of those categories with a partial match.
The user can choose a single book and edit any piece of information. When the user is done, any changes made to the books will be rewritten in the plain text file.

## Description

This is a program I wrote for an assignment in my programming methods course. I'm keeping this here to be able to look back and see how much I have improved since then. Looking back, I would use a single Try-Except block inside the books function to catch any wrong inputs instead of multiple if statements. We were expected to use nested dictionaries inside a tuple for this assignment. But if I had to do something like this in the future, perhaps I would place the nested dictionaries inside another dictionary to represent shelves, with keys representing a spot in the shelf.

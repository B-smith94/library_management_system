# Library Management System

Author: Byron Smith

Date: 9/10/24

Welcome to the Library Management System! Please read the following instructions before using the program.

## Table of Contents:

### 1. Navigating the Main Menu
### 2. Book Operations
### 3. User Operations
### 4. Author Operations


## 1. Navigating the Main Menu

When you first start the program, the following menu will appear:

    Welcome to the Library Management System!

    Main Menu:
    1. Book Operations
    2. User Operations
    3. Author Operations
    4. Quit

The program will prompt you to input a number between 1 and 4, in order to select a menu item:

    What would you like to do? (enter 1, 2, 3, or 4 for the menu choices listed above): |

__NOTE__: In order to use some of the book operations, a username and Library ID number will need to be generated first. To do that, enter '2' when prompted on the main menu. For more instructions on user operations, see __User Operations__.

Entering in a number will take you to the associated submenu for each item. Entering '4' will automatically back up any changes you made to the data stored within the program, and then quit the program.

## 2. Book Operations

When you enter '2' in the Main Menu, it will take you to the Book Operations submenu:

        Book Operations:
        1. Add a new book
        2. Borrow a book
        3. Return a book
        4. Search for a book
        5. Display all books

The program will once again ask you to enter a number cooresponding with the desired menu choice:

    Which operation woul dyou like to perform? (1, 2, 3, 4, 5): |

Entering '1' will prompt the program to ask you for details about the book you wish to add:

    Enter the title of the book you wish to add: |
    Please enter the author: |
    Please enter the genre (example: fantasy): |
    What year was {book} published? (yyyy): |

Once done, it will then add the book with all it's information to a local database.

Entering '2' will ask for your username and Library ID. __REMINDER__: you MUST have a username and library ID in order to borrow or return books. For information on how to create a username and ID, see __User Operations__.

    Please enter your username: |
    Please enter your 6 character Library ID: |

Once the program has verified your identity, it will then ask you to provide the title of the book you wish to borrow:

    Please enter the name of the book you wish to borrow: |

The book will then register that you are borrowing the book, and edit the appropriate data.

Entering '3' will allow you to return a book you previously borrowed. As before, the program will ask you to enter your username and library ID before further action is taken.
Once it verifies your identity, it will ask you to enter in the title of the book you wish to return:

    Please enter the name of the book you wish to return: |

The program will then update the relevant data and register that you have returned your book.

Entering '4' will allow you to look up a specific title:

    Please enter the title of the book you wish to search for: |

It will then display the information for that book in the following format:

    Book: {book title}
       Author: {name of the author}
       Genre: {genre}
       Publication Date: {publication date}
       Availability: In Stock/Out of Stock (If it is already loaned out, this will display Out of Stock)

Entering '5' will display all available books in the above format.

## 3. User Operations

When you enter '2' on the Main Menu, the program will take you to the User Operations submenu:

        User Operations:
        1. Add a new user
        2. View user details
        3. Display all users

Entering '1' will allow you to create a user profile. It will prompt you to create a username:

    Please enter a username:  |

If the username is already created, it will tell you that the username is invalid and give you the opportunity to try again.
If the username is available, the program will then tell you it was successfull, and then provide you with a 6 character Library ID:

    Unique Library Identifier (Library ID)(Do NOT share with others): ABC123

This Library ID acts like a password to your username and ensures that only you will be able to check out or return books in your name.

Entering '2' will allow you to search for specific users in the User ID database. It will prompt you to enter a username and password:

    Please enter the username you wish to search: |
    Please enter your Library ID Number: |

If the Library ID matches the username you are searching, it will display the details in the following manner:

    Username: {username}
       Library ID: ABC123
       Checked Out Books: {}
If the Library ID and username do not match, it will display 'REDACTED' instead of the Library ID. In both cases, the program will display any books associated with the username in 'Checked Out Books'.

Entering '3' will display all usernames in the database, with the Library ID displaying 'REDACTED'.

## 4. Author Operations

When you enter '3' on the Main Menu, the program will take you to the Author Operations submenu:

        Author Operations:
        1. Add a new author
        2. View author details
        3. Display all authors

Entering '1' will allow you to enter in the details of the author you wish to add:

    Enter the name of the author you wish to add: |
    Enter {author}'s date of birth (mm/dd/yyyy): |
    Enter {author}'s date of death (mm/dd/yyyy or 'present' if they are still alive): |

__NOTE__: You MUST include the backslash between the month, day, and year of each date, or the program will not accept your input.

Entering '2' will allow you to view the details of a specific author, according to our records. It will prompt you to enter the name of the author in question:

    Enter the name of the author you wish to view: |

If the author is found in our database, the program will then display the author and their biographical information in the following format:

    Author: {Author Name}
       Date of Birth: dd/mm/yyyy
       Date of Death: dd/mm/yyyy (N/A if the author is still alive)

Entering '3' will display all of the authors in our database in the above format.
       

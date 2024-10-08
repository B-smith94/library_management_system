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
    ****
    Main Menu:
    1. Book Operations
    2. User Operations
    3. Author Operations
    4. Quit

The program will prompt you to input a number between 1 and 4, in order to select a menu item:

    What would you like to do? (enter 1, 2, 3, or 4 for the menu choices listed above): |

__NOTE__: In order to use some of the book operations, a Library ID number will need to be generated first. To do that, enter '2' when prompted on the main menu. For more instructions on user operations, see __User Operations__.

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

    Which operation would you like to perform? (1, 2, 3, 4, 5): |

Entering '1' will prompt the program to ask you for details about the book you wish to add:

    --Book Operation 1: Add a New Book--
    
    Enter the title of the book you wish to add: |
    Please enter the author: |
    Please enter the ISBN number for {book}: |
    When was {book} published? (yyyy-mm-dd): |

Once done, it will then add the book with all it's information to a local database.

Entering '2' will ask for your username and Library ID. __REMINDER__: you MUST have a Library ID in order to borrow or return books. For information on how to create a Library ID, see __User Operations__.

    Please enter your first and last name: |
    Please enter your 6 character Library ID: |

Once the program has verified your identity, it will then ask you to provide the title of the book you wish to borrow and the date it was borrowed on:

    Please enter the name of the book you wish to borrow: |
    Enter the date the book was borrowed (yyyy-mm-dd): |

The book will then register that you are borrowing the book, and edit the appropriate data.

Entering '3' will allow you to return a book you previously borrowed. As before, the program will ask you to enter your name and library ID before further action is taken.
Once it verifies your identity, it will ask you to enter in the title of the book you wish to return:

    Please enter the name of the book you wish to return: |
    Enter the date the book was returned: (yyyy-mm-dd): |

The program will then update the relevant data and register that you have returned your book.

Entering '4' will allow you to look up a specific title:

    Please enter the title of the book you wish to search for: |

It will then display the information for that book in the following format:

    Book: {book title}
       Author: {Author name}
       ISBN: {ISBN number}
       Publication Date: {publication date}
       Availability: In Stock/Out of Stock (If it is already loaned out, this will display Out of Stock)

Entering '5' will display all available books in the above format.

## 3. User Operations

When you enter '2' on the Main Menu, the program will take you to the User Operations submenu:

    User Operations:
    1. Add a new user
    2. View user details
    3. Display all users

Entering '1' will allow you to create a user profile. It will prompt you to enter your first and last name:

    Enter your first and last name:  |

If your first and last name were entered, the program will then tell you it was successfull, and then provide you with a 6 character Library ID:

    Unique Library Identifier (Library ID)(Do NOT share with others): ABC123

This Library ID acts like a password/unique identifier and ensures that only you will be able to check out or return books in your name.
__NOTE__: You must enter both your first and last name in order to recieve a Library ID. If you do not, the program will display an error message and prompt you to enter it in again.

Entering '2' will allow you to search for specific users in the User ID database. It will prompt you to enter a username and password:

    Please enter your first and last name: |
    Please enter your Library ID Number: |

If the Library ID and name match, it will display the details in the following manner:

       Name: {name}
       Library ID: ABC123
       Checked Out Books: [{book title}, borrowed on {date borrowed}]
       
If the user has not checked out any books at the moment, the program will display "None". If the Library ID and name do not match, the program will let you know, then return to the main menu. 

Entering '3' will display a list containing the names of all the users in the database. It will not show which books they've checked out, nor will it show any users' Library ID.

## 4. Author Operations

When you enter '3' on the Main Menu, the program will take you to the Author Operations submenu:

    Author Operations:
    1. Add a new author
    2. View author details
    3. Display all authors

Entering '1' will allow you to enter in the details of the author you wish to add:

    Enter the name of the author you wish to add: |
    Enter {author}'s date of birth (yyyy-mm-dd): |
    Enter {author}'s date of death (yyyy-mm-dd or 'present' if they are still alive): |

__NOTE__: You MUST include the backslash between the month, day, and year of each date, or the program will not accept your input.

Entering '2' will allow you to view the details of a specific author, according to our records. It will prompt you to enter the name of the author in question:

    Enter the name of the author you wish to view: |

If the author is found in our database, the program will then display the author and their biographical information in the following format:

    Author: {Author Name}
       Birthday: {yyyy-mm-dd}; Date of Death: yyyy-mm-dd (N/A if the author is still alive)

Entering '3' will display all of the authors in our database in the above format.
       

import operations
import re

user_id = {}
library_books = {}
author_details = {}

def main():
    while True:
        print("Welcome to the Library Management System!\n")
        print("Main Menu:")
        print("1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit")
        main_menu_choice = input("What would you like to do? (enter 1, 2, 3, or 4 for the menu choices listed above): ")
        if main_menu_choice == "4":
            print("Have a nice day!")
            break
        else:
            if main_menu_choice == "1":
                print("\tBook Operations:")
                print("\t1. Add a new book\n\t2. Borrow a book\n\t3. Return a book\n\t4. Search for a book\n\t5. Display all books.")
                book_ops_choice = input("Which operation would you like to perform? (1, 2, 3, 4, or 5): ")
                if book_ops_choice == "1":
                    book = input("Enter the title of the book you wish to add: ").title()
                    author = input("Please enter the author: ").title()
                    genre = input("Please enter the genre (example: fantasy): ").capitalize()
                    pub_date = input(f"What year was {book} published? (yyyy): ")
                    operations.BookOperations.add_new_book(library_books, book, author, genre, pub_date)
                    print(library_books)
                elif book_ops_choice == "2":
                    pass
                elif book_ops_choice == "3":
                    pass
                elif book_ops_choice == "4":
                    pass
                elif book_ops_choice == "5":
                    operations.BookOperations.display_books(library_books)
                elif book_ops_choice != re.search(["1-5"]):
                    print("You must enter a number between 1 and 5.")
                else:
                    print(f"{book_ops_choice} is not an available option.\n")
            elif main_menu_choice == "2":
                print("\tUser Operations:")
                print("\t1. Add a new user\n\t2. View user details\n\t3. Display all users")
                user_ops_choice = input("Which operation would you like to perform? (1, 2, 3, 4, or 5): ")
                if user_ops_choice == "1":
                    pass
                elif user_ops_choice == "2":
                    pass
                elif user_ops_choice == "3":
                    pass
                elif user_ops_choice != re.search(["1-3"]):
                    print("You must enter a number between 1 and 3.")
                else:
                    print(f"{user_ops_choice} is not an available option.\n")
            elif main_menu_choice == '3':
                print("\tAuthor Operations:")
                print("\t1. Add a new author\n\t2. View author details\n\t3. Display all authors")
                author_ops_choice = input("Which operation would you like to perform? (1, 2, 3, 4, or 5): ")
                if author_ops_choice == "1":
                    pass
                elif author_ops_choice == "2":
                    pass
                elif author_ops_choice == "3":
                    pass
                elif author_ops_choice != re.search(["1-3"]):
                    print("You must enter a number between 1 and 3.")
                else:
                    print(f"{author_ops_choice} is not an available option.\n")
            else:
                print(f"{main_menu_choice} is not available.\n")

if __name__ == "__main__":
    main()
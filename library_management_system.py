import book_operations
import user_operations
import author_operations
import re

user_id = {}
library_books = {}
author_details = {}

def main():
    while True:
        print("Welcome to the Library Management System!\n")
        print("Main Menu:\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit")
        print("")
        print("Please create a username before borrowing any books.")
        main_menu_choice = input("What would you like to do? (enter 1, 2, 3, or 4 for the menu choices listed above): ")
        match = re.search("[1-5]", main_menu_choice)
        if not match:
            print("You must enter a number between 1 and 4.")
            continue
       
        if main_menu_choice == "4":
            print("Have a nice day!")
            break
       
        else:
            if main_menu_choice == "1":
                print("\tBook Operations:")
                print("\t1. Add a new book\n\t2. Borrow a book\n\t3. Return a book\n\t4. Search for a book\n\t5. Display all books.")
                book_ops_choice = input("Which operation would you like to perform? (1, 2, 3, 4, or 5): ")
                match = re.search("[1-5]", book_ops_choice)
                
                if not match:
                    print("You must enter a number between 1 and 5.")
                
                if book_ops_choice == "1":
                    book = input("Enter the title of the book you wish to add: ").title()
                    author = input("Please enter the author: ").title()
                    genre = input("Please enter the genre (example: fantasy): ").capitalize()
                    pub_date = input(f"What year was {book} published? (yyyy): ")
                    book_operations.BookOperations.add_new_book(library_books, book, author, genre, pub_date)
                    print(library_books)
                
                elif book_ops_choice == "2":
                    username = input("Please enter your username: ")
                    book = input("Please enter the name of the book you wish to borrow: ").title()
                    book_operations.BookOperations.borrow_book(library_books, user_id, book, username)
                
                elif book_ops_choice == "3":
                    username = input("Please enter your username: ")
                    book = input("Please enter the name of the book you wish to return: ").title()
                    book_operations.BookOperations.return_book(library_books, user_id, book, username)
                
                elif book_ops_choice == "4":
                    title = input("Please enter the title of the book you wish to search for: ").title()
                    book_operations.BookOperations.search_books(library_books, title)
                
                elif book_ops_choice == "5":
                    book_operations.BookOperations.display_books(library_books)
                
                else:
                    print(f"{book_ops_choice} is not an available option.\n")
            
            elif main_menu_choice == "2":
                print("\tUser Operations:")
                print("\t1. Add a new user\n\t2. View user details\n\t3. Display all users")
                user_ops_choice = input("Which operation would you like to perform? (1, 2, or 3): ")
                match = re.search("[1-3]", user_ops_choice)
                if not match:
                    print("You must enter a number between 1 and 3.")
                
                if user_ops_choice == "1":
                    while True:
                        username = input("Please enter a username: ")
                        if username in user_id:
                            print(f"{username} is not a valid username. Please try again.")
                            continue
                        
                        else:
                            user_operations.UserOperations.add_new_user(user_id, username)
                            print("User added Successfully! Returning to the Main Menu.")
                            break

                elif user_ops_choice == "2":
                    username = input("Please enter your username: ")
                    library_id = input("please enter your Library ID Number: ").upper()
                    user_operations.UserOperations.view_user_details(user_id, username, library_id)
                    
                elif user_ops_choice == "3":
                    user_operations.UserOperations.display_users(user_id)
                
                else:
                    print(f"{user_ops_choice} is not an available option.\n")
            
            elif main_menu_choice == '3':
                print("\tAuthor Operations:")
                print("\t1. Add a new author\n\t2. View author details\n\t3. Display all authors")
                author_ops_choice = input("Which operation would you like to perform? (1, 2, or 3): ")
                match = re.search("[1-3]", author_ops_choice)
                
                if not match:
                    print("You must enter a number between 1 and 3.")
                
                if author_ops_choice == "1":
                    author_name = input("Enter the name of the author you wish to add: ").title()
                    author_birth = input(f"Enter {author_name}'s date of birth (dd/mm/yyyy): ")
                    author_death = input(f"Enter {author_name}'s date of death (dd/mm/yyyy or 'present' if they are still alive): ")
                    if author_death == "present":
                        author_death = "N/A"
                    author_operations.AuthorOperations.add_new_author(author_details, author_name, author_birth, author_death)
                    print(f"{author_name} added to registry!")
                
                elif author_ops_choice == "2":
                    author = input("Enter the full name of the author you wish to view: ").title()
                    author_operations.AuthorOperations.view_author_details(author_details, author)
                
                elif author_ops_choice == "3":
                    author_operations.AuthorOperations.display_all_authors(author_details)
                
                else:
                    print(f"{author_ops_choice} is not an available option.\n")
            

if __name__ == "__main__":
    main()
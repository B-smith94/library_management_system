import operations

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
                    pass
                elif book_ops_choice == "2":
                    pass
                elif book_ops_choice == "3":
                    pass
                elif book_ops_choice == "4":
                    pass
                elif book_ops_choice == "5":
                    pass
            elif main_menu_choice == "2":
                print("\tUser Operations:")
                print("\t1. Add a new user\n\t2. View user details\n\t3. Display all users")
                book_ops_choice = input("Which operation would you like to perform? (1, 2, 3, 4, or 5): ")
                if book_ops_choice == "1":
                    pass
                elif book_ops_choice == "2":
                    pass
                elif book_ops_choice == "3":
                    pass
            else:
                print("\tAuthor Operations:")
                print("\t1. Add a new author\n\t2. View author details\n\t3. Display all authors")
                book_ops_choice = input("Which operation would you like to perform? (1, 2, 3, 4, or 5): ")
                if book_ops_choice == "1":
                    pass
                elif book_ops_choice == "2":
                    pass
                elif book_ops_choice == "3":
                    pass

if __name__ == "__main__":
    main()
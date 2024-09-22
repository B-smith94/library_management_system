import book_operations
import user_operations
import author_operations
import re

def main():
    while True:    
        print("\nWelcome to the Library Management System!\n****")
        print("Main Menu:\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit")
        print("Please create a username before borrowing any books.")
        main_menu_choice = input("What would you like to do? (enter 1, 2, 3, or 4 for the menu choices listed above): ")
        match = re.search(r"[1-5]", main_menu_choice)
        if not match:
            print("You must enter a number between 1 and 4.")
            continue
       
        if main_menu_choice == "4":
            print("Have a nice day!")
            break
       
        else:
            if main_menu_choice == "1":
                print("\nBook Operations:")
                print("1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books.")
                book_ops_choice = input("Which operation would you like to perform? (1, 2, 3, 4, or 5): ")
                match = re.search("[1-5]", book_ops_choice)
                
                if not match:
                    print("You must enter a number between 1 and 5.")
                
                if book_ops_choice == "1":
                    print("\n--Book Operation 1: Add a New Book--\n")
                    book = input("Enter the title of the book you wish to add: ").title()
                    author = input("Please enter the author: ").title()
                    isbn = input(f"Please enter the ISBN number for {book}: ")
                    while True:
                        pub_date = input(f"When was {book} published? (yyyy-mm-dd): ")
                        date_format = re.match(r"(\d{4})-(\d{2})-(\d{2})", pub_date)
                        if not date_format:
                            print("Invalid, please use the correct format.")
                            continue
                        else:
                            break
                    author_id = author_operations.AuthorOperations.retrieve_author_id(author)
                    book_operations.BookOperations.add_new_book(book, author_id, isbn, pub_date)
                
                elif book_ops_choice == "2":
                    print("\n--Book Operation 2: Borrow a Book--\n")
                    name = input("Please enter your first and last name: ").title()
                    library_id = input("Please enter your 6 character Library ID: ").upper()
                    verification = user_operations.UserOperations.verify_library_id(name, library_id)
                    if verification is True:
                        book = input("Please enter the name of the book you wish to borrow: ").title()
                        while True:
                            borrow_date = input(f"Enter the date the book was borrowed: (yyyy-mm-dd): ")
                            date_format = re.match(r"(\d{4})-(\d{2})-(\d{2})", borrow_date)
                            if not date_format:
                                print("Invalid, please use the correct format.")
                                continue
                            else:
                                break
                        user_id = user_operations.UserOperations.retrieve_user_id(name)
                        book_id = book_operations.BookOperations.retrieve_book_id(book)
                        book_operations.BookOperations.borrow_book(user_id, book_id, borrow_date)
                    else:
                        print("Name and Library_ID do not match, please try again.")
            
                elif book_ops_choice == "3":
                    print("\n--Book Operation 3: Return a Book--\n")
                    while True:
                        name = input("Enter your first and last name: ").title()
                        name_format = re.match(r"[A-Za-z\sA-Za-z]", name)
                        if not name_format:
                            print("Did not include both first and last name, please try again.")
                            continue
                        else:
                            break
                    library_id = input("Please enter your 6 character Library ID: ").upper()
                    verification = user_operations.UserOperations.verify_library_id(name, library_id)
                    if verification is True:
                        book = input("Please enter the title of the book you wish to return: ").title()
                        while True:
                            return_date = input(f"Enter the date the book was returned: (yyyy-mm-dd): ")
                            date_format = re.match(r"(\d{4})-(\d{2})-(\d{2})", return_date)
                            if not date_format:
                                print("Invalid, please use the correct format.")
                                continue
                            else:
                                break
                        user_id = user_operations.UserOperations.retrieve_user_id(name)
                        book_id = book_operations.BookOperations.retrieve_book_id(book)
                        book_operations.BookOperations.return_book(user_id, book_id, return_date)
                    else:
                        print("Name and Library_ID do not match, please try again.")
                
                elif book_ops_choice == "4":
                    print("\n--Book Operation 4: Search for a Book--\n")
                    title = input("Please enter the title of the book you wish to search for: ").title()
                    book_operations.BookOperations.search_books(title)
                
                elif book_ops_choice == "5":
                    print("\n--Book Operation 5: Display all Books--\n")
                    book_operations.BookOperations.display_books()
                
                else:
                    print(f"{book_ops_choice} is not an available option.\n")
            
            elif main_menu_choice == "2":
                print("\nUser Operations:")
                print("1. Add a new user\n2. View user details\n3. Display all users")
                user_ops_choice = input("Which operation would you like to perform? (1, 2, or 3): ")
                match = re.search(r"[1-3]", user_ops_choice)
                if not match:
                    print("You must enter a number between 1 and 3.")
                
                if user_ops_choice == "1":
                    print("\n--User Operation 1: Add a New user--\n")
                    while True:
                        name = input("Enter your first and last name: ").title()
                        name_format = re.match(r"[A-Za-z\sA-Za-z]", name)
                        if not name_format:
                            print("Did not include both first and last name, please try again.")
                            continue
                        else:
                            user_operations.UserOperations.add_new_user(name)
                            break

                elif user_ops_choice == "2":
                    print("\n--User Operation 2: View User Details--\n")
                    while True:
                        name = input("Enter your first and last name: ").title()
                        name_format = re.match(r"[A-Za-z\sA-Za-z]", name)
                        if not name_format:
                            print("Did not include both first and last name, please try again.")
                            continue
                        else:
                            break
                    library_id = input("Please enter your Library ID Number: ").upper()
                    verification = user_operations.UserOperations.verify_library_id(name, library_id)
                    if verification is True:
                        user_operations.UserOperations.view_user_details(name)
                    else:
                        print("Name and Library ID do not match, please try again.")
                    
                elif user_ops_choice == "3":
                    print("\n--User Operation 3: Display All Users--\n")
                    user_operations.UserOperations.display_users()
                
                else:
                    print(f"{user_ops_choice} is not an available option.\n")
            
            elif main_menu_choice == '3':
                print("\nAuthor Operations:")
                print("1. Add a new author\n2. View author details\n3. Display all authors")
                author_ops_choice = input("Which operation would you like to perform? (1, 2, or 3): ")
                match = re.search(r"[1-3]", author_ops_choice)
                
                if not match:
                    print("You must enter a number between 1 and 3.")
                
                if author_ops_choice == "1":
                    print("\n--Author Operation 1: Add A New Author--\n")
                    author_name = input("Enter the name of the author you wish to add: ").title() 
                    while True:
                        author_birth = input(f"Enter {author_name}'s date of birth (yyyy-mm-dd): ")
                        date_format = re.match(r"(\d{4})-(\d{2})-(\d{2})", author_birth)
                        if not date_format:
                            print("Invalid, please use the correct format.")
                            continue
                        else:
                            break
                    while True:
                        author_death = input(f"Enter {author_name}'s date of death (yyyy-mm-dd or 'present' if they are still alive): ")
                        if author_death == "present":
                            author_death = "N/A"   
                            break
                        else:
                            date_format = re.match(r"(\d{4})-(\d{2})-(\d{2})", author_death)
                            if not date_format:
                                print("Invalid, please use the correct format.") 
                                continue
                            else:
                                break  
                    author_operations.AuthorOperations.add_new_author(author_name, author_birth, author_death)
                
                elif author_ops_choice == "2":
                    print("\n--Author Operation 2: View Author Details--\n")
                    author = input("Enter the name of the author you wish to view: ").title()
                    author_operations.AuthorOperations.view_author_details(author)
                
                elif author_ops_choice == "3":
                    print("\n--Author Operation 3: Display All Authors--\n")
                    author_operations.AuthorOperations.display_all_authors()
                
                else:
                    print(f"{author_ops_choice} is not an available option.\n")
            

if __name__ == "__main__":
    main()
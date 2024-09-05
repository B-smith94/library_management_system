class BookOperations:
    def __init__(self, book, author):    
        self = dict()
        self.book = book
        self.author = author
        
    def add_new_book(self, book, author):
        if book not in self:
            try:
                self[book] = author
                print(f"\n{book} by {author} added to library stock.\n")
            except Exception as e:
                print(f"An error has occurred: {e}")
        else:
            print(f"\n{book} is already in the library.")

    def borrow_book(self, book, author):
        pass

    def return_book(self, book, author):
        pass

    def search_books(self, book, author):
        pass

    def display_books(self):
        for book, author in self.items():
            print(f"--{book} by {author}")
            
            
class UserOperations(BookOperations):
    def __init__(self, username, library_id, book):
        super().__init__(book)
        self.__username = username
        self.__library_id = library_id

    def add_new_user(self, username, library_id):
        print("New user added.")
        pass

    def view_user_details(self, username):
        pass

    def display_users(self):
        pass

class AuthorOperations(BookOperations):
    def __init__(self, author):
        super().__init__(author)

    def view_author_details(self, author):
        pass

    def display_all_authors(self):
        pass
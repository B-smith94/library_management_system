class LibraryBookBackup:
    def __init__(self, library_dict):
        self.library_dict = dict()

    def book_backup(self, library_dict):
        with open('book_backup.txt', 'w') as file:
            for book, category in library_dict.items():
                file.write(f"{book}: {category}, ")
                

    def get_books_from_file(self, book_dict):
        with open('book_backup.txt', 'r') as file:
            for line in file:
                pass

class UserInfoBackup:
    def __init__(self, user_dict):
        self.user_dict = dict()

    def user_backup(self, user_dict):
        with open('user_backup.txt', 'w') as file:
            for user, category in user_dict.items():
                file.write(f"{user}: {category}, ")
    
    def get_users_from_file(self, user_dict):
        with open('user_backup.txt', 'r') as file:
            for line in file:
                pass

class AuthorInfoBackup:
    def __init__(self, author_dict):
        self.author_dict = dict()
    
    def author_backup(self, author_dict):
        with open('author_backup.txt', 'w') as file:
            for author, category in author_dict.items():
                file.write(f"{author}: {category}, ")

    def get_authors_from_file(self, author_dict):
        with open('author_backup.txt', 'r') as file:
            for line in file:
                pass
                
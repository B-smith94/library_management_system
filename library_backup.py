class LibraryBookBackup:
    def __init__(self, library_dict):
        self.library_dict = dict()

    def book_backup(self, library_dict):
        with open('book_backup.txt', 'w') as file:
            for book, category in library_dict.items():
                file.write(f"{book}\n{category}\n")

    def get_books_from_file(self, book_dict):
        i = 0
        with open('book_backup.txt', 'r') as file:
            for line in file.readlines():
                try:
                    if i % 2 == 0:
                        book = line.strip('\n')
                    elif i % 2 != 0:
                        detail = line.strip('\n')
                        details = eval(detail)
                    i += 1
                    book_dict[book] = details
                except UnboundLocalError:
                    pass
            
            
class UserInfoBackup:
    def __init__(self, user_dict):
        self.user_dict = dict()

    def user_backup(self, user_dict):
        with open('user_backup.txt', 'w') as file:
            for user, category in user_dict.items():
                file.write(f"{user}\n{category}\n")
    
    def get_users_from_file(self, user_dict):
        i = 0
        with open('user_backup.txt', 'r') as file:
            for line in file.readlines() :
                try:
                    if i % 2 == 0:
                        user = line.strip('\n')
                    elif i % 2 != 0:
                        detail = line.strip('\n')
                        details = eval(detail)
                    i += 1 
                    user_dict[user] = details
                except UnboundLocalError:
                    pass
            

class AuthorInfoBackup:
    def __init__(self, author_dict):
        self.author_dict = dict()
    
    def author_backup(self, author_dict):
        with open('author_backup.txt', 'w') as file:
            for author, category in author_dict.items():
                file.write(f"{author}\n{category}\n")

    def get_authors_from_file(self, author_dict):
        i = 0
        with open('author_backup.txt', 'r') as file:
            for line in file.readlines():
                try:
                    if i % 2 == 0:
                        author = line.strip('\n')
                    else:
                        detail = line.strip('\n')
                        details = eval(detail)
                    i += 1    
                    author_dict[author] = details
                except UnboundLocalError:
                    pass
            
                
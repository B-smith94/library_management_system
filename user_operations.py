import random
import string
import re

class UserOperations:
    def __init__(self, username, library_id):
        self.username = username
        self.__library_id = library_id
    
    def get_library_id(self):
        return self.__library_id
    
    def set_library_id (self, new_id):
        self.__library_id = new_id

    def add_new_user(self, username):
        library_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        create_id = UserOperations(username, library_id)
        create_id.set_library_id(library_id)
        stored_id = create_id.get_library_id()
        self[username] = {"Library ID": stored_id, "Checked Out Books": {}}
        print("New user added. Welcome to the Library!")
        print(f"Unique Library Identifier (Library ID)(Do NOT share with others): {library_id}")
    
    def view_user_details(self, username, library_id):
        print(f"Username: {username}")
        if self[username]["Library ID"] == library_id:
            for detail, info in self[username].items():
                print(f"   {detail}: {info}")
        else:
            print(f"Username: {username}")
            for detail, info in self[username].items():
                if detail == "Library ID":
                    print(f"   {detail}: REDACTED")
                else:
                    print(f"   {detail}: {info}")

    def display_users(self):
        for username, category in self.items():
            print(f"Username: {username}")
            for detail, info in category.items():
                if detail == "Library ID":
                    print(f"   {detail}: REDACTED")
                else:
                    print(f"   {detail}: {info}")

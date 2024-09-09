import re

class BookOperations:
    def __init__(self, book, author):    
        self = dict()
        self.book = book
        self.author = author
        
    def add_new_book(self, book, author, genre, pub_date):
        if book not in self:
            try:
                self[book] = {"Author": author, "Genre": genre, "Publication Date": pub_date, "Availability": "In Stock"} 
                print(f"\n{book} by {author} added to library stock.\n")
            except Exception as e:
                print(f"An error has occurred: {e}")
       
        else:
            print(f"\n{book} is already in the library.")

    def borrow_book(self, user_dict, book, username):
        if book not in self:
            print(f"{book} is not available in our library.")
        else:
            if self[book]["Availability"] == "In Stock":
                self[book]["Availability"] = "Out of Stock"
                if type(user_dict[username]["Checked Out Books"]) is not set: 
                    user_dict[username]["Checked Out Books"] = {book}
                elif type(user_dict[username]["Checked Out Books"]) is set:
                    user_dict[username]["Checked Out Books"].add(book)
                print("Here you go! Please return this book by the appropriate date if you want to avoid late fees.")
            else:
                print(f"I'm sorry, {book} is already out on loan.")

    def return_book(self, user_dict, book, username):
        if book not in self:
            print(f"{book} is not available in our library.")
        else:
            if self[book]["Availability"] == "Out of Stock":
                self[book]["Availability"] = "In Stock"
                if book in user_dict[username]["Checked Out Books"]:
                    user_dict[username]["Checked Out Books"].remove(book)
                    print(f"Thank you for returning {book} to our shelves!")
                else:
                    print(f"{book} is not in your list of checked-out materials. You must have returned it already!")
            else:
                print(f"{book} is already in stock.")

    def search_books(self, book):
        if book not in self:
            print(f"{book} is not available in our library.")
        
        else:
            print(f"Book: {book}")
            for detail, info in self[book].items():
                print(f"   {detail}: {info}")

    def display_books(self):
        for book, category in self.items():
            print(f"Book: {book}")
            for detail, info in category.items():
                print(f"   {detail}: {info}")
      

class AuthorOperations:
    def __init__(self, author):
        self.author = author

    def add_new_author(self, author, birthday, date_of_death):
        if author not in self:
            try:
                self[author] = {"Date of Birth": birthday, "Date of Death": date_of_death}
            except Exception as e:
                print(f"An error has occurred: {e}")
        
        else:
            print(f"{author} already exists in the database.")
    def view_author_details(self, author):
        if author not in self:
            print(f"I'm sorry, {author} does not exist in our database.")
        else:
            print(f"Author: {author}")
            for detail, info in self[author].items():
                print(f"   {detail}: {info}")

    def display_all_authors(self):
        for author, category in self.items():
            print(f"Author: {author}")
            for detail, info in category.items():
                print(f"   {detail}: {info}")
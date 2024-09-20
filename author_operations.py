import connect_mysql
from connect_mysql import connect_database

class AuthorOperations:
    def __init__(self, author):
        self.author = author

    def add_new_author(self, author, birthday, date_of_death):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                new_author = author, f"Birthday: {birthday}; Date of Death: {date_of_death}"
                query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"

                cursor.execute(query, new_author)
                conn.commit()

                print(f"{author} successfully added to the database!")
            except connect_mysql.Error as db_err:
                print(f"A Database Error has occurred: {db_err}")
            except Exception as e:
                print(f"An error has occurred: {e}")
            finally:
                cursor.close()
                conn.close()
        
        else:
            print(f"{author} already exists in the database.")
    def view_author_details(self, author):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                
                query = "SELECT * FROM authors WHERE name = %s"

                cursor.execute(query, author)

                for row in cursor.fetchall():
                    print(row)
            except connect_mysql.Error as db_err:
                print(f"A Database Error has occurred: {db_err}")
            except Exception as e:
                print(f"An error has occurred: {e}")
            finally:
                cursor.close()
                conn.close()

    def return_author_id(self, author):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                
                query = "SELECT id FROM authors WHERE name = %s"

                cursor.execute(query, author)

                for row in cursor.fetchall():
                    return row
            except connect_mysql.Error as db_err:
                print(f"A Database Error has occurred: {db_err}")
            except Exception as e:
                print(f"An error has occurred: {e}")
            finally:
                cursor.close()
                conn.close()

    def display_all_authors(self):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                
                query = "SELECT * FROM authors"

                cursor.execute(query)

                for row in cursor.fetchall():
                    print(row)
            except connect_mysql.Error as db_err:
                print(f"A Database Error has occurred: {db_err}")
            except Exception as e:
                print(f"An error has occurred: {e}")
            finally:
                cursor.close()
                conn.close()
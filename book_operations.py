import connect_mysql
from connect_mysql import connect_database

class BookOperations:
    def __init__(self, book, author):    
        self = dict()
        self.book = book
        self.author = author
        
    def add_new_book(title, author_id, isbn, publication_date):
        conn = connect_database()
        if conn is not None:    
            try:
                cursor = conn.cursor()
                new_book = title, author_id, isbn, publication_date
                query = "INSERT INTO Books (title, author_id, isbn, publication_date) Values (%s, %s, %s, %s)"

                cursor.execute(query, new_book)
                conn.commit()

                print("New book successfully added to databse!")
            except connect_mysql.Error as db_err:
                print(f"A Database Error has occurred: {db_err}")
            except Exception as e:
                print(f"An error has occurred: {e}")
            finally:
                cursor.close()
                conn.close()

    def borrow_book(user_id, book_id, borrow_date):
        conn = connect_database
        if conn is not None:
            try:
                cursor = conn.cursor()
                newly_borrowed = user_id, book_id, borrow_date
                query_1 = "INSERT INTO borrowed_books(user_id, book_id, borrow_date) VALUES (%s, %s, %s)"
                query_2 = f"UPDATE books SET availability = BOOLEAN 0 WHERE id = {book_id}"
                cursor.execute(query_1, newly_borrowed)
                cursor.execute(query_2)
                conn.commit()

            except connect_mysql.Error as db_err:
                print(f"A Database Error has occurred: {db_err}")
            except Exception as e:
                print(f"An error has occurred: {e}")
            finally:
                cursor.close()
                conn.close()

    def return_book(user_id, book_id, return_date):
        conn = connect_database
        if conn is not None:
            try:
                cursor = conn.cursor()
                returned_book = return_date, user_id, book_id
                query_1 = "UPDATE borrowed_books SET return_date = %s WHERE user_id = %s AND book_id = %s"
                query_2 = f"UPDATE books SET availability = BOOLEAN 1 WHERE id = {book_id}"
                cursor.execute(query_1, returned_book)
                cursor.execute(query_2)
                conn.commit()

            except connect_mysql.Error as db_err:
                print(f"A Database Error has occurred: {db_err}")
            except Exception as e:
                print(f"An error has occurred: {e}")
            finally:
                cursor.close()
                conn.close()

    def search_books(title):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                query = f"SELECT * FROM books WHERE title = {title}"
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

    def display_books():
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                query = f"SELECT * FROM books"

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
    
    def retrieve_book_id(self, title):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                query = f"SELECT id FROM books WHERE title = {title}"

                cursor.execute(query)

                for row in cursor.fetchall():
                    return row
            except connect_mysql.Error as db_err:
                print(f"A Database Error has occurred: {db_err}")
            except Exception as e:
                print(f"An error has occurred: {e}")
            finally:
                cursor.close()
                conn.close()
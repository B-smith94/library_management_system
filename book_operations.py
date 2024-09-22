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

                print("New book successfully added to database!")
            except connect_mysql.Error as db_err:
                print(f"A Database Error has occurred: {db_err}")
            except Exception as e:
                print(f"An error has occurred: {e}")
            finally:
                cursor.close()
                conn.close()

    def borrow_book(user_id, book_id, borrow_date):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                newly_borrowed = user_id, book_id, borrow_date
                book = (book_id, )
                query_1 = "INSERT INTO borrowed_books(user_id, book_id, borrow_date) VALUES (%s, %s, %s)"
                query_2 = "UPDATE books SET availability = 0 WHERE id = %s"
                cursor.execute(query_1, newly_borrowed)
                cursor.execute(query_2, book)
                conn.commit()
                print("Here is your book! Please remember to return it when you are done.")

            except connect_mysql.Error as db_err:
                print(f"A Database Error has occurred: {db_err}")
            except Exception as e:
                print(f"An error has occurred: {e}")
            finally:
                cursor.close()
                conn.close()

    def return_book(user_id, book_id, return_date):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                returned_book = return_date, user_id, book_id
                book = (book_id, )
                query_1 = "UPDATE borrowed_books SET return_date = %s WHERE user_id = %s AND book_id = %s"
                query_2 = "UPDATE books SET availability = 1 WHERE id = %s"
                cursor.execute(query_1, returned_book)
                cursor.execute(query_2, book)
                conn.commit()
                print("Thank you for returning your book to the Library!")

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
                book = (title, )
                query = "SELECT b.title, a.name, b.isbn, b.publication_date, b.availability FROM books b, authors a WHERE b.title = %s AND a.id = b.author_id"
                cursor.execute(query, book)

                for row in cursor.fetchall():
                    if row[4] == 1:
                        print(f"Title: {row[0]}\n\tAuthor: {row[1]}\n\tISBN: {row[2]}\n\tPublication Date: {row[3]}\n\tAvaiability: In Stock")
                    else:
                        print(f"Title: {row[0]}\n\tAuthor: {row[1]}\n\tISBN: {row[2]}\n\tPublication Date: {row[3]}\n\tAvaiability: Out Of Stock")
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
                query =  query = "SELECT b.title, a.name, b.isbn, b.publication_date, b.availability FROM books b, authors a WHERE a.id = b.author_id"

                cursor.execute(query)

                for row in cursor.fetchall():
                    if row[4] == 1:
                        print(f"Title: {row[0]}\n\tAuthor: {row[1]}\n\tISBN: {row[2]}\n\tPublication Date: {row[3]}\n\tAvaiability: In Stock")
                    else:
                        print(f"Title: {row[0]}\n\tAuthor: {row[1]}\n\tISBN: {row[2]}\n\tPublication Date: {row[3]}\n\tAvaiability: Out Of Stock")
            except connect_mysql.Error as db_err:
                print(f"A Database Error has occurred: {db_err}")
            except Exception as e:
                print(f"An error has occurred: {e}")
            finally:
                cursor.close()
                conn.close()
    
    def retrieve_book_id(title):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                book = (title, )
                query = "SELECT id FROM books WHERE title = %s"

                cursor.execute(query, book)

                for row in cursor.fetchall():
                    return str(row[0])
            except connect_mysql.Error as db_err:
                print(f"A Database Error has occurred: {db_err}")
            except Exception as e:
                print(f"An error has occurred: {e}")
            finally:
                cursor.close()
                conn.close()
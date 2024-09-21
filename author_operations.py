import connect_mysql
from connect_mysql import connect_database

class AuthorOperations:
    def __init__(self, author):
        self.author = author

    def add_new_author(author, birthday, date_of_death):
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

    def view_author_details(author):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                author_name = (author, )
                query = "SELECT * FROM authors WHERE name = %s"

                cursor.execute(query, author_name)

                for row in cursor.fetchall():
                    print(f"Author: {row[1]}\n   {row[2]}")
            except connect_mysql.Error as db_err:
                print(f"A Database Error has occurred: {db_err}")
            except Exception as e:
                print(f"An error has occurred: {e}")
            finally:
                cursor.close()
                conn.close()

    def display_all_authors():
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                query = "SELECT * FROM authors"

                cursor.execute(query)

                for row in cursor.fetchall():
                    print(f"Author: {row[1]}\n   {row[2]}")
            except connect_mysql.Error as db_err:
                print(f"A Database Error has occurred: {db_err}")
            except Exception as e:
                print(f"An error has occurred: {e}")
            finally:
                cursor.close()
                conn.close()

    def retrieve_author_id(author):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                author_name = (author, )
                query = "SELECT id FROM authors WHERE name = %s"
                cursor.execute(query, author_name)

                for row in cursor.fetchall():
                    return str(row[0])
            except connect_mysql.Error as db_err:
                print(f"A Database Error has occurred: {db_err}")
            except Exception as e:
                print(f"An error has occurred: {e}")
            finally:
                cursor.close()
                conn.close()

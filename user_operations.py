import random
import string
import re
import connect_mysql
from connect_mysql import connect_database
class UserOperations:
    def __init__(self, name, library_id):
        self.name = name
        self.__library_id = library_id
    
    def get_library_id(self):
        return self.__library_id
    
    def set_library_id (self, new_id):
        self.__library_id = new_id

    def add_new_user(name):
        library_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        create_id = UserOperations(name, library_id)
        create_id.set_library_id(library_id)
        stored_id = create_id.get_library_id()
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                new_user = name, stored_id
                user_name = (name, )
                query_1 = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
                query_2 = "SELECT library_id FROM users WHERE name = %s"
                
                cursor.execute(query_1, new_user)
                conn.commit()
                
                cursor.execute(query_2, user_name)
                
                print(f"{name} successfully added to the database!")
                for row in cursor.fetchall():
                    print(f"Your Library ID is {row}. Do NOT share this with anyone!")
            except connect_mysql.Error as db_err:
                print(f"A Database Error has occurred: {db_err}")
            except Exception as e:
                print(f"An error has occurred: {e}")
            finally:
                cursor.close()
                conn.close()        
    
    def view_user_details(name):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                user_name = (name, )
                query = "SELECT * FROM users WHERE name = %s"
                cursor.execute(query, user_name)

                for row in cursor.fetchall():
                    print(f"\nName: {row[1]}\nLibrary ID: {row[2]}")

            except connect_mysql.Error as db_err:
                print(f"A Database Error has occurred: {db_err}")
            except Exception as e:
                print(f"An error has occurred: {e}")
            finally:
                cursor.close()
                conn.close()

    def display_users():
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                query = "SELECT id, name FROM users"
                cursor.execute(query)

                for row in cursor.fetchall():
                    print(row)
            except connect_mysql.Error as db_err:
                print(f"A Database Error has occurred: {db_err}")
            except Exception as e:
                print(row)
            finally:
                cursor.close()
                conn.close()

    def retrieve_user_id(name):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                user_name = (name, )
                query = "SELECT id FROM users WHERE name = %s"
                cursor.execute(query, user_name)
                
                for row in cursor.fetchall():
                    return str(row[0])
            except connect_mysql.Error as db_err:
                print(f"A Database Error has occurred: {db_err}")
            except Exception as e:
                print(f"An error has occurred: {e}")
            finally:
                cursor.close()
                conn.close()

    def verify_library_id(name, library_id):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                user_name = (name, )
                query = "SELECT library_id FROM users WHERE name = %s"

                cursor.execute(query, user_name)

                for row in cursor.fetchall():
                    set_id = UserOperations(name, library_id)
                    set_id.set_library_id(library_id)
                    fetched_id = set_id.get_library_id()
                    if fetched_id in row:
                        print("ID Verified!")
                        return True
                    else:
                        return False
            except connect_mysql.Error as db_err:
                print(f"A Database Error has occurred: {db_err}")
            except Exception as e:
                print(f"An error has occurred: {e}")
            finally:
                cursor.close()
                conn.close()
        
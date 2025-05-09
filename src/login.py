from sqlite3 import Error
import sqlite3
from .db import get_database_connection
from .password import hash_password

def verify_user(email, password):
    # Database connection
    conn = get_database_connection()
    if conn is None:
        return False  # Unable to connect to the database

    cursor = conn.cursor()

    try:
        # Query to fetch the hashed password for the given email
        cursor.execute("SELECT password FROM users WHERE email = ?", (email,))
        result = cursor.fetchone()

        if result:
            stored_hashed_password = result["password"]

            # Verify the provided password with the stored hashed password
            hashed_input_password = hash_password(password)
            return hashed_input_password == stored_hashed_password
        else:
            return False  # Email not found
    except Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        cursor.close()
        conn.close()
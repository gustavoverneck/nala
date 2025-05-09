import os
import sqlite3
from .user import User
from .password import hash_password

# Database file path
DB_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'empresa.db')

def get_database_connection():
    """Get a connection to the SQLite database"""
    try:
        # Connect to SQLite file (will create if it doesn't exist)
        connection = sqlite3.connect(DB_FILE)
        
        # Configure SQLite to return rows as dictionaries
        connection.row_factory = sqlite3.Row
        
        print(f"Database connection established to SQLite file: {DB_FILE}")
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to the SQLite database: {e}")
        return None

def initialize_database():
    """Initialize the database with tables if they don't exist"""
    connection = get_database_connection()
    if connection:
        try:
            cursor = connection.cursor()
            
            # Create users table
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            )
            ''')
            
            # Add more tables as needed
            
            connection.commit()
            print("Database initialized successfully")
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
        finally:
            connection.close()


def add_user_to_user_table(user: User):
    """Add a user to the users table"""
    connection = get_database_connection()
    if connection:
        try:
            cursor = connection.cursor()
            
            # Insert user into the users table
            cursor.execute('''
            INSERT INTO users (name, email, password, role)
            VALUES (?, ?, ?, ?)
            ''', (user.name, user.email, hash_password(user.password), user.role))
            
            connection.commit()
            print(f"User {user.name} added successfully")
        except sqlite3.Error as e:
            print(f"Error adding user to the database: {e}")
        finally:
            connection.close()
    else:
        print("Connection not established.")


def get_user_by_email(email: str) -> User:
    """Get a user by email"""
    connection = get_database_connection()
    if connection:
        try:
            cursor = connection.cursor()
            
            # Query the user by email
            cursor.execute('''
            SELECT * FROM users WHERE email = ?
            ''', (email,))
            
            row = cursor.fetchone()
            if row:
                return User(
                    id=row['id'],
                    name=row['name'],
                    email=row['email'],
                    password=row['password'],
                    role=row['role']
                )
        except sqlite3.Error as e:
            print(f"Error fetching user from the database: {e}")
        finally:
            connection.close()
    return None
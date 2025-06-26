import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (adjust host, user, and password if needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password_here'  # Replace with your actual MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Use CREATE DATABASE IF NOT EXISTS to avoid failure if it already exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    
    finally:
        # Close connections safely
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()


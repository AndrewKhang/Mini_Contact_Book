import mysql.connector

try:
 db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",      # Default for XAMPP is empty
        database="contacts_db"
    )    
 if db_connection.is_connected():
        cursor = db_connection.cursor()
        
        # Tạo bảng ở đây
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                name VARCHAR(100),
                phone VARCHAR(15)
            )
        """)
        db_connection.commit()
        print("Table created!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'db_connection' in locals() and db_connection.is_connected():
        cursor.close()
        db_connection.close()
        print("Connection closed.")
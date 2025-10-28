import mysql.connector
from mysql.connector import Error

# Replace these with your MySQL credentials
HOST = "localhost"
USER = "radhaKrishn"
PASSWORD = "MyPass123"  # Use the password you set
DATABASE = "ash"

try:
    # Connect to MySQL
    conn = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    if conn.is_connected():
        print("Successfully connected to MySQL database")

        cursor = conn.cursor()

        # 1️⃣ Create table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50),
            email VARCHAR(50)
        )
        """)
        print("Table 'users' is ready.")

        # 2️⃣ Insert sample data
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("Akash", "akash@example.com"))
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("Radha", "radha@example.com"))
        conn.commit()
        print("Sample data inserted successfully.")

        # 3️⃣ Fetch and display data
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        print("\nData in 'users' table:")
        for row in rows:
            print(row)

except Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("\nMySQL connection is closed")

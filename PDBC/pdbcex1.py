# MySQLAlterTableWithAdd.py
import mysql.connector as mysql
from mysql.connector import Error

def table_alter_with_add():
    try:
        # Step 1: Connect to MySQL
        con = mysql.connect(
            host="localhost",
            user="radhaKrishn",
            password="MyPass123",
            database="ash"
        )
        cur = con.cursor()

        # Step 2: Alter table to add a new column
        alter_query = "ALTER TABLE employees ADD COLUMN cname VARCHAR(10) NOT NULL"
        cur.execute(alter_query)

        print("Table altered successfully")

    except Error as e:
        print("Problem in MySQL:", e)

    finally:
        if 'con' in locals() and con.is_connected():
            cur.close()
            con.close()

# main program
table_alter_with_add()

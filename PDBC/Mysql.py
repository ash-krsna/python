#MySQLCursorTestEx.py
import mysql.connector as mc
try:
    conobj=mc.connect(host="127.0.0.1",
                      user="radhaKrishn",
                      passwd="MyPass123")
    print("Python Program got Connection from MySQL")
    curobj=conobj.cursor()
    print("Python Program Created Cursor Object")
except mc.DatabaseError as db:
    print("Problem in MySQL:", db)
#progra for Creating Data base--'batch11am'
#MySQLDatabaseCreateEx.py
import mysql.connector as mc # Step-1
def databasecreate():
    try:
        conobj=mc.connect(host="127.0.0.1",
                          user="radhaKrishn",
                          passwd="MyPass123") #Step-2
        curobj=conobj.cursor() #Step-3
        #step-4
        dcq="create database HYD"
        curobj.execute(dcq)
        print("Database Created Sucessfully in MySQL-verify")
    except mc.DatabaseError as db:
        print("Problem in MySQL:", db)
#main program
databasecreate()
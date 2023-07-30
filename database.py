# Import module
import sqlite3

def insertLink(name,link,time):
    # Connecting to sqlite
    conn = sqlite3.connect('links.db')

    # Creating a cursor object using the
    # cursor() method
    cursor = conn.cursor()

    # # Creating table
    # table ="""CREATE TABLE LINK(NAME VARCHAR(255), LINK VARCHAR(255),
    # TIME VARCHAR(255));"""
    # cursor.execute(table)

    # Queries to INSERT records.
    cursor.execute('''INSERT INTO LINK VALUES (?,?,?)''',(name,link,time))

    # Closing the connection
    conn.close()

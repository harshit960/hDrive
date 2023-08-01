# Import module
import sqlite3

def create_conn():
    conn = sqlite3.connect('links.db')
    return conn

def insertLink(conn,name,link,time):
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO LINK VALUES (?,?,?)''',(name,link,time))
    conn.commit()

def getLink(conn):
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM LINK''')
    d=cursor.fetchall()
    return [i for i in d]  

def delLink(conn):  
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM LINK''')
    conn.commit()
    
def closeConn(conn):
    conn.close()

def getData(conn):
    conn.close()
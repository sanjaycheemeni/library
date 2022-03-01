import sqlite3 as sql
from warnings import catch_warnings
from winreg import QueryInfoKey



class LibraryDatabase:
  

    def __init__(self,db):
        self.con = sql.connect('lib.db')
        self.cur = self.con.cursor()

    def login(self,user,passw):
        query = f"SELECT * FROM users WHERE uname = '{user}' and pass = '{passw}'"
        self.cur.execute(query)
        if self.cur.fetchone():
           return True
        else:
            False
    def addbook(self,id,name,author,price,stock):
        query = f"INSERT INTO books VALUES('{id}','{name}','{author}','{price}','{stock}')"
        try:
            self.cur.execute(query)
            self.con.commit()
            print('DONE!!')

        except sql.Error as error:
            print("Failed to insert data into sqlite table", error)
    
    def delbook(self,id):
        query = f"SELECT * FROM books WHERE id='{id}'"
        self.cur.execute(query)
        rows = self.cur.fetchall()

        for row in rows:
            print(row)

        query = f"DELETE FROM books WHERE id={id}"
        try:
            self.cur.execute(query)
            self.con.commit()
            print('deleted !!')
            self.cur.close()

        except sql.Error as error:
            print("Failed to delete data from sqlite table", error)

lb = LibraryDatabase('sql.db')
#lb.addbook('001','kayar','Thakayi sp','200','12')
lb.delbook('001')


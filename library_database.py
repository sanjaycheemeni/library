from lib2to3.pgen2.pgen import DFAState
import re
import sqlite3 as sql
from tkinter import N
from typing import List
from warnings import catch_warnings
from winreg import QueryInfoKey



class LibraryDatabase:
  

    def __init__(self,db):
        self.con = sql.connect('lib.db')
        

    def login(self,user,passw):
        self.cur = self.con.cursor()
        query = f"SELECT * FROM users WHERE uname = '{user}' and pass = '{passw}'"
        self.cur.execute(query)
        if self.cur.fetchone():
           return True
        else:
            False
    def addbook(self,id,name,author,stock):
        self.cur = self.con.cursor()
        query = f"SELECT * FROM books WHERE id='{id}'"
        print(query)
        self.cur.execute(query)
        if self.cur.fetchone():
           return False


        self.cur = self.con.cursor()
        query = f"INSERT INTO books(name,author,stock) VALUES('{name}','{author}','{stock}')"
        try:
            self.cur.execute(query)
            self.con.commit()
            return True

        except sql.Error as error:
            print("Failed to insert data into sqlite table", error)
            return False
    
    def delbook(self,id):
        self.cur = self.con.cursor()
        query = f"SELECT * FROM books WHERE id='{id}'"
        self.cur.execute(query)
        rows = self.cur.fetchall()

        for row in rows:
            print(row)

        query = f"DELETE FROM books WHERE id='{id}'"
        try:
            self.cur.execute(query)
            self.con.commit()
            print('deleted !!')
            self.cur.close()
            return True

        except sql.Error as error:
            print("Failed to delete data from sqlite table", error)
            return False
    def bookList(self):
        self.cur = self.con.cursor()
        query = f"SELECT * FROM books"
        self.cur.execute(query)
        rows = self.cur.fetchall()
        lis = []
        for row in rows:
            lis.append(row[1])
        return lis

    def searchBook(self,name):
        self.cur = self.con.cursor()
        query = f"SELECT * FROM books where name like '{name}%' or name like '%{name}%'"
        self.cur.execute(query)
        rows = self.cur.fetchall()
        lis = []
        for row in rows:
            lis.append(f"{row[0]}  {row[1]}")
        return lis
    
    def getbook(self,id):
        self.cur = self.con.cursor()
        query = f"SELECT * FROM books where id='{id}'"
        self.cur.execute(query)
        rows = self.cur.fetchall()
        #print(type(rows))
        return rows

    def updateBook(self,id,name,auth,stock):
        query = f"UPDATE books SET name='{name}',author='{auth}',stock='{stock}' where id = '{id}'"
        self.cur = self.con.cursor()
        try:
            self.cur.execute(query)
            self.con.commit()
            print('deleted !!')
            self.cur.close()
            return True

        except sql.Error as error:
            print("Failed to update data on sqlite table : ", error)
            return False

            

#lb = LibraryDatabase('sql.db')
# lb.addbook('001','kayar','Thakayi sp','200','12')
# lb.addbook('002','naalukettu','onv kurup','180','5')
#lb.delbook('001')
#print(lb.searchBook('k'))


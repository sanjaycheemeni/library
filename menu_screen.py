
from cmath import log
from re import T
from tkinter import *
from turtle import home

from mysqlx import Column
from library_database import LibraryDatabase

l = LibraryDatabase('lib.db')
global lis
lis = l.searchBook('')
def callback(var):
    lis = l.searchBook(var.get())

global home_screen
home_screen = Tk()
home_screen.configure(background="#2d2e2d")
home_screen.title("LIBRARY MANAGER")
home_screen.geometry("600x300")

global search_key
search_key = StringVar()
search_key.trace("w", lambda name, index,mode, var=search_key: callback(var))
label = Label(home_screen,width="300", text='HOME')
label.pack()



search_t = Label(home_screen, text="Search ",bg="#2d2e2d",fg="white")
search_t.config(font=("Product Sans", 10))
search_t.place(x=8,y=25)
Entry(home_screen, textvariable=search_key,bg="white").place(x=63,y=25)



#list of search by $search_key
lisb = Listbox(home_screen,listvariable=lis,width=30,height=10,selectmode='extended')
lisb.place(x=8,y=50)


home_screen.mainloop()


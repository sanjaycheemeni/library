
from cmath import log
from re import T
import re
from signal import valid_signals
from tkinter import *
from tkinter import messagebox
from turtle import home

#from mysqlx import Column
from library_database import LibraryDatabase

#########################################
l = LibraryDatabase('lib.db')
#global home_screen
home_screen = Tk()

bid = StringVar()
bid.set("ID:")
bname = StringVar()
bstock = StringVar()
bauth = StringVar()


######################################## event area
def runHome():
    #home_screen.mainloop()
    pass


def callback(var):
   vlist.set(l.searchBook(var.get()))
   

def clearFields():
    bid.set("ID:")
    bname.set("")
    bauth.set("")
    bstock.set("")

def onSelect(event):
    selection = event.widget.curselection()
    val =str(event.widget.get(selection[0]))
    val = val.split()[0]
    var = l.getbook(val)[0]
    bid.set(f"ID:{var[0]}")
    bname.set(var[1])
    bauth.set(var[2])
    bstock.set(var[3])
    #print(type(bid.get()))

def updateBook():
    if l.updateBook(bid.get(),bname.get(),bauth.get(),bstock.get()) :
        messagebox.showinfo("UPDATE BOOK", "Book details updates!")
        vlist.set(l.searchBook(''))
    else:
        messagebox.showerror("Cant update","something went wrong!")

def deleteBook():
    if l.delbook(bid.get().replace('ID:','')):
        messagebox.showinfo("DELETE BOOK", "Book details deleted succesfuly!")
        vlist.set(l.searchBook(''))
    else:
        messagebox.showerror("Cant delete","something went wrong!") 
def addBook():
    #print(bid.get().replace('ID:',''))
    if(bname.get().strip()=='' or bauth.get().strip()=='' or bstock.get().strip()==''):
        messagebox.showwarning("Cant Add","Fill all required fields")
        return

    if l.addbook(bid.get().replace('ID:',''),bname.get(),bauth.get(),bstock.get()):
        messagebox.showinfo("ADD BOOK", "Book Details Added!")
        clearFields()
        vlist.set(l.searchBook(''))
    else:
        messagebox.showerror("Cant add","something went wrong!") 
    
    
    

########################################
home_screen.configure(background="#2d2e2d")
home_screen.title("LIBRARY MANAGER")
home_screen.geometry("600x300")

global search_key
global vlist
search_key = StringVar()
vlist = StringVar(value=l.searchBook(search_key.get()))
search_key.trace("w", lambda name, index,mode, var=search_key: callback(var))

#=== [ view start ] ==========================================================================

# === TITLE ===
label = Label(home_screen,width="300", text='HOME')
label.pack()

# === SEARCH BAR ===
search_t = Label(home_screen, text="Search ",bg="#2d2e2d",fg="white")
search_t.config(font=("Product Sans", 10))
search_t.place(x=8,y=25)
Entry(home_screen, textvariable=search_key,bg="white").place(x=63,y=25)

# ===LISTBOX ===
lisb = Listbox(home_screen,listvariable=vlist,width=30,height=10,selectmode='extended')
lisb.place(x=8,y=50)
lisb.bind("<<ListboxSelect>>", onSelect)

# === FORM ===
b_id_t = Label(home_screen, text="Book ID ",textvariable=bid,bg="#2d2e2d",fg="yellow")
b_id_t.place(x=300,y=40)

#book name
b_name_t = Label(home_screen, text="Book name",bg="#2d2e2d",fg="white")
b_name_t.place(x=300,y=65)
Entry(home_screen,bg="white",textvariable=bname).place(x=300,y=85)

#author name
b_auth_t = Label(home_screen, text="Author name",bg="#2d2e2d",fg="white")
b_auth_t.place(x=300,y=105)
Entry(home_screen,bg="white",textvariable=bauth).place(x=300,y=125)

#stock
b_stock_t = Label(home_screen, text="Stock count",bg="#2d2e2d",fg="white")
b_stock_t.place(x=300,y=145)
Entry(home_screen,bg="white",textvariable=bstock).place(x=300,y=165)

#buttonset [ update delete add clear ]
Button(home_screen, text="Update", width=10, height=1, bg="#7188f0",fg="black",command=updateBook).place(x=450,y=80)
Button(home_screen, text="Delete", width=10, height=1, bg="#e64e4e",fg="black",command=deleteBook).place(x=450,y=110)
Button(home_screen, text="Add", width=10, height=1, bg="#64d959",fg="black",command=addBook).place(x=450,y=160)
Button(home_screen, text="Clear", width=8, height=1, bg="white",fg="red",command=clearFields).place(x=215,y=130)

# ==== VIEW END =====================================================================




home_screen.mainloop()
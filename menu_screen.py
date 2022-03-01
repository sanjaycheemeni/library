
from cmath import log
from re import T
from signal import valid_signals
from tkinter import *
from tkinter import messagebox
from turtle import home

from mysqlx import Column
from library_database import LibraryDatabase

#########################################
l = LibraryDatabase('lib.db')
global home_screen
home_screen = Tk()

bid = StringVar()
bid.set("Book ID")
bname = StringVar()
bstock = StringVar()
bauth = StringVar()


######################################## event area
def runHome():
    home_screen.mainloop()


def callback(var):
   vlist.set(l.searchBook(var.get()))
   

def editDetails():
    pass

def onSelect(event):
    selection = event.widget.curselection()
    val =str(event.widget.get(selection[0]))
    val = val.split()[0]
    var = l.getbook(val)[0]
    bid.set(f"Book ID {var[0]}")
    bname.set(var[1])
    bauth.set(var[2])
    bstock.set(var[4])
    #print(type(bid.get()))

def updateBook():
    if l.updateBook(bid.get(),bname.get(),bauth.get(),bstock.get()) :
        messagebox.showinfo("UPDATE BOOK", "Book details updates!")
        bid.set("Book ID")
        bname.set("")
        bauth.set("")
        bstock.set("")
    else:
        messagebox.showerror("Cant update","something went wrong!")

def deleteBook():
    messagebox.showinfo("DELETE BOOK", "Book deleted succesfuly!")
    
    
    

########################################
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

global vlist
vlist = StringVar(value=l.searchBook(search_key.get()))
print(search_key.get())

#list of search by $search_key  ####LISTBOX
lisb = Listbox(home_screen,listvariable=vlist,width=30,height=10,selectmode='extended')
lisb.place(x=8,y=50)
lisb.bind("<<ListboxSelect>>", onSelect)


# editable form
b_id_t = Label(home_screen, text="Book ID ",textvariable=bid,bg="#2d2e2d",fg="white")
b_id_t.place(x=300,y=40)


b_name_t = Label(home_screen, text="Book name",bg="#2d2e2d",fg="white")
b_name_t.place(x=300,y=65)
Entry(home_screen,bg="white",textvariable=bname).place(x=300,y=85)

b_auth_t = Label(home_screen, text="Author name",bg="#2d2e2d",fg="white")
b_auth_t.place(x=300,y=105)
Entry(home_screen,bg="white",textvariable=bauth).place(x=300,y=125)

b_stock_t = Label(home_screen, text="Stock count",bg="#2d2e2d",fg="white")
b_stock_t.place(x=300,y=145)
Entry(home_screen,bg="white",textvariable=bstock).place(x=300,y=165)

###
#button
Button(home_screen, text="Update", width=10, height=1, bg="white",fg="black",command=updateBook).place(x=450,y=40)

Button(home_screen, text="Delete", width=10, height=1, bg="white",fg="black",command=deleteBook).place(x=450,y=80)


#########################################
runHome()


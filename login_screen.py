
from imp import load_source
from re import T
from runpy import run_path
from tkinter import *

from mysqlx import Column
from library_database import LibraryDatabase
from menu_screen import runHome

def runLogin():
    login_screen.mainloop()
    


global login_screen
login_screen = Tk()



def loginSucces():
    pass
    



#defining login function
def login():

    lib = LibraryDatabase('lib.db')
    #getting form data
    uname=username.get()
    pwd=password.get()
    #applying empty validation
    if uname=='' or pwd=='':
        message.set("fill the empty field!!!")
    else:
        if lib.login(uname,pwd):
            message.set("success!!")
            loginSucces()
        else:
             message.set("Wrong username or password!!!")


# def homescreen():
#     login_screen.destroy()
#     home = Tk()
#     home.configure(background="blue")
#     home.geometry('400x400')
#     home.mainloop()



##### LOGIN SCREEN #######

login_screen.configure(background="#2d2e2d")
login_screen.title("LIBRARY MANAGER")
login_screen.geometry("600x300")

global  message
global username
global password
username = StringVar()
password = StringVar()
message=StringVar()
label = Label(login_screen,width="300", text='LOGIN')
label.pack()
label.config(font=("Product Sans", 30))
label.config(fg="white")
label.config(bg="#1b1c1c")

#username
t_uname = Label(login_screen, text="USERNAME",bg="#2d2e2d",fg="white")
t_uname.config(font=("Product Sans", 10))
t_uname.place(x=150,y=150)
Entry(login_screen, textvariable=username,bg="white").place(x=240,y=152)
#password
t_pass = Label(login_screen, text="PASSWORD",bg="#2d2e2d",fg="white")
t_pass.config(font=("Product Sans",10))
t_pass.place(x=150,y=180)
Entry(login_screen, textvariable=password ,show=".",bg="white").place(x=240,y=182)
#message
Label(login_screen, text="",textvariable=message,bg="#2d2e2d",fg="red").place(x=150,y=210)
Button(login_screen, text="LOGIN",font=("Product Sans",12), width=10, height=1, bg="white",fg="black",command=login).place(x=210,y=235)

###########################
runLogin()
#database connection file
import mysql.connector

class Library:

    #initilise database
    def __init__(self,user,password,host,database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database


    #login returns wha
    def signin(self,username,password):
        # if(username.strip() ==''or password.strip()==''):
        #     #mb.showwarning('Fields cant be empty!!')
        #     print('Fields cant be empty!!')
        #     return False

        db = mysql.connector.connect(host=self.host,user=self.user,password=self.password,database=self.database)
        mycursor = db.cursor()
        try:
            query = f"SELECT * FROM login WHERE login.username='{username}' AND login.password='{password}'"
            #print(query)
            mycursor.execute(query)
            rec =mycursor.fetchall()
            if(len(rec) > 0):
                print('LOGIN SUCCESS')
                return True
            else :
                print('LOGIN FAILED')
                return False
        except Exception as e:
            print(e)
            mb.showerror(f'LOGIN ERROR : {e}')
            return False

    #register new book
    def add_book(self,book_id,name,author,type,stock,publisher):
        db = mysql.connector.connect(host=self.host,user=self.user,password=self.password,database=self.database)
        mycursor = db.cursor()
        try:
            query = f"INSERT INTO BOOK VALUES('{book_id}','{name}','{author}','{type}','{stock}','{publisher}')"
            print(query)
            mycursor.execute(query)
            db.commit()
            print(' new book details added successfuly..!! ')

        except Exception as e:
            print(e)
            mb.showerror(f'DATABASE ERROR : {e}')
            return False



import sqlite3
from os import mkdir
import pandas as pd
import tkinter.messagebox as msg

class StudentDB():
    '''
    Database Functions
    '''
    def __init__(self):
        '''
        Create Database if not exists
        '''
        
        try:
            self.con = sqlite3.connect('Student.db')
        except sqlite3.OperationalError:
            mkdir('Student.db')
        finally:
            self.con = sqlite3.connect('Student.db')
         
        #### Create Table is not exists  #####    
        self.con.execute("CREATE TABLE IF NOT EXISTS student(id integer PRIMARY KEY, password text, studentId text, FirstName text, LastName text,email text, age int, address text, phoneNumber text, year integer, status text,  UNIQUE(studentId))")
        
        self.add_admin()
                
    def login_confirmation(email,password) -> bool:
        '''
        Login Confirmation. Matches email with password in the database
        :param email: results from email provided in login form
        :param password: results from password provided in login form
        :return: return string('email') if email not found and string('password') if password not found
        '''
        con = sqlite3.connect('Student.db')
        cursor = con.cursor()
        try:
            cursor.execute("SELECT password FROM student WHERE email LIKE ?" ,(email,))
            results=cursor.fetchall()
            if results[0][0] == password:
                return True
            else:
                return False
        except:
            return False
        
    def add_admin(self) -> None:
        '''
        Adds the admin user to the database on creation if not exists
        '''
        con = sqlite3.connect('Student.db')
        try:
            ######## Create admin user #############
            admin = ['test','00000','admin','admin','admin@unomaha.edu',0,'admin','admin',0,'admin']
            con.execute('INSERT OR IGNORE INTO student VALUES (NULL, ?,?,?,?,?,?,?,?,?,?)', admin )
            con.commit()
            con.close()
        except:
            pass
                   
    def addNew(data) -> None:
        '''
        Adds new data into the database
        :param data: list of values to add to database
        '''
        con = sqlite3.connect('Student.db')
        try: 
            con.execute('INSERT INTO student VALUES (NULL, ?,?,?,?,?,?,?,?,?,?)', data)
            con.commit()
            con.close()
        except:
            pass
        
    def find_duplicates(data) -> bool:
        '''
        Looks in database to find duplicates from data provided in params
        :param data:  string from entry fields
        :return: returns True if found and False if not found
        '''
        con = sqlite3.connect('Student.db')
        cursor = con.cursor()
        try:
            cursor.execute("SELECT studentId FROM student WHERE studentId LIKE ?",(data,))
            id = cursor.fetchall()
            if id[0][0] == data:
                return True
        except:
            pass
        try:
            cursor.execute("SELECT email FROM student WHERE email LIKE ?",(data,))
            email=cursor.fetchall()
            if email[0][0] == data:
                return True
        except:
            pass
        return False
            
    def update(id,studentId,password,FirstName,LastName,email, age, address, phoneNumber, year, status) -> None:
        '''
        Updates data already in the database
              exception handling for empty fields
        :params: all variables are databse fields
        '''
        
        con = sqlite3.connect('Student.db')
        if studentId != "":
            con.execute("UPDATE student SET studentId=? WHERE id=?" , (studentId,id))
        if password != "":
            con.execute("UPDATE student SET password=? WHERE id=?",(password,id))
        if FirstName != "":
            con.execute("UPDATE student SET FirstName=? WHERE id=?" , (FirstName,id))
        if LastName != "":
            con.execute("UPDATE student SET LastName=? WHERE id=?" , (LastName,id))
        if email != "":
            con.execute("UPDATE student SET email=? WHERE id=?" , (email,id))
        if age != "":
            con.execute("UPDATE student SET age=? WHERE id=?" , (age,id))
        if address != "":
            con.execute("UPDATE student SET address=? WHERE id=?" , (address,id))
        if phoneNumber != "":
            con.execute("UPDATE student SET phoneNumber=? WHERE id=?" , (phoneNumber,id))
        if year != "":
            con.execute("UPDATE student SET year=? WHERE id=?" , (year,id))
        if status != "":
            con.execute("UPDATE student SET status=? WHERE id=?" , (status,id))
               
        con.commit()
        con.close()
    
    def displayDB() -> list:
        '''
        Sqlite3 query to get all rows in a database
        :return: returns a list of rows from the database
        '''
        con = sqlite3.connect('Student.db')
        cursor = con.cursor()
        cursor.execute('SELECT id,studentId,FirstName,LastName,email FROM Student')
        rows = cursor.fetchall()
        con.close()
        return rows
    
    def searchId(event, studentSearch) -> list:
        '''
        Function that takes id from listbox selection and returns database results
        :param studentSearch: id number from listbox selection
        :return: Returns list of database results
        '''
        con = sqlite3.connect('Student.db')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM student WHERE id like ?", (studentSearch,))
        rows = cursor.fetchall()
        con.close()
        return rows
                       
    def searchdb(event,mystring) -> list:
        '''
        Uses key strokes to find all info from databse that matches the parameter.
        :param mystring: string value to search in the database
        :return: returns a list of results from database search
        '''    
        con = sqlite3.connect('Student.db')
        cursor = con.cursor()
        cursor.execute("SELECT id,studentId,FirstName,LastName,email FROM student WHERE studentId LIKE '%" + mystring + "%' OR FirstName LIKE '%" + mystring + "%' OR LastName LIKE '%" + mystring + "%' OR email LIKE '%" + mystring + "%'")
        rows=cursor.fetchall()
        con.close()
        return rows    

    def delete_data(selection) -> None:
        '''
        Delete record from database using an index value
        :param selection: index value 
        '''
        con = sqlite3.connect('Student.db')
        cursor = con.cursor()
        cursor.execute("DELETE FROM student WHERE id=?", selection)
        con.commit()
        con.close()
        
    def export() -> bool:
        '''
        Exports data from database to a csv file
        :return: returns True if exported and False if not exported
        '''
        try:
            con = sqlite3.connect('Student.db', isolation_level=None, detect_types=sqlite3.PARSE_COLNAMES)
            db_df = pd.read_sql_query("SELECT * From student", con)
            db_df.to_csv('students.csv', index=False)
            return True
        except:
            return False
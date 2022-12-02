from tkinter import *
import tkinter.messagebox as msg
from studentDB import *
import sys


class Login(Toplevel):
    '''
    Login Prompt
    
    '''
    def __init__(self):
        super().__init__()

        self.title("Student Login")
        # self.geometry('400x400')
        self.resizable(False, False)
        self.config(bg='light blue')

        self.email = StringVar()
        self.password = StringVar()

        mainFrame = Frame(self, bg='light blue', padx=10, pady=10, bd=5, relief=RIDGE)
        mainFrame.grid()

        main_inside_Frame = LabelFrame(mainFrame, width='375', height='350', bd=2, relief=RIDGE, text="Student Login\n", font=('calibri', 15, 'bold'), bg='white', padx=2, pady=2)
        main_inside_Frame.pack(side=TOP, fill=BOTH, expand=True)

        self.email_label = Label(main_inside_Frame, font=('calibri', 15, 'bold'), text='Email: ', bg='white', padx=2, pady=2)
        self.email_label.grid(row=0, column=0, sticky=W)
        self.entry_email = Entry(main_inside_Frame, font=('calibri', 15, 'bold'), textvariable=self.email, width=25)
        self.entry_email.grid(row=0, column=1)
        self.entry_email.focus()

        self.password_label = Label(main_inside_Frame, font=('calibri', 15, 'bold'), text='Password: ', bg='white', padx=2, pady=2)
        self.password_label.grid(row=1, column=0, sticky=W)
        self.entry_password = Entry(main_inside_Frame, font=('calibri', 15, 'bold'), textvariable=self.password, show="*", width=25)
        self.entry_password.grid(row=1, column=1)

        button_frame = Frame(mainFrame, width='375', height='50', bg='light blue', padx=18, pady=10)
        button_frame.pack(side=BOTTOM, fill=BOTH, expand=True)

        self.submit_button = Button(button_frame, command=self.login_results, text="Submit", font=('calibri', 15, 'bold'), padx=5, pady=5)
        self.submit_button.pack()

    def login_results(self) -> None:
        '''
        Uses StudentDB class to confirm email and password match the info in the database
             exception handling for empty fields and incorrect email/password
        '''
        if self.email.get() != "" and self.password.get() != "":
            if (StudentDB.login_confirmation(self.email.get(), self.password.get()) == False):
                msg.showerror("Incorrect email/password                 ")
            else:
                student.deiconify()
                login.destroy()
        else:
            msg.showerror("Enter email and password         ")


class Student(Tk):
    '''
    Main Application
    '''
    def __init__(self):
        super().__init__()
        self.title("Student Database Management System")
        self.geometry('1300x750+0+0')
        self.resizable(False, False)
        self.config(bg='light blue')

        ##########   Variables  ##########
        self.student_id = StringVar()
        self.password = StringVar()
        self.first_name = StringVar()
        self.last_name = StringVar()
        self.age = StringVar()
        self.address = StringVar()
        self.phone_number = StringVar()
        self.year = StringVar()
        self.status = StringVar()
        self.email = StringVar()
        self.student_search = StringVar()

        ##############    Frames    ###################
        main_frame = Frame(self, bg='light blue')
        main_frame.grid()

        title_frame = Frame(main_frame, bg='white', bd=2,
                            padx=55, pady=8, relief=RIDGE)
        title_frame.pack(side=TOP, fill=BOTH, expand=True)

        self.label_title = Label(title_frame, text='Student Database Management System', font=('calibri', 47, 'bold'), bg='white')
        self.label_title.grid()

        button_frame = Frame(main_frame, width='1450', height='70', bg='white', bd=2, padx=18, pady=10, relief=RIDGE)
        button_frame.pack(side=BOTTOM)

        data_frame = Frame(main_frame, width='1400', height='400', bg='light blue', bd=1, padx=20, pady=20, relief=RIDGE)
        data_frame.pack(side=TOP, fill=BOTH, expand=True)

        left_frame = LabelFrame(data_frame, width='1100', height='600', bg='white', bd=1, padx=20, relief=RIDGE, font=('calibri', 20, 'bold'), text="Student Info\n")
        left_frame.pack(side=LEFT)

        right_frame = LabelFrame(data_frame, width='350', height='300', bg='white', bd=1, padx=31, pady=3, relief=RIDGE, font=('calibri', 20, 'bold'), text="Student Details\n")
        right_frame.pack(side=RIGHT)

        ########### Labels and Entry Boxes #############
        self.label_id = Label(left_frame, font=('calibri', 20, 'bold'), text='Student Id: ', bg='white', padx=2, pady=2)
        self.label_id.grid(row=0, column=0, sticky=W)
        self.entry_id = Entry(left_frame, font=('calibri', 20, 'bold'), bg='light grey', textvariable=self.student_id, width=39)
        self.entry_id.grid(row=0, column=1)
        self.label_id_error = Label(left_frame, font=('calibri', 20, 'bold'),text="*", fg='white', bg='white', pady=2)
        self.label_id_error.grid(row=0, column=2)

        self.label_password = Label(left_frame, font=('calibri', 20, 'bold'), text='Password: ', bg='white', padx=2, pady=2)
        self.label_password.grid(row=1, column=0, sticky=W)
        self.entry_password = Entry(left_frame, font=('calibri', 20, 'bold'), bg='light grey', show='*', textvariable=self.password, width=39)
        self.entry_password.grid(row=1, column=1)
        self.label_password_error = Label(left_frame, font=('calibri', 20, 'bold'), text="*", fg='white',bg='white', pady=2)
        self.label_password_error.grid(row=1, column=2)

        self.label_first_name = Label(left_frame, font=('calibri', 20, 'bold'), text='First Name: ', bg='white', padx=2, pady=2)
        self.label_first_name.grid(row=2, column=0, sticky=W)
        self.entry_first_name = Entry(left_frame, font=('calibri', 20, 'bold'), bg='light grey', textvariable=self.first_name, width=39)
        self.entry_first_name.grid(row=2, column=1)
        self.label_first_name_error = Label(left_frame, font=('calibri', 20, 'bold'), text="*", fg='white', bg='white', pady=2)
        self.label_first_name_error.grid(row=2, column=2)

        self.label_last_name = Label(left_frame, font=('calibri', 20, 'bold'), text='Last Name: ', bg='white', padx=2, pady=2)
        self.label_last_name.grid(row=3, column=0, sticky=W)
        self.entry_last_name = Entry(left_frame, font=('calibri', 20, 'bold'), bg='light grey', textvariable=self.last_name, width=39)
        self.entry_last_name.grid(row=3, column=1)
        self.label_last_name_error = Label(left_frame, font=('calibri', 20, 'bold'), text="*", fg='white', bg='white', pady=2)
        self.label_last_name_error.grid(row=3, column=2)

        self.label_email = Label(left_frame, font=('calibri', 20, 'bold'), text='Email: ', bg='white', padx=2, pady=2)
        self.label_email.grid(row=4, column=0, sticky=W)
        self.entry_email = Entry(left_frame, font=('calibri', 20, 'bold'), bg='light grey', textvariable=self.email, width=39)
        self.entry_email.grid(row=4, column=1)
        self.label_email_error = Label(left_frame, font=('calibri', 20, 'bold'), text="*", fg='white', bg='white', pady=2)
        self.label_email_error.grid(row=4, column=2)

        self.label_age = Label(left_frame, font=('calibri', 20, 'bold'), text='Age: ', bg='white', padx=2, pady=2)
        self.label_age.grid(row=5, column=0, sticky=W)
        self.entry_age = Entry(left_frame, font=('calibri', 20, 'bold'), bg='light grey', textvariable=self.age, width=39)
        self.entry_age.grid(row=5, column=1)

        self.label_address = Label(left_frame, font=('calibri', 20, 'bold'), text='Address: ', bg='white', padx=2, pady=2)
        self.label_address.grid(row=6, column=0, sticky=W)
        self.entry_address = Entry(left_frame, font=('calibri', 20, 'bold'), bg='light grey', textvariable=self.address, width=39)
        self.entry_address.grid(row=6, column=1)

        self.label_phone_number = Label(left_frame, font=('calibri', 20, 'bold'), text='Phone Number: ', bg='white', padx=2, pady=2)
        self.label_phone_number.grid(row=7, column=0, sticky=W)
        self.entry_phone_number = Entry(left_frame, font=('calibri', 20, 'bold'), bg='light grey', textvariable=self.phone_number, width=39)
        self.entry_phone_number.grid(row=7, column=1)

        self.label_year = Label(left_frame, font=('calibri', 20, 'bold'), text='Year: ', bg='white', padx=2, pady=2)
        self.label_year.grid(row=8, column=0, sticky=W)
        self.entry_year = Entry(left_frame, font=('calibri', 20, 'bold'), bg='light grey', textvariable=self.year, width=39)
        self.entry_year.grid(row=8, column=1)

        self.label_status = Label(left_frame, font=('calibri', 20, 'bold'), text='Status: ', bg='white', padx=2, pady=2)
        self.label_status.grid(row=9, column=0, sticky=W)
        self.entry_status = Entry(left_frame, font=('calibri', 20, 'bold'), bg='light grey', textvariable=self.status, width=39)
        self.entry_status.grid(row=9, column=1)

        self.label_search = Label(right_frame, font=('calibri', 20, 'bold'), text='Search ', justify=CENTER, bg='white', padx=2, pady=2)
        self.label_search.grid(row=0, column=0, sticky='ew')
        self.entry_search = Entry(right_frame, font=('calibri', 20, 'bold'), bg='light grey', textvariable=self.student_search, width=20)
        self.entry_search.grid(row=1, column=0)
        self.entry_search.bind('<Key>', lambda event: self.search(event))

        ############ Scrollbar and Listbox ################
        self.scrollbar = Scrollbar(right_frame)
        self.scrollbar.grid(row=2, column=1, sticky='ns')
        self.student_list = Listbox(right_frame, width=41, height=16, font=('calibri', 12, 'bold'), yscrollcommand=self.scrollbar.set)
        self.student_list.grid(row=2, column=0, padx=8)
        self.student_list.bind('<<ListboxSelect>>', lambda event: self.studentRecord(event))
        self.scrollbar.config(command=self.student_list.yview)

        ############ Buttons ####################
        self.btnUpdateData = Button(button_frame, text="Update", command=self.update, font=('calibri', 20, 'bold'), height=1, width=12, bd=2, relief=SOLID)
        self.btnUpdateData.grid(row=0, column=0)

        self.btnExportData = Button(button_frame, text="Export", command=self.export_data, font=('calibri', 20, 'bold'), height=1, width=12, bd=2, relief=SOLID)
        self.btnExportData.grid(row=0, column=1)

        self.btnDisplayData = Button(button_frame, text="Display", command=self.display, font=('calibri', 20, 'bold'), height=1, width=12, bd=2, relief=SOLID)
        self.btnDisplayData.grid(row=0, column=2)

        self.btnClearData = Button(button_frame, text="Clear", command=self.clear, font=('calibri', 20, 'bold'), height=1, width=12, bd=2, relief=SOLID)
        self.btnClearData.grid(row=0, column=3)

        self.btnDeleteData = Button(button_frame, text="Delete", font=('calibri', 20, 'bold'), command=self.delete, height=1, width=12, bd=2, relief=SOLID)
        self.btnDeleteData.grid(row=0, column=4)

        self.btnAddNewData = Button(button_frame, text="Add New", command=self.addData, font=('calibri', 20, 'bold'), height=1, width=12, bd=2, relief=SOLID)
        self.btnAddNewData.grid(row=0, column=5)

        self.btnExit = Button(button_frame, text="Exit", font=('calibri', 20, 'bold'), command=sys.exit, height=1, width=12, bd=2, relief=SOLID)
        self.btnExit.grid(row=0, column=6)

        ############ Control Functions ##########
    def export_data(self) -> None:
        '''
        Uses StudentDB class to export data
        Displays message of the results
        '''
        result = StudentDB.export()
        if result == True:
            msg.showinfo("Records exported            ")
        else:
            msg.showerror("Could not export            ")

    def delete(self) -> None:
        '''
        Uses the StudentDB class to delete record selected
        Confirms deletion before deleting
        '''
        answer = msg.askyesno("Delete the selected student?                ")
        if answer == True:
            try:
                selection = self.student_list.curselection()[0]
                if type(selection) == int:
                    selection += 1
                StudentDB.delete_data(str(selection))
                self.clear()
                self.display()
            except:
                msg.showinfo("Please select a student!!         ")

    def display(self) -> None:
        '''
        Uses StudentDB class to retrieve all records and displays them in a listbox
        '''
        self.student_list.delete(0, END)
        rows = StudentDB.displayDB()
        for row in rows:
            self.student_list.insert(END, row)

    def clear(self) -> None:
        '''
        Clears all entry fields
        '''
        self.entry_id.delete(0, END)
        self.entry_password.delete(0, END)
        self.entry_first_name.delete(0, END)
        self.entry_last_name.delete(0, END)
        self.entry_address.delete(0, END)
        self.entry_age.delete(0, END)
        self.entry_phone_number.delete(0, END)
        self.entry_status.delete(0, END)
        self.entry_year.delete(0, END)
        self.entry_email.delete(0, END)
        self.reset_error()
        
    def reset_error(self) -> None:
        '''
        Resets error astericks when adding invalid data
        '''
        self.label_id_error.config(fg='white')
        self.label_first_name_error.config(fg='white')
        self.label_last_name_error.config(fg='white')
        self.label_password_error.config(fg='white')
        self.label_email_error.config(fg='white')
            
    def studentRecord(self, event) -> None:
        '''
        Auto fills entry boxes with listbox selection
        :param event: event is a mouse click and is assigned an index from selection
        '''
        self.reset_error()
        global id
        studentSearch = (self.student_list.curselection()[0] + 1)
        listId = StudentDB.searchId(event, str(studentSearch))
        self.clear()
        self.entry_id.insert(END, listId[0][2])
        self.entry_password.insert(END, listId[0][1])
        self.entry_first_name.insert(END, listId[0][3])
        self.entry_last_name.insert(END, listId[0][4])
        self.entry_email.insert(END, listId[0][5])
        self.entry_age.insert(END, listId[0][6])
        self.entry_address.insert(END, listId[0][7])
        self.entry_phone_number.insert(END, listId[0][8])
        self.entry_year.insert(END, listId[0][9])
        self.entry_status.insert(END, listId[0][10])
        id = listId[0][0]

    def search(self, event) -> None:
        '''
        Uses StudentDB class to retrieve results of search and displays them in the listbox
        :param event: Event is a keystroke. Retrieves entry text and searches for results in the database
        '''
        self.reset_error()
        mystring = self.student_search.get()
        if len(mystring) > 0:
            rows = StudentDB.searchdb(event, mystring)
            self.student_list.delete(0, END)
            for row in rows:
                self.student_list.insert(END, row,)
        else:
            self.display()

    def update(self) -> None:
        '''
        Uses StudentDB class to update the current selection in the database
        '''
        self.reset_error()
        global id
        if (self.password.get() == "") or (self.first_name.get() == "") or (self.last_name.get()==""):
            msg.showerror("Invalid Entry               ")
            self.label_password_error.config(fg='red')
            self.label_first_name_error.config(fg='red')
            self.label_last_name_error.config(fg='red')
        else:
            StudentDB.update(id, self.password.get(), self.first_name.get(), self.last_name.get(), self.age.get(), self.address.get(), self.phone_number.get(), self.year.get(), self.status.get())
            self.display()

    def addData(self) -> None:
        '''
        Uses StudentDB class to add new data to the database
        '''
        valid=True
        data = [self.password.get(), self.student_id.get(), self.first_name.get(), self.last_name.get(), self.email.get(), self.age.get(
        ), self.address.get(), self.phone_number.get(), self.year.get(), self.status.get()]
        
        if (data[0] == "" and data[1] == "" and data[2] == "" and data[3] == "" and data[4] == ""):
            msg.showerror("Invalid Entry               ")
            self.label_password_error.config(fg='red')
            self.label_id_error.config(fg='red')
            self.label_first_name_error.config(fg='red')
            self.label_last_name_error.config(fg='red')
            self.label_email_error.config(fg='red')
            valid=False
        else:    
            if (data[0] == ""):
                self.label_password_error.config(fg="red")
                valid=False
            else:
                self.label_password_error.config(fg="white")
                valid=True
                
            if (data[1] == ""):
                self.label_id_error.config(fg="red")
                valid=False
            elif (StudentDB.find_duplicates(data[1]) == True):
                self.label_id_error.config(fg="red")
                valid=False
                msg.showerror("Duplicate student id               ")
            else:
                self.label_id_error.config(fg='white')
                valid=True
                
            if (data[2] == ""):
                self.label_first_name_error.config(fg="red")
                valid=False
            else:
                self.label_first_name_error.config(fg='white')
                valid=True
                
            if (data[3] == ""):
                self.label_last_name_error.config(fg="red")
                valid=False
            else:
                self.label_last_name_error.config(fg='white')
                valid=True
                
            if (data[4] == ""):
                self.label_email_error.config(fg="red")
                valid=False
                msg.showerror("Please enter email                  ")
            elif (StudentDB.find_duplicates(data[4]) == True):
                self.label_email_error.config(fg="red")
                valid=False
                msg.showerror("Duplicate email                 ")
            else:
                self.label_email_error.config(fg='white')
                valid=True
                
        if (valid==True):     
            StudentDB.addNew(data)
            self.display()


if __name__ == "__main__":
    student = Student()
    StudentDB()
    student.withdraw()
    login = Login()
    student.mainloop()

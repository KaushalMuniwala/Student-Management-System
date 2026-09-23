# from tkinter import *
# from PIL import Image, ImageTk, ImageSequence
# from tkinter import ttk,messagebox
# import sqlite3

# class studentClass:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Student Management System")
#         self.root.config(bg="white")
#         self.root.update_idletasks()  # Ensure Tkinter initializes before setting geometry
#         self.center_window()
#         self.root.focus_force()
        
#         # Title
#         title = Label(self.root, text="Manage Student Details", padx=10, compound=LEFT,font=("montserrat", 20, "bold"), bg="#232323", fg="white")
#         title.place(x=0, y=0, relwidth=1, height=50)
        
#         # Variables
#         self.var_roll=StringVar()
#         self.var_name=StringVar()
#         self.var_email=StringVar()
#         self.var_gender=StringVar()
#         self.var_dob=StringVar()
#         self.var_contact=StringVar()
#         self.var_course=StringVar()
#         self.var_a_date=StringVar()
#         self.var_state=StringVar()
#         self.var_city=StringVar()
#         self.var_pin=StringVar()
        
#         # Widgets
#         # column1
#         lbl_roll=Label(self.root,text="Roll No:",font=("montserrat",15,'bold'),bg="white").place(x=10,y=70)
#         lbl_name=Label(self.root,text="Name:",font=("montserrat",15,'bold'),bg="white").place(x=10,y=130)
#         lbl_email=Label(self.root,text="Email:",font=("montserrat",15,'bold'),bg="white").place(x=10,y=190)
#         lbl_gender=Label(self.root,text="Gender:",font=("montserrat",15,'bold'),bg="white").place(x=10,y=250)
        
#         lbl_state=Label(self.root,text="State:",font=("montserrat",15,'bold'),bg="white").place(x=10,y=310)
#         txt_state=Entry(self.root,textvariable=self.var_state,font=("montserrat",15,'bold'),bg="#ffcbd1").place(x=120,y=310,width=120)
#         lbl_city=Label(self.root,text="City:",font=("montserrat",15,'bold'),bg="white").place(x=270,y=310)
#         txt_city=Entry(self.root,textvariable=self.var_city,font=("montserrat",15,'bold'),bg="#ffcbd1").place(x=340,y=310,width=120)
#         lbl_pin=Label(self.root,text="Pin:",font=("montserrat",15,'bold'),bg="white").place(x=490,y=310)
#         txt_pin=Entry(self.root,textvariable=self.var_pin,font=("montserrat",15,'bold'),bg="#ffcbd1").place(x=560,y=310,width=120)
        
#         lbl_address=Label(self.root,text="Address:",font=("montserrat",15,'bold'),bg="white").place(x=10,y=360)
        
#         # Entry Fields
#         self.txt_roll=Entry(self.root,textvariable=self.var_roll,font=("montserrat",15,'bold'),bg="#ffcbd1")
#         self.txt_roll.place(x=120,y=70,width=200)
        
#         txt_name=Entry(self.root,textvariable=self.var_name,font=("montserrat",15,'bold'),bg="#ffcbd1").place(x=120,y=130,width=200)
#         txt_email=Entry(self.root,textvariable=self.var_email,font=("montserrat",15,'bold'),bg="#ffcbd1").place(x=120,y=190,width=200)
        
#         self.txt_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),font=("montserrat",15,'bold'),state='readonly',justify=CENTER)
#         self.txt_gender.place(x=120,y=250,width=200)
#         self.txt_gender.current(0)
        
#         # Widgets
#         # Column2
#         lbl_dob=Label(self.root,text="D.O.B:",font=("montserrat",15,'bold'),bg="white").place(x=330,y=70)
#         lbl_contact=Label(self.root,text="Contact:",font=("montserrat",15,'bold'),bg="white").place(x=330,y=130)
#         lbl_addmission=Label(self.root,text="Addmission:",font=("montserrat",15,'bold'),bg="white").place(x=330,y=190)
#         lbl_course=Label(self.root,text="Course:",font=("montserrat",15,'bold'),bg="white").place(x=330,y=250)
        
        
#         # Entry Fields
#         self.course_list=[]
#         # Fuction_call to update the list
#         self.fetch_course()
#         txt_dob=Entry(self.root,textvariable=self.var_dob,font=("montserrat",15,'bold'),bg="#ffcbd1").place(x=480,y=70,width=200)
#         txt_contact=Entry(self.root,textvariable=self.var_contact,font=("montserrat",15,'bold'),bg="#ffcbd1").place(x=480,y=130,width=200)
#         txt_addmision=Entry(self.root,textvariable=self.var_a_date,font=("montserrat",15,'bold'),bg="#ffcbd1").place(x=480,y=190,width=200)
#         self.txt_course=ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list,font=("montserrat",15,'bold'),state='readonly',justify=CENTER)
#         self.txt_course.place(x=480,y=250,width=200)
#         self.txt_course.set("Select")
        
#         # Text Address
#         self.txt_address=Text(self.root,font=("montserrat",15,'bold'),bg="#ffcbd1")
#         self.txt_address.place(x=120,y=360,width=560,height=150)
  
#         # Buttons
#         self.btn_add=Button(self.root,text="Save",font=("montserrat",15,'bold'),bg="#28A745",fg="white",cursor="hand2",command=self.add)
#         self.btn_add.place(x=120,y=590,width=110,height=40)
#         self.btn_update=Button(self.root,text="Update",font=("montserrat",15,'bold'),bg="#007BFF",fg="black",cursor="hand2",command=self.update)
#         self.btn_update.place(x=270,y=590,width=110,height=40)
#         self.btn_delete=Button(self.root,text="Delete",font=("montserrat",15,'bold'),bg="#DC3545",fg="black",cursor="hand2",command=self.delete)
#         self.btn_delete.place(x=420,y=590,width=110,height=40)
#         self.btn_clear=Button(self.root,text="Clear",font=("montserrat",15,'bold'),bg="#6C757D",fg="white",cursor="hand2",command=self.clear)
#         self.btn_clear.place(x=570,y=590,width=110,height=40)
  
#         # Search Panel
#         self.var_search=StringVar()
#         lbl_search_roll=Label(self.root,text="Roll No:",font=("montserrat",15,'bold'),bg="white").place(x=770,y=70)
#         txt_search_roll=Entry(self.root,textvariable=self.var_search,font=("montserrat",15,'bold'),bg="#ffcbd1").place(x=890,y=70,width=390)
        
#         btn_search=Button(self.root,text="Search",font=("montserrat",12,'bold'),bg="#17A2B8",fg="black",cursor="hand2",command=self.search).place(x=1305,y=70,width=120,height=30)
        
#         # Content
#         self.C_Frame=Frame(self.root,bd=10,relief=RIDGE)
#         self.C_Frame.place(x=755,y=130,width=670,height=500)
        
#         # Scrollbar
#         scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
#         scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        
#         self.CourseTable=ttk.Treeview(self.C_Frame,columns=("roll","name","email","gender","dob","contact","admission","course","state","city","pin","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
#         scrollx.pack(side=BOTTOM,fill=X)
#         scrolly.pack(side=RIGHT,fill=Y)
#         scrollx.config(command=self.CourseTable.xview)
#         scrolly.config(command=self.CourseTable.yview)
        
#         self.CourseTable.heading("roll",text="Roll No")
#         self.CourseTable.heading("name",text="Name")
#         self.CourseTable.heading("email",text="Email")
#         self.CourseTable.heading("gender",text="Gender")
#         self.CourseTable.heading("dob",text="D.O.B")
#         self.CourseTable.heading("contact",text="Contact")
#         self.CourseTable.heading("admission",text="Admission")
#         self.CourseTable.heading("course",text="Course")
#         self.CourseTable.heading("state",text="State")
#         self.CourseTable.heading("city",text="City")
#         self.CourseTable.heading("pin",text="PIN")
#         self.CourseTable.heading("pin",text="Address")
        
#         self.CourseTable["show"]='headings'
        
#         self.CourseTable.column("roll",width=100)
#         self.CourseTable.column("name",width=100)
#         self.CourseTable.column("email",width=100)
#         self.CourseTable.column("gender",width=100)
#         self.CourseTable.column("dob",width=100)
#         self.CourseTable.column("contact",width=100)
#         self.CourseTable.column("admission",width=100)
#         self.CourseTable.column("course",width=100)
#         self.CourseTable.column("state",width=100)
#         self.CourseTable.column("city",width=100)
#         self.CourseTable.column("pin",width=100)
#         self.CourseTable.column("address",width=100)
        
#         self.CourseTable.pack(fill=BOTH,expand=1)
        
#         self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
#         self.show()
        

#         # Footer
#         footer = Label(self.root, text="SMS - Student Management System",font=("montserrat", 12), bg="#232323", fg="white").pack(side=BOTTOM,fill=X)
#         title.place(x=0, y=0, relwidth=1, height=50)
        
# #----------------------------------------------------------------------------------------------------------------------------------------------------
    
    
#     def clear(self):
#         self.show()
#         self.var_roll.set("")
#         self.var_name.set("")
#         self.var_email.set("")
#         self.var_gender.set("Select")
#         self.var_dob.set("")
#         self.var_contact.set("")
#         self.var_a_date.set("")
#         self.var_course.set("Select")
#         self.var_state.set("")
#         self.var_city.set("")
#         self.var_pin.set("")
#         self.txt_address.delete("1.0",END)   
#         self.txt_roll.config(state=NORMAL)
#         self.var_search.set("")
    
#     def delete(self):
#         con=sqlite3.connect(database="sms.db")
#         cur=con.cursor()
#         try:
#             if self.var_roll.get()=="":
#                 messagebox.showerror("Error","Roll Number should be required",parent=self.root)
#             else:
#                 cur.execute("select * from student where roll=?",(self.var_roll.get(),))
#                 row=cur.fetchone()
#                 print(row)
#                 if row==None:
#                     messagebox.showerror("Error","Please select student from the list first",parent=self.root)
#                 else:
#                     op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
#                     if op==True:
#                         cur.execute("Delete from student where roll=?",(self.var_roll.get(),))
#                         con.commit()
#                         messagebox.showinfo("Delete","Student Deleted Successfully",parent=self.root)
#                         self.clear()
#         except Exception as ex:
#             messagebox.showerror("Error",f"Enter due to {str(ex)}")
    
    
#     def get_data(self,ev):
#         self.txt_roll.config(state="readonly")
#         # self.txt_roll
#         r=self.CourseTable.focus()
#         content=self.CourseTable.item(r)
#         row=content["values"]
#         # print(row)
#         self.var_roll.set(row[0])
#         self.var_name.set(row[1])
#         self.var_email.set(row[2])
#         self.var_gender.set(row[3])
#         self.var_dob.set(row[4])
#         self.var_contact.set(row[5])
#         self.var_a_date.set(row[6])
#         self.var_course.set(row[7])
#         self.var_state.set(row[8])
#         self.var_city.set(row[9])
#         self.var_pin.set(row[10])
#         self.txt_address.delete("1.0",END)
#         self.txt_address.insert(END,row[11])
        
        
#     def add(self):
#         con=sqlite3.connect(database="sms.db")
#         cur=con.cursor()
#         try:
#             if self.var_roll.get()=="":
#                 messagebox.showerror("Error","Roll Number should be required",parent=self.root)
#             else:
#                 cur.execute("select * from student where roll=?",(self.var_roll.get(),))
#                 row=cur.fetchone()
#                 print(row)
#                 if row!=None:
#                     messagebox.showerror("Error","Roll Number already present",parent=self.root)
#                 else:
#                     cur.execute("insert into student (roll,name,email,gender,dob,contact,admission,course,state,city,pin,address) values(?,?,?,?,?,?,?,?,?,?,?,?)",(
#                         self.var_roll.get(),
#                         self.var_name.get(),
#                         self.var_email.get(),
#                         self.var_gender.get(),
#                         self.var_dob.get(),
#                         self.var_contact.get(),
#                         self.var_a_date.get(),
#                         self.var_course.get(),
#                         self.var_state.get(),
#                         self.var_city.get(),
#                         self.var_pin.get(),
#                         self.txt_address.get("1.0",END)
#                     ))
#                     con.commit()
#                     messagebox.showerror("Success","Student Addedd Successfully",parent=self.root)  
#                     self.show()         
#         except Exception as ex:
#             messagebox.showerror("Error",f"Enter due to {str(ex)}")
            
            
#     def search(self):
#         con=sqlite3.connect(database="sms.db")
#         cur=con.cursor()
#         try:
#             cur.execute("select * from student where roll=?",(self.var_search.get(),))
#             row=cur.fetchone()  
#             if row!=None:
#                 self.CourseTable.delete(*self.CourseTable.get_children())
#                 self.CourseTable.insert('',END,values=row)
#             else:
#                 messagebox.showerror("Error","No record found",parent=self.root)
#         except Exception as ex:
#             messagebox.showerror("Error",f"Enter due to {str(ex)}")
            
    
#     def show(self):
#         con=sqlite3.connect(database="sms.db")
#         cur=con.cursor()
#         try:
#             cur.execute("select * from student")
#             rows=cur.fetchall()         
#             self.CourseTable.delete(*self.CourseTable.get_children())
#             for row in rows:
#                 self.CourseTable.insert('',END,values=row)
#         except Exception as ex:
#             messagebox.showerror("Error",f"Enter due to {str(ex)}")
      
      
#     def fetch_course(self):
#         con=sqlite3.connect(database="sms.db")
#         cur=con.cursor()
#         try:
#             cur.execute("select name from course")
#             rows=cur.fetchall()    
#             if len(rows)>0:
#                 for row in rows:
#                     self.course_list.append(row[0])
#             # print(v)
            
#         except Exception as ex:
#             messagebox.showerror("Error",f"Enter due to {str(ex)}")
        
        
#     def update(self):
#         con=sqlite3.connect(database="sms.db")
#         cur=con.cursor()
#         try:
#             if self.var_roll.get()=="":
#                 messagebox.showerror("Error","Roll Number should be required",parent=self.root)
#             else:
#                 cur.execute("select * from student where roll=?",(self.var_roll.get(),))
#                 row=cur.fetchone()
#                 #print(row)
#                 if row==None:
#                     messagebox.showerror("Error","Select student from list",parent=self.root)
#                 else:
#                     cur.execute("update student set name=?,email=?,gender=?,dob=?,contact=?,admission=?,course=?,state=?,city=?,pin=?,address=? where roll=?",(
                        
#                         self.var_name.get(),
#                         self.var_email.get(),
#                         self.var_gender.get(),
#                         self.var_dob.get(),
#                         self.var_contact.get(),
#                         self.var_a_date.get(),
#                         self.var_course.get(),
#                         self.var_state.get(),
#                         self.var_city.get(),
#                         self.var_pin.get(),
#                         self.txt_address.get("1.0",END),
#                         self.var_roll.get(),
#                     ))
#                     con.commit()
#                     messagebox.showerror("Success","Student Update Successfully",parent=self.root)  
#                     self.show()         
#         except Exception as ex:
#             messagebox.showerror("Error",f"Enter due to {str(ex)}")
        
        
#     def center_window(self, width=1450, height=700):
#         screen_width = self.root.winfo_screenwidth()
#         screen_height = self.root.winfo_screenheight()

#         x_position = (screen_width // 2) - (width // 2)
#         y_position = (screen_height // 2) - (height // 2)

#         self.root.geometry(f"{width}x{height}+{x_position}+{y_position}")
    
        
# if __name__ == "__main__":
#     root = Tk()
#     obj = studentClass(root)
#     root.mainloop()

from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
import os
from datetime import datetime

try:
    from tkcalendar import DateEntry
except ModuleNotFoundError:
    DateEntry = None

DB_PASSWORD = os.getenv("SMS_DB_PASSWORD", "root")

class studentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Manage Student")
        self.root.config(bg="white")
        self.root.update_idletasks()
        self.root.geometry("1295x735+233+50")
        self.root.focus_force()
        
        # Title
        title = Label(self.root, text="Manage Student Details", padx=10, compound=LEFT, font=("montserrat", 20, "bold"), bg="#0C1C47", fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)
        
        # Variables
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()
        self.course_list = StringVar()
        
        # Widgets
        # column1
        lbl_roll = Label(self.root, text="Roll No:", font=("montserrat", 15, 'bold'), bg="white").place(x=10, y=70)
        
        # Roll No Entry (Disabled)
        self.txt_roll = Entry(self.root, textvariable=self.var_roll, font=("montserrat", 15, 'bold'), bg="#ffcbd1", state="readonly")
        self.txt_roll.place(x=120, y=70, width=200)
        
        lbl_name = Label(self.root, text="Name:", font=("montserrat", 15, 'bold'), bg="white").place(x=10, y=130)
        lbl_email = Label(self.root, text="Email:", font=("montserrat", 15, 'bold'), bg="white").place(x=10, y=190)
        lbl_gender = Label(self.root, text="Gender:", font=("montserrat", 15, 'bold'), bg="white").place(x=10, y=250)
        
        lbl_state = Label(self.root, text="State:", font=("montserrat", 15, 'bold'), bg="white").place(x=10, y=310)
        txt_state = Entry(self.root, textvariable=self.var_state, font=("montserrat", 15, 'bold'), bg="#C6E2FF").place(x=120, y=310, width=120)
        lbl_city = Label(self.root, text="City:", font=("montserrat", 15, 'bold'), bg="white").place(x=270, y=310)
        txt_city = Entry(self.root, textvariable=self.var_city, font=("montserrat", 15, 'bold'), bg="#C6E2FF").place(x=340, y=310, width=120)
        lbl_pin = Label(self.root, text="Pin:", font=("montserrat", 15, 'bold'), bg="white").place(x=490, y=310)
        txt_pin = Entry(self.root, textvariable=self.var_pin, font=("montserrat", 15, 'bold'), bg="#C6E2FF").place(x=560, y=310, width=120)
        
        lbl_address = Label(self.root, text="Address:", font=("montserrat", 15, 'bold'), bg="white").place(x=10, y=360)
        
        # Entry Fields
        txt_name = Entry(self.root, textvariable=self.var_name, font=("montserrat", 15, 'bold'), bg="#C6E2FF").place(x=120, y=130, width=200)
        txt_email = Entry(self.root, textvariable=self.var_email, font=("montserrat", 15, 'bold'), bg="#C6E2FF").place(x=120, y=190, width=200)
        
        self.txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select", "Male", "Female", "Other"), font=("montserrat", 15, 'bold'), state='readonly', justify=CENTER)
        self.txt_gender.place(x=120, y=250, width=200)
        self.txt_gender.current(0)
        
        # Widgets
        # Column2
        lbl_dob = Label(self.root, text="D.O.B:", font=("montserrat", 15, 'bold'), bg="white").place(x=330, y=70)
        lbl_contact = Label(self.root, text="Contact:", font=("montserrat", 15, 'bold'), bg="white").place(x=330, y=130)
        lbl_addmission = Label(self.root, text="Admission:", font=("montserrat", 15, 'bold'), bg="white").place(x=330, y=190)
        lbl_course = Label(self.root, text="Course:", font=("montserrat", 15, 'bold'), bg="white").place(x=330, y=250)
        
        # DateEntry Widgets for DOB and Admission
        if DateEntry is not None:
            self.cal_dob = DateEntry(self.root, font=("montserrat", 15, 'bold'), bg="#C6E2FF", date_pattern='yyyy-mm-dd')
            self.cal_dob.place(x=480, y=70, width=200)
            self.cal_admission = DateEntry(self.root, font=("montserrat", 15, 'bold'), bg="#C6E2FF", date_pattern='yyyy-mm-dd')
            self.cal_admission.place(x=480, y=190, width=200)
        else:
            self.cal_dob = Entry(self.root, font=("montserrat", 15, 'bold'), bg="#C6E2FF")
            self.cal_dob.place(x=480, y=70, width=200)
            self.cal_dob.insert(0, datetime.today().strftime('%Y-%m-%d'))
            self.cal_admission = Entry(self.root, font=("montserrat", 15, 'bold'), bg="#C6E2FF")
            self.cal_admission.place(x=480, y=190, width=200)
            self.cal_admission.insert(0, datetime.today().strftime('%Y-%m-%d'))
        
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("montserrat", 15, 'bold'), bg="#C6E2FF").place(x=480, y=130, width=200)
        
        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course, values=self.course_list, font=("montserrat", 15, 'bold'), state='readonly', justify=CENTER)
        self.txt_course.place(x=480, y=250, width=200)
        self.txt_course.set("Select")
        self.fetch_course()
        
        # Text Address
        self.txt_address = Text(self.root, font=("montserrat", 15, 'bold'), bg="#C6E2FF")
        self.txt_address.place(x=120, y=360, width=560, height=150)

        # Buttons
        self.btn_add = Button(self.root, text="Save", font=("montserrat", 15, 'bold'), bg="#28A745", fg="white", cursor="hand2", command=self.add)
        self.btn_add.place(x=120, y=590, width=110, height=40)
        self.btn_update = Button(self.root, text="Update", font=("montserrat", 15, 'bold'), bg="#007BFF", fg="black", cursor="hand2", command=self.update)
        self.btn_update.place(x=270, y=590, width=110, height=40)
        self.btn_delete = Button(self.root, text="Delete", font=("montserrat", 15, 'bold'), bg="#DC3545", fg="black", cursor="hand2", command=self.delete)
        self.btn_delete.place(x=420, y=590, width=110, height=40)
        self.btn_clear = Button(self.root, text="Clear", font=("montserrat", 15, 'bold'), bg="#6C757D", fg="white", cursor="hand2", command=self.clear)
        self.btn_clear.place(x=570, y=590, width=110, height=40)
  
        # Search Panel
        self.var_search = StringVar()
        lbl_search_roll = Label(self.root, text="Roll No:", font=("montserrat", 15, 'bold'), bg="white").place(x=730, y=70)
        txt_search_roll = Entry(self.root, textvariable=self.var_search, font=("montserrat", 15, 'bold'), bg="#C6E2FF").place(x=830, y=70, width=290, height=32)
        
        btn_search = Button(self.root, text="Search", font=("montserrat", 12, 'bold'), bg="#0C1C47", fg="white", cursor="hand2", command=self.search).place(x=1140, y=70, width=120, height=32)
        
        # Content
        self.C_Frame = Frame(self.root, bd=10, relief=RIDGE)
        self.C_Frame.place(x=700, y=130, width=580, height=500)
        
        # Scrollbar
        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        
        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("roll", "name", "email", "gender", "dob", "contact", "admission", "course", "state", "city", "pin", "address"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        
        self.CourseTable.heading("roll", text="Roll No")
        self.CourseTable.heading("name", text="Name")
        self.CourseTable.heading("email", text="Email")
        self.CourseTable.heading("gender", text="Gender")
        self.CourseTable.heading("dob", text="D.O.B")
        self.CourseTable.heading("contact", text="Contact")
        self.CourseTable.heading("admission", text="Admission")
        self.CourseTable.heading("course", text="Course")
        self.CourseTable.heading("state", text="State")
        self.CourseTable.heading("city", text="City")
        self.CourseTable.heading("pin", text="PIN")
        self.CourseTable.heading("address", text="Address")
        
        self.CourseTable["show"] = 'headings'
        
        self.CourseTable.column("roll", width=100)
        self.CourseTable.column("name", width=100)
        self.CourseTable.column("email", width=100)
        self.CourseTable.column("gender", width=100)
        self.CourseTable.column("dob", width=100)
        self.CourseTable.column("contact", width=100)
        self.CourseTable.column("admission", width=100)
        self.CourseTable.column("course", width=100)
        self.CourseTable.column("state", width=100)
        self.CourseTable.column("city", width=100)
        self.CourseTable.column("pin", width=100)
        self.CourseTable.column("address", width=100)
        
        self.CourseTable.pack(fill=BOTH, expand=1)
        
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()
        
        # Footer
        footer = Label(self.root, text="Student Management System | GUJJU infotech | Contact Us: 7874273210",
                       font=("montserrat", 13),  bg="#0C1C47", fg="white")
        footer.pack(side=BOTTOM, fill=X)
        
    def _set_date_value(self, widget, value):
        if hasattr(widget, 'set_date'):
            widget.set_date(value)
        else:
            widget.delete(0, END)
            widget.insert(0, value.strftime('%Y-%m-%d'))

    def clear(self):
        self.show()
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_course.set("Select")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.txt_address.delete("1.0", END)
        self._set_date_value(self.cal_dob, datetime.now())
        self._set_date_value(self.cal_admission, datetime.now())
        self.txt_roll.config(state="readonly")
        self.var_search.set("")
    
    def delete(self):
        con = mysql.connector.connect(host="localhost", user="root", password=DB_PASSWORD, database="sms")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll Number should be required", parent=self.root)
            else:
                cur.execute("select * from student where roll=%s", (self.var_roll.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please select student from the list first", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("Delete from student where roll=%s", (self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Student Deleted Successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()
    
    def get_data(self, ev):
        self.txt_roll.config(state="readonly")
        r = self.CourseTable.focus()
        content = self.CourseTable.item(r)
        row = content["values"]
        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[5])
        self.var_course.set(row[7])
        self.var_state.set(row[8])
        self.var_city.set(row[9])
        self.var_pin.set(row[10])
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[11])
        
        # Set dates in date widgets
        try:
            dob_date = datetime.strptime(row[4], "%Y-%m-%d").date()
            self._set_date_value(self.cal_dob, dob_date)
        except:
            self._set_date_value(self.cal_dob, datetime.now())
            
        try:
            adm_date = datetime.strptime(row[6], "%Y-%m-%d").date()
            self._set_date_value(self.cal_admission, adm_date)
        except:
            self._set_date_value(self.cal_admission, datetime.now())
        
    def add(self):
        con = mysql.connector.connect(host="localhost", user="root", password=DB_PASSWORD, database="sms")
        cur = con.cursor()
        try:
            # Check if the selected course exists in the course table
            cur.execute("SELECT name FROM course WHERE name=%s", (self.var_course.get(),))
            course_row = cur.fetchone()
            if course_row is None:
                messagebox.showerror("Error", "Selected course does not exist", parent=self.root)
            else:
                # Get dates from date widgets
                if hasattr(self.cal_dob, 'get_date'):
                    dob = self.cal_dob.get_date().strftime("%Y-%m-%d")
                    admission = self.cal_admission.get_date().strftime("%Y-%m-%d")
                else:
                    dob = self.cal_dob.get().strip() or datetime.today().strftime('%Y-%m-%d')
                    admission = self.cal_admission.get().strip() or datetime.today().strftime('%Y-%m-%d')
                
                # Insert the student record
                cur.execute("""
                    INSERT INTO student (name, email, gender, dob, contact, admission, course, state, city, pin, address)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    self.var_name.get(),
                    self.var_email.get(),
                    self.var_gender.get(),
                    dob,
                    self.var_contact.get(),
                    admission,
                    self.var_course.get(),
                    self.var_state.get(),
                    self.var_city.get(),
                    self.var_pin.get(),
                    self.txt_address.get("1.0", END)
                ))
                con.commit()
                messagebox.showinfo("Success", "Student Added Successfully", parent=self.root)  
                self.show()         
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()
            
    def search(self):
        con = mysql.connector.connect(host="localhost", user="root", password=DB_PASSWORD, database="sms")
        cur = con.cursor()
        try:
            cur.execute("select * from student where roll=%s", (self.var_search.get(),))
            row = cur.fetchone()  
            if row != None:
                self.CourseTable.delete(*self.CourseTable.get_children())
                self.CourseTable.insert('', END, values=row)
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()
            
    def show(self):
        con = mysql.connector.connect(host="localhost", user="root", password=DB_PASSWORD, database="sms")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM student")
            rows = cur.fetchall()         
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()
      
    def fetch_course(self):
        con = mysql.connector.connect(host="localhost", user="root", password=DB_PASSWORD, database="sms")
        cur = con.cursor()
        try:
            cur.execute("SELECT name FROM course")
            rows = cur.fetchall()    
            if len(rows) > 0:
                self.course_list = [row[0] for row in rows]
                self.txt_course['values'] = self.course_list
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()
        
    def update(self):
        con = mysql.connector.connect(host="localhost", user="root", password=DB_PASSWORD, database="sms")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll Number should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM student WHERE roll=%s", (self.var_roll.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Select student from list", parent=self.root)
                else:
                    cur.execute("SELECT name FROM course WHERE name=%s", (self.var_course.get(),))
                    course_row = cur.fetchone()
                    if course_row is None:
                        messagebox.showerror("Error", "Selected course does not exist", parent=self.root)
                    else:
                        # Get dates from date widgets
                        if hasattr(self.cal_dob, 'get_date'):
                            dob = self.cal_dob.get_date().strftime("%Y-%m-%d")
                            admission = self.cal_admission.get_date().strftime("%Y-%m-%d")
                        else:
                            dob = self.cal_dob.get().strip() or datetime.today().strftime('%Y-%m-%d')
                            admission = self.cal_admission.get().strip() or datetime.today().strftime('%Y-%m-%d')
                        
                        cur.execute("""
                            UPDATE student SET name=%s, email=%s, gender=%s, dob=%s, contact=%s, 
                            admission=%s, course=%s, state=%s, city=%s, pin=%s, address=%s
                            WHERE roll=%s
                        """, (
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            dob,
                            self.var_contact.get(),
                            admission,
                            self.var_course.get(),
                            self.var_state.get(),
                            self.var_city.get(),
                            self.var_pin.get(),
                            self.txt_address.get("1.0", END),
                            self.var_roll.get(),
                        ))
                        con.commit()
                        messagebox.showinfo("Success", "Student Updated Successfully", parent=self.root)  
                        self.show()         
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()
        
if __name__ == "__main__":
    root = Tk()
    obj = studentClass(root)
    root.mainloop()
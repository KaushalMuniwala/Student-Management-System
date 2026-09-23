# import mysql.connector
# from tkinter import *
# from PIL import Image, ImageTk, ImageSequence
# from tkinter import ttk,messagebox
# import sqlite3

# class resultClass:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Student Management System")
#         self.root.config(bg="white")
#         self.root.update_idletasks()  # Ensure Tkinter initializes before setting geometry
#         self.center_window()
#         self.root.focus_force()
        
        
#         # Title
#         title = Label(self.root, text="Add Student Results", padx=10, compound=LEFT,font=("montserrat", 20, "bold"), bg="#232323", fg="white")
#         title.place(x=0, y=0, relwidth=1, height=50)
        
#         # Widgets
#         #Variables
#         self.var_roll=StringVar()
#         self.var_name=StringVar()
#         self.var_course=StringVar()
#         self.var_marks=StringVar()
#         self.var_full_marks=StringVar()
#         self.roll_list=[]
#         self.fetch_roll()
        
#         lbl_select=Label(self.root,text="Select Student:",font=("montserrat",20,"bold"),bg="white").place(x=50,y=100)
#         lbl_name=Label(self.root,text="Name:",font=("montserrat",20,"bold"),bg="white").place(x=50,y=160)
#         lbl_course=Label(self.root,text="Course:",font=("montserrat",20,"bold"),bg="white").place(x=50,y=220)
#         lbl_marks=Label(self.root,text="Marks Obtained:",font=("montserrat",20,"bold"),bg="white").place(x=50,y=280)
#         lbl_full_marks=Label(self.root,text="Full Marks:",font=("montserrat",20,"bold"),bg="white").place(x=50,y=340)
        
#         self.txt_student = ttk.Combobox(self.root, textvariable=self.var_roll, values=self.roll_list, font=("montserrat", 19, 'bold'), state='readonly', justify=CENTER)
#         self.txt_student.place(x=320, y=105, width=200)
#         self.txt_student.set("Select")
        
#         btn_search = Button(self.root, text="Search", font=("montserrat", 15, 'bold'), bg="#17A2B8", fg="black", cursor="hand2",command=self.search).place(x=550, y=105, width=120, height=40)

#         txt_name = Entry(self.root, textvariable=self.var_name, font=("montserrat", 20, 'bold'), bg="#ffcbd1",state="readonly").place(x=320, y=165, width=350)
#         txt_course = Entry(self.root, textvariable=self.var_course, font=("montserrat", 20, 'bold'), bg="#ffcbd1",state="readonly").place(x=320, y=225, width=350)
#         txt_marks = Entry(self.root, textvariable=self.var_marks, font=("montserrat", 20, 'bold'), bg="#ffcbd1").place(x=320, y=285, width=350)
#         txt_full_marks = Entry(self.root, textvariable=self.var_full_marks, font=("montserrat", 20, 'bold'), bg="#ffcbd1").place(x=320, y=345, width=350)

#         # Button
#         btn_add=Button(self.root,text="Submit",font=("montserrat",15),bg="green",fg="white",activebackground="green",cursor="hand2",command=self.add).place(x=320,y=565,width=150,height=40)
#         btn_clear=Button(self.root,text="Clear",font=("montserrat",15),bg="red",fg="white",activebackground="red",cursor="hand2",command=self.clear).place(x=520,y=565,width=150,height=40)
        
#         # Content Window
#         self.bg_img = Image.open("D:/Ashish khadela/Master/SEM_2/PYTHON/Mini_Project/SMS/Code/img/result.png")
#         self.bg_img = self.bg_img.resize((720, 500), Image.Resampling.LANCZOS)
#         self.bg_img = ImageTk.PhotoImage(self.bg_img)

#         self.lbl_bg = Label(self.root, image=self.bg_img)
#         self.lbl_bg.place(x=700, y=105, width=720, height=500)
        
#         # Footer
#         footer = Label(self.root, text="SMS - Student Management System",font=("montserrat", 12), bg="#232323", fg="white").pack(side=BOTTOM,fill=X)
#         title.place(x=0, y=0, relwidth=1, height=50)


#     def search(self):
#         con=sqlite3.connect(database="sms.db")
#         cur=con.cursor()
#         try:
#             cur.execute("select name,course from student where roll=?",(self.var_roll.get(),))
#             row=cur.fetchone()  
#             if row!=None:
#                 self.var_name.set( row[0])
#                 self.var_course.set(row[1])
#             else:
#                 messagebox.showerror("Error","No record found",parent=self.root)
#         except Exception as ex:
#             messagebox.showerror("Error",f"Enter due to {str(ex)}")
         
    
#     def add(self):
#         con=sqlite3.connect(database="sms.db")
#         cur=con.cursor()
#         try:
#             if self.var_name.get()=="":
#                 messagebox.showerror("Error","Please first search student record",parent=self.root)
#             else:
#                 cur.execute("select * from result where roll=? and course=?",(self.var_roll.get(),self.var_course.get(),))
#                 row=cur.fetchone()
#                 print(row)
#                 if row!=None:
#                     messagebox.showerror("Error","Result already present",parent=self.root)
#                 else:
#                     per=(int(self.var_marks.get())*100)/int(self.var_full_marks.get())
#                     cur.execute("insert into result (roll,name,course,marks_ob,full_marks,per) values(?,?,?,?,?,?)",(
#                         self.var_roll.get(),
#                         self.var_name.get(),
#                         self.var_course.get(),
#                         self.var_marks.get(),
#                         self.var_full_marks.get(),
#                         str(per)
#                     ))
#                     con.commit()
#                     messagebox.showerror("Success","Result Addedd Successfully",parent=self.root)       
#         except Exception as ex:
#             messagebox.showerror("Error",f"Enter due to {str(ex)}")
            
            
#     def clear(self):
#         self.var_roll.set("Select")
#         self.var_name.set("")
#         self.var_course.set("")
#         self.var_marks.set("")
#         self.var_full_marks.set("")

#     def fetch_roll(self):
#         con=sqlite3.connect(database="sms.db")
#         cur=con.cursor()
#         try:
#             cur.execute("select roll from student")
#             rows=cur.fetchall()    
#             if len(rows)>0:
#                 for row in rows:
#                     self.roll_list.append(row[0])
#             # print(v) 
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
#     obj = resultClass(root)
#     root.mainloop()


import mysql.connector
from tkinter import *
from PIL import Image, ImageTk, ImageSequence
from tkinter import ttk, messagebox
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "img")
DB_PASSWORD = os.getenv("SMS_DB_PASSWORD", "root")


def image_path(filename):
    return os.path.join(IMG_DIR, filename)

class resultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Manage Result")
        self.root.config(bg="white")
        self.root.update_idletasks()  # Ensure Tkinter initializes before setting geometry
        # self.center_window()
        self.root.geometry("1295x735+233+50")  # Example: Width=1350, Height=800, X=100, Y=50
        self.root.focus_force()

        # Title
        title = Label(self.root, text="Add Student Results", padx=10, compound=LEFT, font=("montserrat", 20, "bold"), bg="#0C1C47", fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)

        # Widgets
        # Variables
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_full_marks = StringVar()
        self.roll_list = []
        self.fetch_roll()

        lbl_select = Label(self.root, text="Select Student:", font=("montserrat", 20, "bold"), bg="white").place(x=50, y=100)
        lbl_name = Label(self.root, text="Name:", font=("montserrat", 20, "bold"), bg="white").place(x=50, y=160)
        lbl_course = Label(self.root, text="Course:", font=("montserrat", 20, "bold"), bg="white").place(x=50, y=220)
        lbl_marks = Label(self.root, text="Marks Obtained:", font=("montserrat", 20, "bold"), bg="white").place(x=50, y=280)
        lbl_full_marks = Label(self.root, text="Full Marks:", font=("montserrat", 20, "bold"), bg="white").place(x=50, y=340)

        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_roll, values=self.roll_list, font=("montserrat", 19, 'bold'), state='readonly', justify=CENTER)
        self.txt_student.place(x=320, y=105, width=200)
        self.txt_student.set("Select")

        btn_search = Button(self.root, text="Search", font=("montserrat", 15, 'bold'), bg="#0C1C47", fg="white", cursor="hand2", command=self.search).place(x=550, y=105, width=120, height=40)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("montserrat", 20, 'bold'), bg="#C6E2FF", state="readonly").place(x=320, y=165, width=350)
        txt_course = Entry(self.root, textvariable=self.var_course, font=("montserrat", 20, 'bold'), bg="#C6E2FF", state="readonly").place(x=320, y=225, width=350)
        txt_marks = Entry(self.root, textvariable=self.var_marks, font=("montserrat", 20, 'bold'), bg="#C6E2FF").place(x=320, y=285, width=350)
        txt_full_marks = Entry(self.root, textvariable=self.var_full_marks, font=("montserrat", 20, 'bold'), bg="#C6E2FF").place(x=320, y=345, width=350)

        # Button
        btn_add = Button(self.root, text="Submit", font=("montserrat", 15), bg="green", fg="white", activebackground="green", cursor="hand2", command=self.add).place(x=320, y=480, width=150, height=40)
        btn_clear = Button(self.root, text="Clear", font=("montserrat", 15), bg="red", fg="white", activebackground="red", cursor="hand2", command=self.clear).place(x=520, y=480, width=150, height=40)

        # Content Window
        self.bg_img = Image.open(image_path("result.png"))
        self.bg_img = self.bg_img.resize((570, 520), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img)
        self.lbl_bg.place(x=700, y=70, width=570, height=520)

        # Footer
        footer = Label(self.root, text="Student Management System | GUJJU infotech | Contact Us: 7874273210",
                       font=("montserrat", 13),  bg="#0C1C47", fg="white")
        footer.pack(side=BOTTOM, fill=X)

    def search(self):
        con = mysql.connector.connect(host="localhost", user="root", password=DB_PASSWORD, database="sms")
        cur = con.cursor()
        try:
            cur.execute("SELECT name, course FROM student WHERE roll=%s", (self.var_roll.get(),))
            row = cur.fetchone()
            if row is not None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

    def add(self):
        con = mysql.connector.connect(host="localhost", user="root", password=DB_PASSWORD, database="sms")
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Please first search student record", parent=self.root)
            else:
                cur.execute("SELECT * FROM result WHERE roll=%s AND course=%s", (self.var_roll.get(), self.var_course.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Result already present", parent=self.root)
                else:
                    per = (int(self.var_marks.get()) * 100) / int(self.var_full_marks.get())
                    cur.execute("INSERT INTO result (roll, name, course, marks_ob, full_marks, per) VALUES (%s, %s, %s, %s, %s, %s)", (
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks.get(),
                        self.var_full_marks.get(),
                        str(per)
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Result Added Successfully", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

    def clear(self):
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_full_marks.set("")

    def fetch_roll(self):
        con = mysql.connector.connect(host="localhost", user="root", password=DB_PASSWORD, database="sms")
        cur = con.cursor()
        try:
            cur.execute("SELECT roll FROM student")
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.roll_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

    # def center_window(self, width=1450, height=700):
    #     screen_width = self.root.winfo_screenwidth()
    #     screen_height = self.root.winfo_screenheight()
    #     x_position = (screen_width // 2) - (width // 2)
    #     y_position = (screen_height // 2) - (height // 2)
    #     self.root.geometry(f"{width}x{height}+{x_position}+{y_position}")

if __name__ == "__main__":
    root = Tk()
    obj = resultClass(root)
    root.mainloop()
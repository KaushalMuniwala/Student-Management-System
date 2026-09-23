from tkinter import *
from PIL import Image, ImageTk, ImageSequence
from tkinter import ttk, messagebox
import mysql.connector
import os

DB_PASSWORD = os.getenv("SMS_DB_PASSWORD", "root")

class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Manage Course")
        self.root.config(bg="white")
        self.root.update_idletasks()  # Ensure Tkinter initializes before setting geometry
        self.root.geometry("1295x735+233+50")  # Example: Width=1350, Height=800, X=100, Y=50

        self.root.focus_force()

        # Title
        title = Label(self.root, text="Manage Course Details", padx=10, compound=LEFT, font=("montserrat", 20, "bold"), bg="#0C1C47", fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)

        # Variables
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()

        # Widgets
        lbl_courseName = Label(self.root, text="Course Name:", font=("montserrat", 15, 'bold'), bg="white").place(x=10, y=70)
        lbl_duration = Label(self.root, text="Duration:", font=("montserrat", 15, 'bold'), bg="white").place(x=10, y=130)
        lbl_charges = Label(self.root, text="Charges:", font=("montserrat", 15, 'bold'), bg="white").place(x=10, y=190)
        lbl_description = Label(self.root, text="Description:", font=("montserrat", 15, 'bold'), bg="white").place(x=10, y=250)

        # Entry Fields
        self.txt_courseName = Entry(self.root, textvariable=self.var_course, font=("montserrat", 15, 'bold'), bg="#C6E2FF")
        self.txt_courseName.place(x=180, y=70, width=200)

        txt_duration = Entry(self.root, textvariable=self.var_duration, font=("montserrat", 15, 'bold'), bg="#C6E2FF").place(x=180, y=130, width=200)
        txt_charges = Entry(self.root, textvariable=self.var_charges, font=("montserrat", 15, 'bold'), bg="#C6E2FF").place(x=180, y=190, width=200)

        self.txt_description = Text(self.root, font=("montserrat", 15, 'bold'), bg="#C6E2FF")
        self.txt_description.place(x=180, y=250, width=400, height=150)

        # Buttons
        self.btn_add = Button(self.root, text="Save", font=("montserrat", 15, 'bold'), bg="#28A745", fg="white", cursor="hand2", command=self.add)
        self.btn_add.place(x=20, y=590, width=110, height=40)
        self.btn_update = Button(self.root, text="Update", font=("montserrat", 15, 'bold'), bg="#007BFF", fg="black", cursor="hand2", command=self.update)
        self.btn_update.place(x=170, y=590, width=110, height=40)
        self.btn_delete = Button(self.root, text="Delete", font=("montserrat", 15, 'bold'), bg="#DC3545", fg="black", cursor="hand2", command=self.delete)
        self.btn_delete.place(x=315, y=590, width=110, height=40)
        self.btn_clear = Button(self.root, text="Clear", font=("montserrat", 15, 'bold'), bg="#6C757D", fg="white", cursor="hand2", command=self.clear)
        self.btn_clear.place(x=465, y=590, width=110, height=40)

        # Search Panel
        self.var_search = StringVar()
        lbl_search_courseName = Label(self.root, text="Course Name:", font=("montserrat", 15, 'bold'), bg="white").place(x=690, y=70)
        txt_search_courseName = Entry(self.root, textvariable=self.var_search, font=("montserrat", 15, 'bold'), bg="#C6E2FF").place(x=870, y=70, width=200)

        btn_search = Button(self.root, text="Search", font=("montserrat", 12, 'bold'), bg="#0C1C47", fg="white", cursor="hand2", command=self.search).place(x=1100, y=70, width=120, height=30)

        # Content
        self.C_Frame = Frame(self.root, bd=10, relief=RIDGE)
        self.C_Frame.place(x=610, y=130, width=670, height=500)

        # Scrollbar
        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("cid", "name", "duration", "charges", "description"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("cid", text="Course ID")
        self.CourseTable.heading("name", text="Name")
        self.CourseTable.heading("duration", text="Duration")
        self.CourseTable.heading("charges", text="Charges")
        self.CourseTable.heading("description", text="Description")

        self.CourseTable["show"] = 'headings'

        self.CourseTable.column("cid", width=100)
        self.CourseTable.column("name", width=100)
        self.CourseTable.column("duration", width=100)
        self.CourseTable.column("charges", width=100)
        self.CourseTable.column("description", width=100)

        self.CourseTable.pack(fill=BOTH, expand=1)

        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()


        # Footer
        footer = Label(self.root, text="Student Management System | GUJJU infotech | Contact Us: 7874273210",
                       font=("montserrat", 13),  bg="#0C1C47", fg="white")
        footer.pack(side=BOTTOM, fill=X)
        
        # # Footer
        # footer = Label(self.root, text="SMS - Student Management System", font=("montserrat", 12), bg="#232323", fg="white").pack(side=BOTTOM, fill=X)
        # title.place(x=0, y=0, relwidth=1, height=50)

    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete('1.0', END)
        self.txt_courseName.config(state=NORMAL)

    def delete(self):
        con = mysql.connector.connect(host="localhost", user="root", password=DB_PASSWORD, database="sms")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM course WHERE name=%s", (self.var_course.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Please select course from the list first", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op:
                        cur.execute("DELETE FROM course WHERE name=%s", (self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Course Deleted Successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

    def get_data(self, ev):
        self.txt_courseName.config(state="readonly")
        r = self.CourseTable.focus()
        content = self.CourseTable.item(r)
        row = content["values"]
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.txt_description.delete('1.0', END)
        self.txt_description.insert(END, row[4])

    def add(self):
        con = mysql.connector.connect(host="localhost", user="root", password=DB_PASSWORD, database="sms")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM course WHERE name=%s", (self.var_course.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Course name already present", parent=self.root)
                else:
                    cur.execute("INSERT INTO course (name, duration, charges, description) VALUES (%s, %s, %s, %s)", (
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0", END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Course Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

    def search(self):
        con = mysql.connector.connect(host="localhost", user="root", password=DB_PASSWORD, database="sms")
        cur = con.cursor()
        try:
            cur.execute(f"SELECT * FROM course WHERE name LIKE '%{self.var_search.get()}%'")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

    def show(self):
        con = mysql.connector.connect(host="localhost", user="root", password=DB_PASSWORD, database="sms")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM course")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

    def update(self):
        con = mysql.connector.connect(host="localhost", user="root", password=DB_PASSWORD, database="sms")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM course WHERE name=%s", (self.var_course.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Select Course from list", parent=self.root)
                else:
                    cur.execute("UPDATE course SET duration=%s, charges=%s, description=%s WHERE name=%s", (
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0", END),
                        self.var_course.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Course Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()


# import mysql.connector
# from tkinter import *
# from PIL import Image, ImageTk, ImageSequence
# from tkinter import ttk, messagebox

# class CourseClass:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Student Management System")
#         self.root.config(bg="white")
#         self.root.update_idletasks()
#         self.center_window()
#         self.root.focus_force()
        
#         # Database Connection
#         self.con = mysql.connector.connect(host="localhost", user="root", password="Ashish@0629", database="sms")
#         self.cur = self.con.cursor()
        
#         # Title
#         title = Label(self.root, text="Manage Course Details", padx=10, compound=LEFT, font=("montserrat", 20, "bold"), bg="#232323", fg="white")
#         title.place(x=0, y=0, relwidth=1, height=50)
        
#         # Variables
#         self.var_course = StringVar()
#         self.var_duration = StringVar()
#         self.var_charges = StringVar()
#         self.var_search = StringVar()
        
#         # Widgets
#         Label(self.root, text="Course Name:", font=("montserrat", 15, 'bold'), bg="white").place(x=10, y=70)
#         Label(self.root, text="Duration:", font=("montserrat", 15, 'bold'), bg="white").place(x=10, y=130)
#         Label(self.root, text="Charges:", font=("montserrat", 15, 'bold'), bg="white").place(x=10, y=190)
#         Label(self.root, text="Description:", font=("montserrat", 15, 'bold'), bg="white").place(x=10, y=250)
        
#         self.txt_courseName = Entry(self.root, textvariable=self.var_course, font=("montserrat", 15, 'bold'), bg="#ffcbd1")
#         self.txt_courseName.place(x=180, y=70, width=200)
#         Entry(self.root, textvariable=self.var_duration, font=("montserrat", 15, 'bold'), bg="#ffcbd1").place(x=180, y=130, width=200)
#         Entry(self.root, textvariable=self.var_charges, font=("montserrat", 15, 'bold'), bg="#ffcbd1").place(x=180, y=190, width=200)
        
#         self.txt_description = Text(self.root, font=("montserrat", 15, 'bold'), bg="#ffcbd1")
#         self.txt_description.place(x=180, y=250, width=500, height=150)
        
#         # Buttons
#         Button(self.root, text="Save", font=("montserrat", 15, 'bold'), bg="#28A745", fg="white", cursor="hand2", command=self.add).place(x=180, y=590, width=110, height=40)
#         Button(self.root, text="Update", font=("montserrat", 15, 'bold'), bg="#007BFF", fg="black", cursor="hand2", command=self.update).place(x=310, y=590, width=110, height=40)
#         Button(self.root, text="Delete", font=("montserrat", 15, 'bold'), bg="#DC3545", fg="black", cursor="hand2", command=self.delete).place(x=440, y=590, width=110, height=40)
#         Button(self.root, text="Clear", font=("montserrat", 15, 'bold'), bg="#6C757D", fg="white", cursor="hand2", command=self.clear).place(x=570, y=590, width=110, height=40)
        
#         # Search Panel
#         Label(self.root, text="Course Name:", font=("montserrat", 15, 'bold'), bg="white").place(x=750, y=70)
#         Entry(self.root, textvariable=self.var_search, font=("montserrat", 15, 'bold'), bg="#ffcbd1").place(x=930, y=70, width=350)
#         Button(self.root, text="Search", font=("montserrat", 12, 'bold'), bg="#17A2B8", fg="black", cursor="hand2", command=self.search).place(x=1305, y=70, width=120, height=30)
        
#         # Content
#         self.C_Frame = Frame(self.root, bd=10, relief=RIDGE)
#         self.C_Frame.place(x=755, y=130, width=670, height=500)
        
#         scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
#         scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        
#         self.CourseTable = ttk.Treeview(self.C_Frame, columns=("cid", "name", "duration", "charges", "description"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
#         scrollx.pack(side=BOTTOM, fill=X)
#         scrolly.pack(side=RIGHT, fill=Y)
#         scrollx.config(command=self.CourseTable.xview)
#         scrolly.config(command=self.CourseTable.yview)
        
#         self.CourseTable.heading("cid", text="Course ID")
#         self.CourseTable.heading("name", text="Name")
#         self.CourseTable.heading("duration", text="Duration")
#         self.CourseTable.heading("charges", text="Charges")
#         self.CourseTable.heading("description", text="Description")
#         self.CourseTable["show"] = 'headings'
#         self.CourseTable.pack(fill=BOTH, expand=1)
#         self.CourseTable.bind("<ButtonRelease-1>", self.get_data)
#         self.show()
        
#         # Footer
#         footer = Label(self.root, text="SMS - Student Management System", font=("montserrat", 12), bg="#232323", fg="white").pack(side=BOTTOM, fill=X)
#         title.place(x=0, y=0, relwidth=1, height=50)
        
    
#     def clear(self):
#         self.show()
#         self.var_course.set("")
#         self.var_duration.set("")
#         self.var_charges.set("")
#         self.var_search.set("")
#         self.txt_description.delete('1.0',END)
#         self.txt_courseName.config(state=NORMAL)
    
        
#     def add(self):
#         self.cur.execute("INSERT INTO course (name, duration, charges, description) VALUES (%s, %s, %s, %s)",
#                         (self.var_course.get(), self.var_duration.get(), self.var_charges.get(), self.txt_description.get("1.0", END)))
#         self.con.commit()
#         messagebox.showinfo("Success", "Course Added Successfully", parent=self.root)
#         self.show()
        
#     def get_data(self,ev):
#         self.txt_courseName.config(state="readonly")
#         self.txt_courseName
#         r=self.CourseTable.focus()
#         content=self.CourseTable.item(r)
#         row=content["values"]
#         # print(row)
#         self.var_course.set(row[1])
#         self.var_duration.set(row[2])
#         self.var_charges.set(row[3])
#         # self.var_description.set(row[4])
#         self.txt_description.delete('1.0',END)
#         self.txt_description.insert(END,row[4])
        


#     def update(self):
#         self.cur.execute("UPDATE course SET duration=%s, charges=%s, description=%s WHERE name=%s",
#                         (self.var_duration.get(), self.var_charges.get(), self.txt_description.get("1.0", END), self.var_course.get()))
#         self.con.commit()
#         messagebox.showinfo("Success", "Course Updated Successfully", parent=self.root)
#         self.show()

#     def delete(self):
#         self.cur.execute("DELETE FROM course WHERE name=%s", (self.var_course.get(),))
#         self.con.commit()
#         messagebox.showinfo("Success", "Course Deleted Successfully", parent=self.root)
#         self.show()

#     def search(self):
#         self.cur.execute("SELECT * FROM course WHERE name LIKE %s", (f"%{self.var_search.get()}%",))
#         rows = self.cur.fetchall()
#         self.CourseTable.delete(*self.CourseTable.get_children())
#         for row in rows:
#             self.CourseTable.insert('', END, values=row)
        
#     def show(self):
#         self.cur.execute("SELECT * FROM course")
#         rows = self.cur.fetchall()
#         self.CourseTable.delete(*self.CourseTable.get_children())
#         for row in rows:
#             self.CourseTable.insert('', END, values=row)
        
#     def center_window(self, width=1450, height=700):
#         screen_width = self.root.winfo_screenwidth()
#         screen_height = self.root.winfo_screenheight()
#         x_position = (screen_width // 2) - (width // 2)
#         y_position = (screen_height // 2) - (height // 2)
#         self.root.geometry(f"{width}x{height}+{x_position}+{y_position}")

# if __name__ == "__main__":
#     root = Tk()
#     obj = CourseClass(root)
#     root.mainloop()

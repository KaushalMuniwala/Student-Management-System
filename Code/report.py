# import mysql.connector
# from tkinter import *
# from PIL import Image, ImageTk, ImageSequence
# from tkinter import ttk,messagebox
# import sqlite3

# class reportClass:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Student Management System")
#         self.root.config(bg="white")
#         self.root.update_idletasks()  # Ensure Tkinter initializes before setting geometry
#         self.center_window()
#         self.root.focus_force()
        
#         # Title
#         title = Label(self.root, text="View Student Results", padx=10, compound=LEFT,font=("montserrat", 20, "bold"), bg="#232323", fg="white")
#         title.place(x=0, y=0, relwidth=1, height=50)
        
        
#         # Search
#         self.var_search=StringVar()
#         lbl_search=Label(self.root,text="Search By Roll Number:",font=("montserrat",20,"bold"),bg="white").place(x=250,y=100)
#         txt_search=Entry(self.root,textvariable=self.var_search,font=("montserrat",20,),bg="#ffcbd1").place(x=620,y=100,width=250)

#         btn_search = Button(self.root, text="Search", font=("montserrat", 15, 'bold'), bg="#17A2B8", fg="black", cursor="hand2").place(x=900, y=100, width=120, height=40)
#         btn_clear=Button(self.root,text="Clear",font=("montserrat",15),bg="red",fg="white",activebackground="red",cursor="hand2").place(x=1050,y=100,width=120,height=40)
        
        
        
        
#         # Footer
#         footer = Label(self.root, text="SMS - Student Management System",font=("montserrat", 12), bg="#232323", fg="white").pack(side=BOTTOM,fill=X)
#         title.place(x=0, y=0, relwidth=1, height=50)
      
      
      
      
      
      
      
        
#     def center_window(self, width=1450, height=700):
#         screen_width = self.root.winfo_screenwidth()
#         screen_height = self.root.winfo_screenheight()
#         x_position = (screen_width // 2) - (width // 2)
#         y_position = (screen_height // 2) - (height // 2)
#         self.root.geometry(f"{width}x{height}+{x_position}+{y_position}")

# if __name__ == "__main__":
#     root = Tk()
#     obj = reportClass(root)
#     root.mainloop()


import mysql.connector
import csv
import os
from tkinter import *
from tkinter import ttk, messagebox

DB_PASSWORD = os.getenv("SMS_DB_PASSWORD", "root")

class ReportClass:
    def __init__(self, root):
        self.root = root
        self.root.title("View Result Report")
        self.root.update_idletasks()  # Ensure Tkinter initializes before setting geometry
        self.root.config(bg="white")
        # self.center_window()
        self.root.geometry("1295x735+233+50")  # Example: Width=1350, Height=800, X=100, Y=50
        self.root.focus_force()

        # Title
        title = Label(self.root, text="Student Result Report", font=("montserrat", 20, "bold"), bg="#0C1C47", fg="white")
        title.pack(side=TOP, fill=X)

        # Search Bar
        self.var_search = StringVar()
        lbl_search = Label(self.root, text="Search Roll No:", font=("montserrat", 18, "bold"), bg="white").place(x=70, y=80)
        txt_search = Entry(self.root, textvariable=self.var_search, font=("montserrat", 20), bg="#C6E2FF").place(x=300, y=80, width=200)
        btn_search = Button(self.root, text="Search", font=("montserrat", 12), bg="#0C1C47", fg="white", command=self.search).place(x=570, y=80, width=100)
        btn_show_all = Button(self.root, text="Show All", font=("montserrat", 12), bg="#0C1C47", fg="white", command=self.fetch_data).place(x=730, y=80, width=100)
        btn_export = Button(self.root, text="Generate Report", font=("montserrat", 12), bg="green", fg="white", command=self.export_report).place(x=1050, y=80, width=180)

        # Result Table
        frame = Frame(self.root, bd=2, relief=RIDGE)
        frame.place(x=20, y=140, width=1250, height=540)

        scroll_x = Scrollbar(frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(frame, orient=VERTICAL)

        self.result_table = ttk.Treeview(frame, columns=("roll", "name", "course", "marks_ob", "full_marks", "per"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.result_table.xview)
        scroll_y.config(command=self.result_table.yview)

        self.result_table.heading("roll", text="Roll No")
        self.result_table.heading("name", text="Name")
        self.result_table.heading("course", text="Course")
        self.result_table.heading("marks_ob", text="Marks Obtained")
        self.result_table.heading("full_marks", text="Full Marks")
        self.result_table.heading("per", text="Percentage")
        self.result_table["show"] = "headings"

        self.result_table.column("roll", width=100)
        self.result_table.column("name", width=150)
        self.result_table.column("course", width=100)
        self.result_table.column("marks_ob", width=100)
        self.result_table.column("full_marks", width=100)
        self.result_table.column("per", width=100)

        self.result_table.pack(fill=BOTH, expand=1)
        self.result_table.bind("<ButtonRelease-1>", self.get_cursor)

        # Delete Button
        btn_delete = Button(self.root, text="Delete", font=("montserrat", 12), bg="red", fg="white", command=self.delete_data).place(x=890, y=80, width=100)

        self.fetch_data()

        # Footer
        footer = Label(self.root, text="Student Management System | GUJJU infotech | Contact Us: 7874273210",
                       font=("montserrat", 13),  bg="#0C1C47", fg="white")
        footer.pack(side=BOTTOM, fill=X)

    def fetch_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password=DB_PASSWORD, database="sms")
        cur = con.cursor()
        cur.execute("SELECT roll, name, course, marks_ob, full_marks, per FROM result")
        rows = cur.fetchall()
        self.result_table.delete(*self.result_table.get_children())
        for row in rows:
            self.result_table.insert("", END, values=row)
        con.close()

    def search(self):
        con = mysql.connector.connect(host="localhost", user="root", password=DB_PASSWORD, database="sms")
        cur = con.cursor()
        cur.execute("SELECT roll, name, course, marks_ob, full_marks, per FROM result WHERE roll=%s", (self.var_search.get(),))
        row = cur.fetchone()
        if row:
            self.result_table.delete(*self.result_table.get_children())
            self.result_table.insert("", END, values=row)
        else:
            messagebox.showerror("Error", "No record found")
        con.close()

    def get_cursor(self, event):
        cursor_row = self.result_table.focus()
        contents = self.result_table.item(cursor_row)
        row = contents['values']
        self.var_search.set(row[0])

    def delete_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password=DB_PASSWORD, database="sms")
        cur = con.cursor()
        cur.execute("DELETE FROM result WHERE roll=%s", (self.var_search.get(),))
        con.commit()
        messagebox.showinfo("Success", "Record Deleted Successfully")
        self.fetch_data()
        con.close()

    def export_report(self):
        con = mysql.connector.connect(host="localhost", user="root", password=DB_PASSWORD, database="sms")
        cur = con.cursor()
        cur.execute("SELECT roll, name, course, marks_ob, full_marks, per FROM result")
        rows = cur.fetchall()
        con.close()
        if rows:
            with open("student_results.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Roll No", "Name", "Course", "Marks Obtained", "Full Marks", "Percentage"])
                writer.writerows(rows)
            messagebox.showinfo("Success", "Report generated as 'student_results.csv'")
        else:
            messagebox.showerror("Error", "No data available to export")

    def center_window(self, width=1450, height=700):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_position = (screen_width // 2) - (width // 2)
        y_position = (screen_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x_position}+{y_position}")

if __name__ == "__main__":
    root = Tk()
    obj = ReportClass(root)
    root.mainloop()


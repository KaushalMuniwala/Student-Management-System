# from tkinter import *
# from PIL import Image, ImageTk, ImageSequence
# from course import CourseClass
# from student import studentClass
# from result import resultClass
# from report import ReportClass
# from register import Register
# from login import Login
# from tkinter import Toplevel

# class SMS:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Student Management System")
#         self.root.geometry("1520x785+0+0")
#         self.root.config(bg="white")

#         # Icone
#         self.logo_dash=ImageTk.PhotoImage(Image.open("D:/Ashish khadela/Master/SEM_2/PYTHON/Mini_Project/SMS/Code/img/logo.png").resize((175,120),Image.Resampling.LANCZOS))

#         # Title
#         title = Label(self.root, text="Student Management System", padx=10, compound=LEFT,image=self.logo_dash,font=("montserrat", 20, "bold"), bg="#ff2c2c", fg="black")
#         title.place(x=0, y=0, relwidth=1, height=50)

#         # Menu
#         M_Frame=LabelFrame(self.root,text="Menu",font=("montserrat",15),bg="white")
#         M_Frame.place(x=10,y=50,width=1500,height=85)

#         btn_course=Button(M_Frame,text="Course",font=("montserrat",15,"bold"),bg="#232323",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=235,height=40)
#         btn_student=Button(M_Frame,text="Student",font=("montserrat",15,"bold"),bg="#232323",fg="white",cursor="hand2",command=self.add_student).place(x=265,y=5,width=235,height=40)
#         btn_result=Button(M_Frame,text="Result",font=("montserrat",15,"bold"),bg="#232323",fg="white",cursor="hand2",command=self.add_result).place(x=510,y=5,width=235,height=40)
#         btn_view=Button(M_Frame,text="View Student Result",font=("montserrat",15,"bold"),bg="#232323",fg="white",cursor="hand2",command=self.add_report).place(x=755,y=5,width=235,height=40)
#         btn_logout=Button(M_Frame,text="Logout",font=("montserrat",15,"bold"),bg="#232323",fg="white",cursor="hand2").place(x=1000,y=5,width=235,height=40)
#         btn_exit=Button(M_Frame,text="Exit",font=("montserrat",15,"bold"),bg="#232323",fg="white",cursor="hand2").place(x=1245,y=5,width=235,height=40)

#         # Content Window
#         self.bg_img = Image.open("D:/Ashish khadela/Master/SEM_2/PYTHON/Mini_Project/SMS/Code/img/background.png")
#         self.bg_img = self.bg_img.resize((1000, 400), Image.Resampling.LANCZOS)
#         self.bg_img = ImageTk.PhotoImage(self.bg_img)

#         self.lbl_bg = Label(self.root, image=self.bg_img)
#         self.lbl_bg.place(x=400, y=150, width=1110, height=455)

#         # Update
#         self.lbl_course=Label(self.root,text="Total Courses\n[ 0 ]",font=("montserrat",20),bd=10,relief=RIDGE,bg="#232323",fg="white")
#         self.lbl_course.place(x=400,y=620,width=300,height=100)

#         self.lbl_student=Label(self.root,text="Total Students\n[ 0 ]",font=("montserrat",20),bd=10,relief=RIDGE,bg="#6ca0dc",fg="black")
#         self.lbl_student.place(x=805,y=620,width=300,height=100)

#         self.lbl_result=Label(self.root,text="Total Results\n[ 0 ]",font=("montserrat",20),bd=10,relief=RIDGE,bg="#232323",fg="white")
#         self.lbl_result.place(x=1210,y=620,width=300,height=100)

#         # Footer
#         footer = Label(self.root, text="SMS - Student Management System\nContact Us for any Technical Issue: 9723835434",font=("montserrat", 12), bg="#ff2c2c", fg="black").pack(side=BOTTOM,fill=X)
#         title.place(x=0, y=0, relwidth=1, height=50)
        

#     def add_course(self):
#         self.new_win=Toplevel(self.root)    
#         self.new_obj=CourseClass(self.new_win)

#     def add_student(self):
#         self.new_win=Toplevel(self.root)    
#         self.new_obj=studentClass(self.new_win)

#     def add_result(self):
#         self.new_win=Toplevel(self.root)    
#         self.new_obj=resultClass(self.new_win)

#     def add_report(self):
#         self.new_win=Toplevel(self.root)    
#         self.new_obj=ReportClass(self.new_win)
        
#     def add_register(self):
#         self.new_win=Toplevel(self.root)    
#         self.new_obj=Register(self.new_win)
        
#     def add_login(self):
#         self.new_win=Toplevel(self.root)    
#         self.new_obj=Login(self.new_win)

#     def logout(self):
#         self.root.destroy()  # Close the dashboard window
#         from login import Login  # Import login module
#         Login(Tk())  # Open login window again

# if __name__ == "__main__":
#     root = Tk()
#     obj = SMS(root)
#     root.mainloop()

# from tkinter import *
# from PIL import Image, ImageTk
# from course import CourseClass
# from student import studentClass
# from result import resultClass
# from report import ReportClass
# from tkinter import messagebox
# import os
# import mysql.connector

# class SMS:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Student Management System")
#         self.root.geometry("1520x785+0+0")
#         self.root.config(bg="white")

#         print("Initializing Dashboard UI...")  # Debugging

#         # Image Paths
#         logo_path = "D:/Ashish khadela/Master/SEM_2/PYTHON/Mini_Project/SMS/Code/img/logo.png"
#         bg_path = "D:/Ashish khadela/Master/SEM_2/PYTHON/Mini_Project/SMS/Code/img/background.png"

#         # Load Logo Image
#         if os.path.exists(logo_path):
#             self.logo_dash = ImageTk.PhotoImage(Image.open(logo_path).resize((175, 120), Image.Resampling.LANCZOS))
#         else:
#             print("Error: Logo image not found!")
#             self.logo_dash = None  # Prevent crash

#         # Load Background Image
#         if os.path.exists(bg_path):
#             self.bg_img = Image.open(bg_path)
#             self.bg_img = self.bg_img.resize((1000, 400), Image.Resampling.LANCZOS)
#             self.bg_img = ImageTk.PhotoImage(self.bg_img)
#         else:
#             print("Error: Background image not found!")
#             self.bg_img = None

#         # Title Bar
#         title = Label(self.root, text="Student Management System", padx=10, compound=LEFT,
#                       image=self.logo_dash if self.logo_dash else None, 
#                       font=("montserrat", 20, "bold"), bg="#ff2c2c", fg="black")
#         title.place(x=0, y=0, relwidth=1, height=50)

#         # Menu Frame
#         M_Frame = LabelFrame(self.root, text="Menu", font=("montserrat", 15), bg="white")
#         M_Frame.place(x=10, y=50, width=1500, height=85)

#         # Menu Buttons
#         btn_course = Button(M_Frame, text="Course", font=("montserrat", 15, "bold"), bg="#232323", fg="white", cursor="hand2", command=self.add_course)
#         btn_course.place(x=20, y=5, width=235, height=40)

#         btn_student = Button(M_Frame, text="Student", font=("montserrat", 15, "bold"), bg="#232323", fg="white", cursor="hand2", command=self.add_student)
#         btn_student.place(x=265, y=5, width=235, height=40)

#         btn_result = Button(M_Frame, text="Result", font=("montserrat", 15, "bold"), bg="#232323", fg="white", cursor="hand2", command=self.add_result)
#         btn_result.place(x=510, y=5, width=235, height=40)

#         btn_view = Button(M_Frame, text="View Student Result", font=("montserrat", 15, "bold"), bg="#232323", fg="white", cursor="hand2", command=self.add_report)
#         btn_view.place(x=755, y=5, width=235, height=40)

#         btn_logout = Button(M_Frame, text="Logout", font=("montserrat", 15, "bold"), bg="#232323", fg="white", cursor="hand2", command=self.logout)
#         btn_logout.place(x=1000, y=5, width=235, height=40)

#         btn_exit = Button(M_Frame, text="Exit", font=("montserrat", 15, "bold"), bg="#232323", fg="white", cursor="hand2", command=self.exit_app)
#         btn_exit.place(x=1245, y=5, width=235, height=40)

#         # Content Area
#         if self.bg_img:
#             self.lbl_bg = Label(self.root, image=self.bg_img)
#             self.lbl_bg.place(x=400, y=150, width=1110, height=455)
#         else:
#             print("Skipping background image due to missing file.")

#         # Update Stats
#         self.lbl_course = Label(self.root, text="Total Courses\n[ 0 ]", font=("montserrat", 20), bd=10, relief=RIDGE, bg="#232323", fg="white")
#         self.lbl_course.place(x=400, y=620, width=300, height=100)

#         self.lbl_student = Label(self.root, text="Total Students\n[ 0 ]", font=("montserrat", 20), bd=10, relief=RIDGE, bg="#6ca0dc", fg="black")
#         self.lbl_student.place(x=805, y=620, width=300, height=100)

#         self.lbl_result = Label(self.root, text="Total Results\n[ 0 ]", font=("montserrat", 20), bd=10, relief=RIDGE, bg="#232323", fg="white")
#         self.lbl_result.place(x=1210, y=620, width=300, height=100)

#         # Footer
#         footer = Label(self.root, text="SMS - Student Management System\nContact Us for any Technical Issue: 9723835434",
#                        font=("montserrat", 12), bg="#ff2c2c", fg="black")
#         footer.pack(side=BOTTOM, fill=X)

#         self.update_details()
        
#         # Force UI Refresh
#         self.root.update_idletasks()
#         self.root.update()

#     def update_details(self):
#         con = mysql.connector.connect(host="localhost", user="root", password="Ashish@0629", database="sms")
#         cur = con.cursor()
#         try:
#             cur.execute("SELECT * FROM course")
#             cr = cur.fetchall()
#             self.lbl_course.config(text=f"Total Courses\n[ {str(len(cr))} ]")
            
#             cur.execute("SELECT * FROM student")
#             cr = cur.fetchall()
#             self.lbl_student.config(text=f"Total Students\n[ {str(len(cr))} ]")
            
#             cur.execute("SELECT * FROM result")
#             cr = cur.fetchall()
#             self.lbl_result.config(text=f"Total Results\n[ {str(len(cr))} ]")
            
#             self.lbl_course.after(200,self.update_details)
            
#         except Exception as ex:
#             messagebox.showerror("Error", f"Error due to {str(ex)}")
#         finally:
#             con.close()

#     # Navigation Functions
#     def add_course(self):
#         from course import CourseClass
#         self.new_win = Toplevel(self.root)
#         self.new_obj = CourseClass(self.new_win)

#     def add_student(self):
#         from student import studentClass
#         self.new_win = Toplevel(self.root)
#         self.new_obj = studentClass(self.new_win)

#     def add_result(self):
#         from result import resultClass
#         self.new_win = Toplevel(self.root)
#         self.new_obj = resultClass(self.new_win)

#     def add_report(self):
#         from report import ReportClass
#         self.new_win = Toplevel(self.root)
#         self.new_obj = ReportClass(self.new_win)

#     def logout(self):
#         op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
#         if op==True:
#             self.root.destroy()  # Close Dashboard
#             from login import Login
#             root = Tk()
#             obj = Login(root)
#             root.mainloop()

#     def exit_app(self):
#         op=messagebox.askyesno("Confirm","Do you really want to Exit?",parent=self.root)
#         if op==True:
#             self.root.destroy()

# # Run Application
# if __name__ == "__main__":
#     root = Tk()
#     obj = SMS(root)
#     print("Dashboard is running...")  # Debugging
#     root.mainloop()



from tkinter import *
from PIL import Image, ImageTk
from course import CourseClass
from student import studentClass
from result import resultClass
from report import ReportClass
from attendance import AttendanceClass
from tkinter import messagebox
import os
import mysql.connector

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "img")
DB_PASSWORD = os.getenv("SMS_DB_PASSWORD", "root")


def image_path(filename):
    return os.path.join(IMG_DIR, filename)

class SMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        # self.root.geometry("1520x785+0+0")
        self.root.config(bg="white")

        print("Initializing Dashboard UI...")  # Debugging
        
    # Sidebar Frame
        sidebar_width = int(screen_width * 0.15)
        sidebar_height = screen_height
        
        self.sidebar_frame = Frame(self.root, bg="#C6E2FF", width=sidebar_width, height=sidebar_height)
        self.sidebar_frame.place(x=0, y=0, width=sidebar_width, height=sidebar_height)
        
        # Logo inside Sidebar
        logo_size = int(sidebar_width * 1)
        logo = Image.open(image_path("1.png"))
        logo = logo.resize((logo_size, logo_size))
        self.logo_dash = ImageTk.PhotoImage(logo)
        
        logo_label = Label(self.sidebar_frame, image=self.logo_dash, bg="#C6E2FF")
        logo_label.pack(pady=0*2)
        
        # Sidebar Buttons
        button_style = {"font": ("montserrat", 13, "bold"), "bg": "#0C1C47", "cursor": "hand2", "fg": "white", "width": 15, "height": 2}
        
        btn_course = Button(self.sidebar_frame, text="Course", command=self.add_course, **button_style)
        btn_course.pack(pady=10)
        
        btn_student = Button(self.sidebar_frame, text="Student", command=self.add_student, **button_style)
        btn_student.pack(pady=10)
        
        btn_result = Button(self.sidebar_frame, text="Result" , command=self.add_result, **button_style)
        btn_result.pack(pady=10)
        
        btn_viewResult = Button(self.sidebar_frame, text="View Result",command=self.view_result, **button_style)
        btn_viewResult.pack(pady=10)
        
        btn_attendance = Button(self.sidebar_frame, text="Attendance", command=self.add_attandance, **button_style)
        btn_attendance.pack(pady=10)
        
        btn_logout = Button(self.sidebar_frame, text="Logout",command=self.logout, **button_style)
        btn_logout.pack(pady=10)

        # Main Content Area
        main_area = Frame(self.root, bg="#F5F5F5")
        main_area.place(x=sidebar_width + 10, y=10, width=screen_width - sidebar_width - 20, height=screen_height - 50)
                                            
        welcome_label = Label(main_area, text="WELCOME TO THE STUDENT MANAGEMENT SYSTEM", font=("montserrat", 25, "bold"), bg="#F5F5F5", fg="#0C1C47")
        welcome_label.pack(pady=10)  # Added some padding

        # Background Image
        bg_img = Image.open(image_path("bg4.png"))
        bg_img = bg_img.resize((screen_width - sidebar_width - 20, int(screen_height * 0.6)))  # Adjusted height
        self.bg_img = ImageTk.PhotoImage(bg_img)
        lbl_bg = Label(main_area, image=self.bg_img, bg="#F5F5F5")
        lbl_bg.pack(side=TOP, anchor="center", pady=10)  # Added some space

        # Info Boxes (Bottom)
        info_frame = Frame(main_area, bg="#F5F5F5")
        info_frame.pack(side=TOP, fill=X, pady=10)  # Adjusted positioning and spacing
        
        box_style = {"font": ("montserrat", 18), "bd": 5, "relief": RIDGE, "width": 25, "height": 3}  # Increased width
        
      # Initialize labels with placeholders
        self.lbl_course = Label(info_frame, text="Total Courses\n[ ]", bg="#C6E2FF", fg="black", **box_style)
        self.lbl_course.grid(row=0, column=0, padx=10, pady=5)
        
        self.lbl_student = Label(info_frame, text="Total Students\n[ ]", bg="#0C1C47", fg="white", **box_style)
        self.lbl_student.grid(row=0, column=1, padx=10, pady=5)
        
        self.lbl_result = Label(info_frame, text="Total Results\n[ ]", bg="#C6E2FF", fg="black", **box_style)
        self.lbl_result.grid(row=0, column=2, padx=10, pady=5)
        
        self.update_details()
        
        # Footer
        footer = Label(self.root, text="Student Management System | GUJJU infotech | Contact Us: 7874273210",
                       font=("montserrat", 13),  bg="#0C1C47", fg="white")
        footer.pack(side=BOTTOM, fill=X)
        

    def update_details(self):
        con = mysql.connector.connect(host="localhost", user="root", password=DB_PASSWORD, database="sms")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM course")
            cr = cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[ {str(len(cr))} ]")
            
            cur.execute("SELECT * FROM student")
            cr = cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[ {str(len(cr))} ]")
            
            cur.execute("SELECT * FROM result")
            cr = cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[ {str(len(cr))} ]")
            
            self.lbl_course.after(200,self.update_details)
            
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

    # Navigation Functions
    def add_course(self):
        from course import CourseClass
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        from student import studentClass
        self.new_win = Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)

    def add_result(self):
        from result import resultClass
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)

    def view_result(self):
        from report import ReportClass
        self.new_win = Toplevel(self.root)
        self.new_obj = ReportClass(self.new_win)
        
    def add_attandance(self):
        from attendance import AttendanceClass
        self.new_win = Toplevel(self.root)    
        self.new_obj = AttendanceClass(self.new_win)

    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()  # Close Dashboard
            from login import Login
            root = Tk()
            obj = Login(root)
            root.mainloop()

# Run Application
if __name__ == "__main__":
    root = Tk()
    obj = SMS(root)
    print("Dashboard is running...")  # Debugging
    root.mainloop()
import mysql.connector
from tkinter import *
from tkinter import ttk, messagebox
import os
from datetime import datetime
import csv
from tkinter import filedialog

try:
    from tkcalendar import DateEntry
except ModuleNotFoundError:
    DateEntry = None

DB_PASSWORD = os.getenv("SMS_DB_PASSWORD", "root")

class AttendanceClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Management System")
        self.root.config(bg="#F5F7FA")
        self.root.geometry("1295x735+233+50")  # Example: Width=1350, Height=800, X=100, Y=50
        self.root.update_idletasks()
        # self.center_window()
        self.root.focus_force()

         # Title
        title = Label(self.root, text="Manage Student Attendance", padx=10, compound=LEFT, font=("montserrat", 20, "bold"), bg="#0C1C47", fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)

        # Main Frame for Inputs
        input_frame = Frame(self.root, bg="#C6E2FF", relief=FLAT, bd=0)
        input_frame.place(x=20, y=70, width=1255, height=80)

        lbl_select_course = Label(input_frame, text="Select Course:", font=("montserrat", 14, "bold"), bg="#C6E2FF", fg="#0C1C47")
        lbl_select_course.place(x=50, y=25)
        self.var_course = StringVar()
        self.course_list = []
        self.txt_course = ttk.Combobox(input_frame, textvariable=self.var_course, values=self.course_list,
                                      font=("Helvetica", 12), state='readonly', justify=CENTER)
        self.txt_course.place(x=220, y=25, width=200, height=30)
        self.txt_course.set("Select")
        self.txt_course.bind("<<ComboboxSelected>>", self.update_student_list)

        
        lbl_date = Label(input_frame, text="Date:", font=("montserrat", 14, "bold"), bg="#C6E2FF", fg="#0C1C47")
        lbl_date.place(x=500, y=25)
        self.date = StringVar()
        if DateEntry is not None:
            self.cal = DateEntry(input_frame, textvariable=self.date, date_pattern='yyyy-mm-dd',
                                font=("Helvetica", 12), bg="#FFFFFF", fg="#333333", borderwidth=1)
        else:
            self.cal = Entry(input_frame, textvariable=self.date, font=("Helvetica", 12), bg="#FFFFFF", fg="#333333", borderwidth=1)
            self.date.set(datetime.today().strftime('%Y-%m-%d'))
        self.cal.place(x=580, y=25, width=200, height=30)

        self.btn_csv = Button(input_frame, text="Attendance Report", font=("montserrat", 12),
                     bg="#0C1C47", fg="white", activebackground="white", command=self.export_to_csv)
        self.btn_csv.place(x=1050, y=25, width=180, height=35)
        self.btn_csv.bind("<Enter>", lambda e: self.btn_csv.config(bg="black"))
        self.btn_csv.bind("<Leave>", lambda e: self.btn_csv.config(bg="#0C1C47"))

        # Frame for Student List with Table-Like Structure
        self.student_frame = Frame(self.root, bd=0, relief=FLAT, bg="#FFFFFF")
        self.student_frame.place(x=20, y=160, width=1255, height=450)

        # Header for Student List
        header_frame = Frame(self.student_frame, bg="#0C1C47", bd=0, relief=FLAT)
        header_frame.pack(fill=X)
        Label(header_frame, text="Roll", font=("montserrat", 12, "bold"), bg="#C6E2FF", fg="black", width=10).pack(side=LEFT, padx=10, pady=5)
        Label(header_frame, text="Name", font=("montserrat", 12, "bold"), bg="#C6E2FF", fg="black", width=15).pack(side=LEFT, padx=10, pady=5)
        Label(header_frame, text="Email", font=("montserrat", 12, "bold"), bg="#C6E2FF", fg="black", width=20).pack(side=LEFT, padx=10, pady=5)
        Label(header_frame, text="Gender", font=("montserrat", 12, "bold"), bg="#C6E2FF", fg="black", width=10).pack(side=LEFT, padx=10, pady=5)
        Label(header_frame, text="Status", font=("montserrat", 12, "bold"), bg="#C6E2FF", fg="black", width=60).pack(side=LEFT, padx=10, pady=5)

        # Canvas for Scrollable Student List
        self.canvas = Canvas(self.student_frame, bg="#FFFFFF")
        scrollbar = Scrollbar(self.student_frame, orient=VERTICAL, command=self.canvas.yview)
        self.inner_frame = Frame(self.canvas, bg="#FFFFFF")

        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")
        self.inner_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Fetch courses
        self.student_data = {}
        self.fetch_courses()

        # Button Frame
        button_frame = Frame(self.root, bg="#C6E2FF")
        button_frame.place(x=20, y=630, width=1255, height=50)

        self.btn_submit = Button(button_frame, text="Submit Attendance", font=("montserrat", 14, "bold"),
                                bg="green", fg="white", activebackground="#218838", activeforeground="white",
                                command=self.submit_attendance)
        self.btn_submit.place(x=20, y=5, width=230, height=40)
        self.btn_submit.bind("<Enter>", lambda e: self.btn_submit.config(bg="#218838"))
        self.btn_submit.bind("<Leave>", lambda e: self.btn_submit.config(bg="#28A745"))

        self.btn_clear = Button(button_frame, text="Clear", font=("montserrat", 14, "bold"),
                               bg="red", fg="white", activebackground="#C82333", activeforeground="white",
                               command=self.clear)
        self.btn_clear.place(x=280, y=5, width=200, height=40)
        self.btn_clear.bind("<Enter>", lambda e: self.btn_clear.config(bg="#C82333"))
        self.btn_clear.bind("<Leave>", lambda e: self.btn_clear.config(bg="#DC3545"))

        self.btn_all_present = Button(button_frame, text="All Present", font=("montserrat", 12),
                                     bg="#0C1C47", fg="white", activebackground="#138496", activeforeground="white",
                                     command=self.set_all_present)
        self.btn_all_present.place(x=510, y=5, width=120, height=40)
        self.btn_all_present.bind("<Enter>", lambda e: self.btn_all_present.config(bg="#138496"))
        self.btn_all_present.bind("<Leave>", lambda e: self.btn_all_present.config(bg="#17A2B8"))

        self.btn_all_absent = Button(button_frame, text="All Absent", font=("montserrat", 12),
                                    bg="#0C1C47", fg="white", activebackground="#E0A800", activeforeground="black",
                                    command=self.set_all_absent)
        self.btn_all_absent.place(x=660, y=5, width=120, height=40)
        self.btn_all_absent.bind("<Enter>", lambda e: self.btn_all_absent.config(bg="#E0A800"))
        self.btn_all_absent.bind("<Leave>", lambda e: self.btn_all_absent.config(bg="#FFC107"))

        # New "View Attendance" Button
        self.btn_view = Button(button_frame, text="View Attendance", font=("montserrat", 12),
                              bg="black", fg="white", activebackground="#5A6268", activeforeground="white",
                              command=self.view_attendance)
        self.btn_view.place(x=810, y=5, width=155, height=40)
        self.btn_view.bind("<Enter>", lambda e: self.btn_view.config(bg="#5A6268"))
        self.btn_view.bind("<Leave>", lambda e: self.btn_view.config(bg="#6C757D"))

        self.lbl_present = Label(button_frame, text="Present: 0", font=("montserrat", 14, "bold"), bg="#C6E2FF", fg="green")
        self.lbl_present.place(x=990, y=10)
        self.lbl_absent = Label(button_frame, text="Absent: 0", font=("montserrat", 14, "bold"), bg="#C6E2FF", fg="red")
        self.lbl_absent.place(x=1130, y=10)



        # Footer
        footer = Label(self.root, text="Student Management System | GUJJU infotech | Contact Us: 7874273210",
                       font=("montserrat", 13),  bg="#0C1C47", fg="white")
        footer.pack(side=BOTTOM, fill=X)
        
        
        
        
    def fetch_courses(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password=DB_PASSWORD,
            database="sms"
        )
        cur = con.cursor()
        try:
            self.course_list.clear()
            cur.execute("SELECT name FROM course")
            rows = cur.fetchall()
            print("Fetched courses:", rows)
            if len(rows) > 0:
                for row in rows:
                    self.course_list.append(row[0])
            self.txt_course['values'] = self.course_list
            if not self.course_list:
                messagebox.showwarning("Warning", "No courses found in the database. Please add courses first.")
        except mysql.connector.Error as ex:
            messagebox.showerror("Error", f"Error fetching courses: {str(ex)}")
        finally:
            con.close()

    def update_student_list(self, event):
        selected_course = self.var_course.get()
        print(f"Selected course: {selected_course}")
        if selected_course != "Select":
            self.inner_frame.destroy()
            self.inner_frame = Frame(self.canvas, bg="#FFFFFF")
            self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")
            self.inner_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

            con = mysql.connector.connect(
                host="localhost",
                user="root",
                password=DB_PASSWORD,
                database="sms"
            )
            cur = con.cursor()
            try:
                self.student_data.clear()
                cur.execute("SELECT roll, name, email, gender FROM student WHERE course = %s", (selected_course,))
                rows = cur.fetchall()
                print(f"Fetched students for {selected_course}: {rows}")
                if len(rows) > 0:
                    for idx, (roll, name, email, gender) in enumerate(rows):
                        self.student_data[roll] = {'name': name, 'email': email, 'gender': gender, 'status': StringVar(value='A')}
                        frame = Frame(self.inner_frame, bg="#FFFFFF" if idx % 2 == 0 else "#F5F5F5", bd=0, relief=FLAT)
                        frame.pack(fill=X, pady=10)
                        frame.bind("<Enter>", lambda e, f=frame: f.config(bg="#E0E0E0"))
                        frame.bind("<Leave>", lambda e, f=frame, i=idx: f.config(bg="#FFFFFF" if i % 2 == 0 else "#F5F5F5"))

                        Label(frame, text=str(roll), font=("montserrat", 12), bg=frame.cget("bg"), width=10).pack(side=LEFT, padx=10, pady=5)
                        Label(frame, text=name, font=("montserrat", 12), bg=frame.cget("bg"), width=18).pack(side=LEFT, padx=10, pady=5)
                        Label(frame, text=email, font=("montserrat", 12), bg=frame.cget("bg"), width=20).pack(side=LEFT, padx=10, pady=5)
                        Label(frame, text=gender, font=("montserrat", 12), bg=frame.cget("bg"), width=13).pack(side=LEFT, padx=10, pady=5)

                        status_frame = Frame(frame, bg=frame.cget("bg"), bd=0, relief=FLAT)
                        status_frame.pack(side=LEFT, padx=20, pady=5)

                        present_radio = Radiobutton(status_frame, text="Present", variable=self.student_data[roll]['status'], value='P',
                                                   font=("montserrat", 12, "bold"), bg=frame.cget("bg"), fg="green",
                                                   activebackground="#D4F1DE", activeforeground="#1E7E34",
                                                   selectcolor="#D4F1DE", indicatoron=1, width=18, padx=5, pady=5)
                        present_radio.pack(side=LEFT, padx=5)
                        present_radio.bind("<Enter>", lambda e, r=present_radio: r.config(bg="#D4F1DE"))
                        present_radio.bind("<Leave>", lambda e, r=present_radio, f=frame.cget("bg"): r.config(bg=f))

                        absent_radio = Radiobutton(status_frame, text="Absent", variable=self.student_data[roll]['status'], value='A',
                                                  font=("montserrat", 12, "bold"), bg=frame.cget("bg"), fg="red",
                                                  activebackground="#FAD2D2", activeforeground="#B02A37",
                                                  selectcolor="#FAD2D2", indicatoron=1, width=18, padx=5, pady=5)
                        absent_radio.pack(side=LEFT, padx=5)
                        absent_radio.bind("<Enter>", lambda e, r=absent_radio: r.config(bg="#FAD2D2"))
                        absent_radio.bind("<Leave>", lambda e, r=absent_radio, f=frame.cget("bg"): r.config(bg=f))
                else:
                    Label(self.inner_frame, text="No students enrolled in this course.", font=("Helvetica", 12), bg="#FFFFFF").pack(pady=10)

                if len(rows) < 5:
                    for _ in range(5 - len(rows)):
                        frame = Frame(self.inner_frame, bg="#FFFFFF", bd=0, relief=FLAT)
                        frame.pack(fill=X, pady=10)
                        Label(frame, text="", font=("Helvetica", 12), bg=frame.cget("bg"), width=10).pack(side=LEFT, padx=10, pady=5)
                        Label(frame, text="No more students", font=("Helvetica", 12), bg=frame.cget("bg"), width=15, fg="#6C757D").pack(side=LEFT, padx=10, pady=5)
                        Label(frame, text="", font=("Helvetica", 12), bg=frame.cget("bg"), width=20).pack(side=LEFT, padx=10, pady=5)
                        Label(frame, text="", font=("Helvetica", 12), bg=frame.cget("bg"), width=10).pack(side=LEFT, padx=10, pady=5)
                        status_frame = Frame(frame, bg=frame.cget("bg"), bd=0, relief=FLAT)
                        status_frame.pack(side=LEFT, padx=10, pady=5)

                self.canvas.config(height=300)
            except mysql.connector.Error as ex:
                messagebox.showerror("Error", f"Error fetching students: {str(ex)}")
            finally:
                con.close()
        else:
            self.inner_frame.destroy()
            self.inner_frame = Frame(self.canvas, bg="#FFFFFF")
            self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")
            self.inner_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
            Label(self.inner_frame, text="Please select a course.", font=("Helvetica", 12), bg="#FFFFFF").pack(pady=10)

    def set_all_present(self):
        for roll, data in self.student_data.items():
            data['status'].set('P')
        messagebox.showinfo("Success", "All students marked as Present.", parent=self.root)

    def set_all_absent(self):
        for roll, data in self.student_data.items():
            data['status'].set('A')
        messagebox.showinfo("Success", "All students marked as Absent.", parent=self.root)

    def submit_attendance(self):
        if self.var_course.get() == "Select":
            messagebox.showerror("Error", "Please select a course", parent=self.root)
            return
        try:
            datetime.strptime(self.date.get(), "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.", parent=self.root)
            return

        if not messagebox.askyesno("Confirm", "Are you sure you want to submit attendance?", parent=self.root):
            return

        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password=DB_PASSWORD,
            database="sms"
        )
        cur = con.cursor()
        try:
            cur.execute("SELECT cid FROM course WHERE name=%s", (self.var_course.get(),))
            course_id = cur.fetchone()
            if not course_id:
                messagebox.showerror("Error", "Invalid course", parent=self.root)
                return
            course_id = course_id[0]

            present_count = 0
            absent_count = 0
            for roll, data in self.student_data.items():
                status = data['status'].get()
                cur.execute("INSERT INTO attendance (roll, date, course, status) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE status=%s",
                           (roll, self.date.get(), course_id, status, status))
                if status == 'P':
                    present_count += 1
                else:
                    absent_count += 1

            con.commit()
            self.lbl_present.config(text=f"Present: {present_count}")
            self.lbl_absent.config(text=f"Absent: {absent_count}")
            messagebox.showinfo("Success", "Attendance Submitted Successfully", parent=self.root)
        except mysql.connector.Error as ex:
            messagebox.showerror("Error", f"Error submitting attendance: {str(ex)}")
        finally:
            con.close()

    def update_attendance_list(self, view_window):
        # Clear existing content
        for widget in self.attendance_inner_frame.winfo_children():
            widget.destroy()

        try:
            datetime.strptime(self.view_date.get(), "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.", parent=view_window)
            return

        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password=DB_PASSWORD,
            database="sms"
        )
        cur = con.cursor()
        try:
            cur.execute("SELECT cid FROM course WHERE name=%s", (self.var_course.get(),))
            course_id = cur.fetchone()
            if not course_id:
                messagebox.showerror("Error", "Invalid course", parent=view_window)
                view_window.destroy()
                return
            course_id = course_id[0]

            # Fetch attendance data based on the selected date
            cur.execute("""
                SELECT a.roll, s.name, a.date, a.status 
                FROM attendance a 
                JOIN student s ON a.roll = s.roll 
                WHERE a.course = %s AND a.date = %s
            """, (course_id, self.view_date.get()))
            rows = cur.fetchall()
            print(f"Fetched attendance for course {self.var_course.get()} on {self.view_date.get()}: {rows}")

            if len(rows) > 0:
                for idx, (roll, name, date, status) in enumerate(rows):
                    frame = Frame(self.attendance_inner_frame, bg="#FFFFFF" if idx % 2 == 0 else "#F5F5F5", bd=0, relief=FLAT)
                    frame.pack(fill=X, pady=10)
                    Label(frame, text=str(roll), font=("montserrat", 12), bg=frame.cget("bg"), width=10).pack(side=LEFT, padx=10, pady=5)
                    Label(frame, text=name, font=("montserrat", 12), bg=frame.cget("bg"), width=17).pack(side=LEFT, padx=10, pady=5)
                    Label(frame, text=date, font=("montserrat", 12), bg=frame.cget("bg"), width=16).pack(side=LEFT, padx=10, pady=5)
                    status_color = "#28A745" if status == "P" else "#DC3545"
                    Label(frame, text="Present" if status == "P" else "Absent", font=("montserrat", 12, "bold"), bg=frame.cget("bg"), fg=status_color, width=17).pack(side=LEFT, padx=10, pady=5)
            else:
                Label(self.attendance_inner_frame, text="No attendance records found for this date.", font=("Helvetica", 12), bg="#FFFFFF").pack(pady=10)

        except mysql.connector.Error as ex:
            messagebox.showerror("Error", f"Error fetching attendance: {str(ex)}", parent=view_window)
            view_window.destroy()
        finally:
            con.close()

    def view_attendance(self):
        if self.var_course.get() == "Select":
            messagebox.showerror("Error", "Please select a course", parent=self.root)
            return

        # Create a new window for viewing attendance
        view_window = Toplevel(self.root)
        view_window.title("Attendance Report")
        view_window.geometry("800x515+245+150")  # Increased height to accommodate CSV button
        view_window.config(bg="#F5F7FA")

        # Title Frame with Date Picker and CSV button
        title_frame = Frame(view_window, bg="#0C1C47", relief=RIDGE, bd=2)
        title_frame.pack(fill=X, pady=10)
        
        # Left side - Title and date picker
        left_frame = Frame(title_frame, bg="#0C1C47")
        left_frame.pack(side=LEFT, fill=X, expand=True)
        
        Label(left_frame, text="Attendance Report for ", font=("montserrat", 16, "bold"), bg="#0C1C47", fg="white").pack(side=LEFT, padx=10)
        self.view_date = StringVar(value=self.date.get() if self.date.get() else datetime.now().strftime("%Y-%m-%d"))
        view_cal = DateEntry(left_frame, textvariable=self.view_date, date_pattern='yyyy-mm-dd',
                            font=("montserrat", 12), bg="#0C1C47", width=12)
        view_cal.pack(side=LEFT, padx=10)
        view_cal.bind("<<DateEntrySelected>>", lambda e: self.update_attendance_list(view_window))
        Label(left_frame, text=f"{self.var_course.get()}", font=("montserrat", 16, "bold"), bg="#0C1C47", fg="white").pack(side=LEFT, padx=10)
        

        # Rest of your existing view_attendance code...
        # Frame for the attendance list
        attendance_frame = Frame(view_window, bd=0, relief=FLAT, bg="#FFFFFF")
        attendance_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

        # Header for the attendance list
        header_frame = Frame(attendance_frame, bg="#C6E2FF", bd=0, relief=FLAT)
        header_frame.pack(fill=X)
        Label(header_frame, text="Roll", font=("montserrat", 12, "bold"), bg="#C6E2FF", fg="black", width=10).pack(side=LEFT, padx=10, pady=5)
        Label(header_frame, text="Name", font=("montserrat", 12, "bold"), bg="#C6E2FF", fg="black", width=15).pack(side=LEFT, padx=10, pady=5)
        Label(header_frame, text="Date", font=("montserrat", 12, "bold"), bg="#C6E2FF", fg="black", width=12).pack(side=LEFT, padx=10, pady=5)
        Label(header_frame, text="Status", font=("montserrat", 12, "bold"), bg="#C6E2FF", fg="black", width=21).pack(side=LEFT, padx=10, pady=5)

        # Canvas for scrollable attendance list
        canvas = Canvas(attendance_frame, bg="#FFFFFF")
        scrollbar = Scrollbar(attendance_frame, orient=VERTICAL, command=canvas.yview)
        self.attendance_inner_frame = Frame(canvas, bg="#FFFFFF")

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        canvas.create_window((0, 0), window=self.attendance_inner_frame, anchor="nw")
        self.attendance_inner_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Initial population of attendance list
        self.update_attendance_list(view_window)

    # Add this method to the AttendanceClass
    def export_to_csv(self):
        if self.var_course.get() == "Select":
            messagebox.showerror("Error", "Please select a course first", parent=self.root)
            return
        
        if not self.date.get():
            messagebox.showerror("Error", "Please select a date first", parent=self.root)
            return
        
        if not self.student_data:
            messagebox.showerror("Error", "No student data to export", parent=self.root)
            return
        
        try:
            # Ask user where to save the file
            file_path = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")],
                initialfile=f"attendance_{self.var_course.get()}_{self.date.get()}.csv"
            )
            
            if not file_path:  # User cancelled the save dialog
                return
                
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                
                # Write header
                writer.writerow(["Roll No", "Name", "Email", "Gender", "Status", "Course", "Date"])
                
                # Write data
                for roll, data in self.student_data.items():
                    status = "Present" if data['status'].get() == 'P' else "Absent"
                    writer.writerow([
                        roll,
                        data['name'],
                        data['email'],
                        data['gender'],
                        status,
                        self.var_course.get(),
                        self.date.get()
                    ])
            
            messagebox.showinfo("Success", f"Attendance data exported to:\n{file_path}", parent=self.root)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export CSV: {str(e)}", parent=self.root)

    def clear(self):
        self.var_course.set("Select")
        self.student_data.clear()
        self.inner_frame.destroy()
        self.inner_frame = Frame(self.canvas, bg="#FFFFFF")
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")
        self.inner_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        Label(self.inner_frame, text="Please select a course.", font=("Helvetica", 12), bg="#FFFFFF").pack(pady=10)
        self.lbl_present.config(text="Present: 0")
        self.lbl_absent.config(text="Absent: 0")

    # def center_window(self, window=None, width=1200, height=650):
    #     if window is None:
    #         window = self.root
    #     screen_width = window.winfo_screenwidth()
    #     screen_height = window.winfo_screenheight()
    #     x_position = (screen_width // 2) - (width // 2)
    #     y_position = (screen_height // 2) - (height // 2)
    #     window.geometry(f"{width}x{height}+{x_position}+{y_position}")

if __name__ == "__main__":
    root = Tk()
    obj = AttendanceClass(root)
    root.mainloop()
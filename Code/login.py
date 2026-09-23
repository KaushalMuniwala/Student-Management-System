from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # pip install pillow
import mysql.connector  # Use MySQL Connector instead of pymysql
from dashboard import SMS
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "img")
DB_PASSWORD = os.getenv("SMS_DB_PASSWORD", "root")


def image_path(filename):
    return os.path.join(IMG_DIR, filename)

def login_window(self):
    self.new_window = Toplevel(self.root)  # Create a new window
    self.app = Login(self.new_window)  # Open the Login form

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Form")
        self.root.geometry("1520x785+0+0")
        self.root.config(bg="#021e2f")

        login_frame = Frame(self.root, bg="lightblue")
        login_frame.place(x=370, y=130, width=800, height=500)

        title = Label(login_frame, text="..... LOGIN HERE .....", font=("montserrat", 25, "bold", "underline"),
                      bg="lightblue", fg="#021e2f").place(x=250, y=30)

        # Labels & Entry Fields
        Label(login_frame, text="EMAIL ADDRESS:", font=("montserrat", 15, "bold"), bg="lightblue",
              fg="#021e2f").place(x=50, y=120)
        self.txt_email = Entry(login_frame, font=("montserrat", 15), bg="lightgray")
        self.txt_email.place(x=50, y=180, width=350)

        Label(login_frame, text="PASSWORD:", font=("montserrat", 15, "bold"), bg="lightblue",
              fg="#021e2f").place(x=50, y=230)
        self.txt_password = Entry(login_frame, font=("montserrat", 15), bg="lightgray", show="*")
        self.txt_password.place(x=50, y=290, width=350)

        btn_reg = Button(login_frame, cursor="hand2", command=self.register_window, text="Register New Account?",
                         font=("montserrat", 14), bg="lightblue", bd=0, fg="#B00857").place(x=42, y=330)
        
        btn_forget = Button(login_frame, cursor="hand2", command=self.forget_password, text="Forget Password ?",
                         font=("montserrat", 10), bg="lightblue", bd=0, fg="red").place(x=280, y=340)




        btn_login = Button(login_frame, text="Sign In", font=("montserrat", 20, "bold"), bd=0, cursor="hand2",
                           command=self.login, bg="#021e2f", fg="white", activebackground="black",
                           activeforeground="white").place(x=50, y=400, width=350, height=50)

        # Load and display the image
        right_image = Image.open(image_path("login.jpg"))
        right_image = right_image.resize((300, 340), Image.Resampling.LANCZOS)
        self.right_img = ImageTk.PhotoImage(right_image)

        right_label = Label(login_frame, image=self.right_img, bg="lightblue")
        right_label.place(x=450, y=80, width=300, height=400)


    def forget_password(self):
        if self.txt_email.get() == "":
            messagebox.showerror("Error", "Please enter the email address to reset your password", parent=self.root)
        else:
            try:
                # Using MySQL Connector
                con = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password=DB_PASSWORD,
                    database="sms"
                )
                cur = con.cursor(dictionary=True)  # Fetch results as dictionaries

                # Check if the email exists in the register table
                cur.execute("SELECT * FROM register WHERE email=%s", (self.txt_email.get(),))
                row = cur.fetchone()

                if row is None:
                    messagebox.showerror("Error", "Please enter the valid email address to reset your password", parent=self.root)
                else:
                    con.close()  # Close the connection
                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("450x480+340+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()
                    
                    t = Label(self.root2, text=".......Forget Password.......", font=("montserrat", 23, "bold", "underline"), bg="white", fg="red").place(x=0, y=10, relwidth=1)
                    
                    question = Label(self.root2, text="Security question:", font=("montserrat", 15, "bold"), bg="white", fg="black").place(x=40, y=80)
                    self.cmd_quest = ttk.Combobox(self.root2, font=("montserrat", 13), state='readonly', justify=CENTER)
                    self.cmd_quest['values'] = ("Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Name")
                    self.cmd_quest.place(x=40, y=130, width=370)
                    self.cmd_quest.current(0)

                    answer = Label(self.root2, text="Answer:", font=("montserrat", 15, "bold"), bg="white", fg="black").place(x=40, y=190)
                    self.txt_answer = Entry(self.root2, font=("montserrat", 15), bg="lightgray")
                    self.txt_answer.place(x=40, y=230, width=370)

                    new_password = Label(self.root2, text="New Password:", font=("montserrat", 15, "bold"), bg="white", fg="black").place(x=40, y=290)
                    self.txt_new_pass = Entry(self.root2, font=("montserrat", 15), bg="lightgray")
                    self.txt_new_pass.place(x=40, y=330, width=370)

                    btn_change_password = Button(self.root2, text="Reset Password", bg="green", fg="white", cursor="hand2", font=("montserrat", 15, "bold"), command=self.reset_password).place(x=100, y=400, width=250)
                    
            except mysql.connector.Error as es:
                messagebox.showerror("Error", f"Database Error: {str(es)}", parent=self.root)
    
    def reset_password(self):
        if self.cmd_quest.get() == "Select":
            messagebox.showerror("Error", "Please select a security question", parent=self.root2)
        elif self.txt_answer.get() == "":
            messagebox.showerror("Error", "Please enter the answer", parent=self.root2)
        elif self.txt_new_pass.get() == "":
            messagebox.showerror("Error", "Please enter new password", parent=self.root2)
        else:
            try:
                con = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password=DB_PASSWORD,
                    database="sms"
                )
                cur = con.cursor()
                
                # Verify security question and answer
                cur.execute("SELECT * FROM register WHERE email=%s AND question=%s AND answer=%s", 
                        (self.txt_email.get(), self.cmd_quest.get(), self.txt_answer.get()))
                row = cur.fetchone()
                
                if row is None:
                    messagebox.showerror("Error", "Security answer is incorrect", parent=self.root2)
                else:
                    # Update password
                    cur.execute("UPDATE register SET password=%s WHERE email=%s", 
                            (self.txt_new_pass.get(), self.txt_email.get()))
                    con.commit()
                    messagebox.showinfo("Success", "Password has been reset successfully", parent=self.root2)
                    self.root2.destroy()
                    
            except mysql.connector.Error as es:
                messagebox.showerror("Error", f"Database Error: {str(es)}", parent=self.root2)
            finally:
                if con.is_connected():
                    con.close()
        
            
    def register_window(self):
        from register import Register  # Import only inside the function
        self.new_window = Toplevel(self.root)
        Register(self.new_window)


    def login(self):
        if self.txt_email.get() == "" or self.txt_password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                # ✅ Using MySQL Connector
                con = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password=DB_PASSWORD,
                    database="sms"
                )
                cur = con.cursor(dictionary=True)  # Fetch results as dictionaries

                # Check if the email and password exist in the register table
                cur.execute("SELECT * FROM register WHERE email=%s AND password=%s",
                            (self.txt_email.get(), self.txt_password.get()))
                row = cur.fetchone()

                if row is None:
                    messagebox.showerror("Error", "Invalid EMAIL & PASSWORD", parent=self.root)
                else:
                    messagebox.showinfo("Success", "Welcome!", parent=self.root)
                    self.open_dashboard()  # Call function to open dashboard

                con.close()  # Close the connection

            except mysql.connector.Error as es:
                messagebox.showerror("Error", f"Database Error: {str(es)}", parent=self.root)

    # Open dashboard window
    def open_dashboard(self):
        self.root.destroy()  # Close login window
        from dashboard import SMS  # Import the Dashboard class
        root = Tk()  # Create a new root
        obj=SMS(root)  # Open the dashboard
        root.mainloop()  # Start Tkinter main loop

if __name__ == "__main__":
    root = Tk()
    obj = Login(root)
    root.mainloop()

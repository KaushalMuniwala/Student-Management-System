# import sqlite3 # For Databases (Not use other software for databases(Like Xampp))

# def create_db():
#     con=sqlite3.connect(database="sms.db")
#     cur=con.cursor()
#     cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text,duration text,charges text,description text)")    
#     con.commit()
    
#     cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,dob text,contact text,admission text,course text,state text,city text,pin text,address text)")    
#     con.commit()
    
#     cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT,roll text,name text,course text,marks_ob text,full_marks text,per text)")    
#     con.commit()
    
#     con.close()
    
# create_db()


import mysql.connector
import os

DB_PASSWORD = os.getenv("SMS_DB_PASSWORD", "root")


def create_db():
    try:
        # Connect to MySQL
        con = mysql.connector.connect(
            host="localhost",    # Change this if MySQL is running on another server
            user="root",         # Your MySQL username
            password=DB_PASSWORD,
        )
        cur = con.cursor()

        # Create database if not exists
        cur.execute("CREATE DATABASE IF NOT EXISTS sms")
        con.commit()

        # Connect to the newly created database
        con.database = "sms"

        # Create course table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS course(
                cid INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) UNIQUE,  # Ensure course names are unique
                duration VARCHAR(100),
                charges VARCHAR(50),
                description TEXT
            )
        """)
        con.commit()

        # Create student table with foreign key
        cur.execute("""
            CREATE TABLE IF NOT EXISTS student(
                roll INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                email VARCHAR(255),
                gender VARCHAR(10),
                dob DATE,
                contact VARCHAR(15),
                admission DATE,
                course VARCHAR(255),
                state VARCHAR(100),
                city VARCHAR(100),
                pin VARCHAR(10),
                address TEXT,
                CONSTRAINT fk_course FOREIGN KEY (course) REFERENCES course(name) ON DELETE CASCADE
            )
        """)
        con.commit()

        # Create result table with foreign key
        cur.execute("""
            CREATE TABLE IF NOT EXISTS result(
                rid INT AUTO_INCREMENT PRIMARY KEY,
                roll INT,
                name VARCHAR(255),
                course VARCHAR(255),
                marks_ob INT,
                full_marks INT,
                per FLOAT,
                CONSTRAINT fk_student FOREIGN KEY (roll) REFERENCES student(roll) ON DELETE CASCADE
            )
        """)
        con.commit()
        
        # Create register table (Updated)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS register (
                reg_id INT AUTO_INCREMENT PRIMARY KEY,
                f_name VARCHAR(255) NOT NULL,
                l_name VARCHAR(255) NOT NULL,
                contact VARCHAR(15),
                email VARCHAR(255) UNIQUE NOT NULL,
                question VARCHAR(255),
                answer TEXT,
                password VARCHAR(255) NOT NULL  -- Ensure password is always provided
            )
        """)
        con.commit()
        
        # Create attendance table with foreign key to course and student
        cur.execute("""
            CREATE TABLE IF NOT EXISTS attendance (
                aid INT AUTO_INCREMENT PRIMARY KEY,
                roll INT,
                date DATE,
                course INT,
                status ENUM('P', 'A'),
                CONSTRAINT fk_attendance_student FOREIGN KEY (roll) REFERENCES student(roll) ON DELETE CASCADE,
                CONSTRAINT fk_attendance_course FOREIGN KEY (course) REFERENCES course(cid) ON DELETE CASCADE,
                CONSTRAINT unique_attendance UNIQUE (roll, date, course)
            )
        """)
        con.commit()
        
        # Create default demo courses if there are no courses yet
        cur.execute("SELECT COUNT(*) FROM course")
        if cur.fetchone()[0] == 0:
            default_courses = [
                ("BCA", "3 Years", "35000", "Bachelor of Computer Applications"),
                ("B.Sc IT", "3 Years", "32000", "Bachelor of Science in Information Technology"),
                ("MBA", "2 Years", "50000", "Master of Business Administration"),
                ("MCA", "3 Years", "42000", "Master of Computer Applications")
            ]
            cur.executemany(
                "INSERT INTO course (name, duration, charges, description) VALUES (%s, %s, %s, %s)",
                default_courses,
            )
            con.commit()

        print("Database and Tables Created Successfully!")
        con.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Run the function to create the database and tables
create_db()
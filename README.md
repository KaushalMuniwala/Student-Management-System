# Student Management System

A Python-based desktop Student Management System built with Tkinter, MySQL, Pillow, and tkcalendar.

The application helps manage students, courses, attendance, results, and reports from a simple graphical dashboard.

![Student Management System](Code/img/login.jpg)

## Features

- Student registration and records management
- Course creation and management
- Attendance tracking
- Result entry and reporting
- Dashboard overview with summary cards
- MySQL-backed data storage
- User login and registration flow

## Tech Stack

- Python
- Tkinter
- MySQL Connector
- Pillow
- tkcalendar
- MySQL

## Project Structure

- `Code/` - Main application files
- `Code/create_db.py` - Creates the database and required tables
- `Code/dashboard.py` - Main dashboard
- `Code/login.py` - Login screen
- `Code/register.py` - Registration screen
- `Code/student.py` - Student management
- `Code/course.py` - Course management
- `Code/attendance.py` - Attendance management
- `Code/result.py` - Result management
- `Code/report.py` - Reports

## Setup Instructions

1. Install Python 3.x
2. Install the required packages:

```bash
pip install pillow mysql-connector-python tkcalendar
```

3. Make sure MySQL is installed and running.
4. Create a database named `sms`.
5. Set the database password for the app:

```bash
set SMS_DB_PASSWORD=root
```

On Linux/macOS:

```bash
export SMS_DB_PASSWORD=root
```

6. Run the database setup script:

```bash
python Code/create_db.py
```

7. Launch the app:

```bash
python Code/dashboard.py
```

## Database Notes

The project expects a MySQL database named `sms` and uses the root user by default in this setup. If you use a different MySQL password, set the `SMS_DB_PASSWORD` environment variable before running the project.

## Screenshots

- Login screen: `Code/img/login.jpg`
- Dashboard and management screens are available under `Code/img/`

## License

This project is for educational and personal use.

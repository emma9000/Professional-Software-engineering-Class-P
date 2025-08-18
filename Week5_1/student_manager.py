from database import create_connection
import sqlite3

def add_student(name, address):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Students (Stu_Name, Stu_Address) VALUES (?, ?)", (name, address))
    conn.commit()
    print(" student added successfully.")
    conn.close()

def view_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students")
    rows = cursor.fetchall()
    conn.close()
    return rows
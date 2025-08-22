import sqlite3

def create_connection():
    conn = sqlite3.connect("YBCollege.db")
    return conn;

def create_table():
    conn=create_connection()
    cursor=conn.cursor()
    # create
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS class (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    ''')  

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS course (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            details TEXT
        )
    ''') 

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teacher (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            title TEXT,
            courseid INTEGER
        )
    ''') 

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            phone TEXT,
            classid INTEGER,   
            account TEXT,
            password TEXT
        )
    ''') 

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS assignment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            deadline TEXT,
            course_id INTEGER NOT NULL
        )
    ''') 

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grade (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            value REAL NOT NULL,  
            comment TEXT,
            student_id INTEGER NOT NULL, 
            assignment_id INTEGER NOT NULL
        )
    ''') 
    conn.commit()
    conn.close()

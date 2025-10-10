import sqlite3

def create_connection():
    conn = sqlite3.connect("costs.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Cost (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount DOUBLE NOT NULL,
            description TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

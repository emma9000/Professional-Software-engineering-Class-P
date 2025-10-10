from db import create_connection
import sqlite3

def add_cost(amount, description):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Cost (amount, description) VALUES (?, ?)", (amount, description))
    conn.commit()
    print(" cost added successfully.")
    conn.close()

def view_costs():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Cost")
    rows = cursor.fetchall()
    conn.close()
    return rows

def calculate_total_cost():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM Cost")
    total = cursor.fetchone()[0]
    conn.close()
    return total if total else 0.0
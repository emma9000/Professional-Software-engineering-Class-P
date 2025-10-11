from db import create_connection,create_table

def add_cost(amount, description):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Cost (amount, description) VALUES (?, ?)", (amount, description))
    conn.commit()
    # print(" cost added successfully.")
    conn.close()

def view_costs():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Cost")
    rows = cursor.fetchall()
    conn.close()
    return rows


def clear_costs():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Cost")
    conn.commit()
    conn.close()

def calculate_total_cost():
    """
    Return the total cost from the Cost table.

    example: 
    >>> create_table()
    >>> clear_costs()
    >>> add_cost(100.0, "Groceries")
    >>> add_cost(50.0, "Transport")
    >>> calculate_total_cost()
    150.0
    """
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM Cost")
    total = cursor.fetchone()[0]
    conn.close()
    return total if total else 0.0
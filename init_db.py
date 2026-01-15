import sqlite3

def create_database():
    """
    Create and initialize the local SQLite 'sales.db' database with dummy data.

    This function is intended for development and testing purposes. It will:
    - Create the 'users' and 'sales' tables if they do not already exist.
    - Remove all existing records from both tables.
    - Insert a fixed set of example rows into each table to simulate realistic data.

    The function has no parameters and does not return a value. It operates by
    creating or modifying the 'sales.db' file in the current working directory.
    """
    conn = sqlite3.connect("sales.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        role TEXT,
        department TEXT,
        salary INTEGER,
        hire_date TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY,
        product_name TEXT,
        amount INTEGER,
        customer_name TEXT,
        date TEXT,
        status TEXT
    )
    """)

    cursor.execute("DELETE FROM users")
    cursor.execute("DELETE FROM sales")

    users_data = [
        (1, "Alice Smith", "Manager", "Sales", 95000, "2023-01-15"),
        (2, "Bob Jones", "Salesperson", "Sales", 60000, "2023-03-10"),
        (3, "Charlie Lee", "Engineer", "Engineering", 110000, "2022-06-21"),
        (4, "Dana White", "HR Specialist", "HR", 55000, "2021-11-05"),
        (5, "Evan Wright", "Salesperson", "Sales", 62000, "2023-08-19")
    ]
    cursor.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)", users_data)

    sales_data = [
        (1, "Enterprise License", 15000, "TechCorp", "2025-11-01", "Completed"),
        (2, "Basic Subscription", 2000, "SmallBiz Inc", "2025-11-05", "Completed"),
        (3, "Enterprise License", 15000, "MegaBank", "2025-12-01", "Pending"),
        (4, "Consulting Pack", 5000, "StartUp Hub", "2025-12-10", "Completed"),
        (5, "Basic Subscription", 2000, "Local Shop", "2025-12-15", "Cancelled"),
        (6, "Enterprise License", 15000, "HealthPlus", "2026-01-05", "Completed")
    ]
    cursor.executemany("INSERT INTO sales VALUES (?, ?, ?, ?, ?, ?)", sales_data)

    conn.commit()
    conn.close()
    print("Database 'sales.db' created successfully with dummy data")

if __name__ == "__main__":
    create_database()
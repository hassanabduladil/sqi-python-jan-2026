import sqlite3

with sqlite3.connect("students.db") as conn:

    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    year_joined INTEGER NOT NULL,
    dept TEXT NOT NULL,
    gender TEXT
    );""")
    
    # cursor.execute("""INSERT  INTO employees (first_name, last_name, dept, year_joined, gender) VALUES
    # (?, ?, ?, ?, ?),
    # (?, ?, ?, ?, ?),
    # (?, ?, ?, ?, ?),
    # (?, ?, ?, ?, ?),
    # (?, ?, ?, ?, ?);""", ("Mattheus", "Cunha", "Accoutant", 2025, "M", "Jess", "Park", "Secretary", 2018, "F", "Bruno", "Fernandes", "Manager", 1990, "M", "Bryan", "Mbeumo", "Soldier", 2024, "M", "Senne", "Lammens", "Security", 2023, "M"))

    # employees = cursor.execute("SELECT * FROM employees;").fetchall()
    # print(employees)

    # employeess_after_1997 = cursor.execute("SELECT * FROM employees WHERE year_joined > ?;", (18,)).fetchall()
    # print(employeess_after_1997)

    # cursor.execute("""UPDATE employees
    # SET dept = ?
    # WHERE id = ?;
    # """, ("Magician", 3))

    # employees = cursor.execute("SELECT * FROM employees;").fetchall()
    # print(employees)

    # cursor.execute("""DELETE FROM employees
    # WHERE year_joined < ?;""", (1997,))
    
    # employees = cursor.execute("SELECT * FROM employees;").fetchall()
    # print(employees)
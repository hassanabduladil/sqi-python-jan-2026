import sqlite3

with sqlite3.connect("students.db") as conn:

    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        age INTEGER,
        gender TEXT
    );""")

    # cursor.execute("""INSERT INTO students (first_name, last_name, age, gender) VALUES 
    # (?, ?, ?, ?),
    # (?, ?, ?, ?),
    # (?, ?, ?, ?),
    # (?, ?, ?, ?),
    # (?, ?, ?, ?);""", ("Ajana", "Olumide", 16, "M", "Adil", "Hassan", 45, "M", "Francis", "Ezebue", 32, "M", "Winifred", "Igboama", 30, "F", "Pelumi", "Olabiyi", 19, "M"))



    # students = cursor.execute("SELECT * FROM students;").fetchall()

    # print(students)

    # students = cursor.execute("SELECT first_name, age FROM students;").fetchall()

    # for first_name, age in students:
    #     print("First name: ", first_name)
    #     print("Age: ", age)


    # students = cursor.execute("SELECT * FROM students WHERE age > ?;", (18,)).fetchall()

    # print(students)

    # students = cursor.execute("SELECT * FROM students WHERE id = ?;", (100,)).fetchone()

    # print(students)


    cursor.execute("""
UPDATE students
SET age = ?
WHERE first_name = ?;
""", (19, "Francis"))



    students = cursor.execute("SELECT * FROM students;").fetchall()

    print(students)

    cursor.execute("""DELETE FROM students
WHERE id = ?;""", (4,))
    
    students = cursor.execute("SELECT * FROM students;").fetchall()
    
    print(students)

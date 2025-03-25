import sqlite3


departments = [
    (10, "CSE"),
    (20, "ECE"),
    (30, "Civil"),
    (40, "Mech"),
]

students = [
    (1, "Ajay", "Delhi", 10),
    (2, "Vijay", "Kolkata", 10),
    (3, "Ajay", "Mumbai", 20),
    (4, "Ramesh", "Delhi", 30),
    (5, "Suneeta", "Lucknow", 40),
    (6, "Anita", "Kolkata", 30),
    (7, "Raj", "Jaipur", 30),
    (8, "Ali", "Lucknow", 40),
    (9, "Michael", "Cochin", 10),
    (10, "Pavan", "Vijaywada", 20),
    (11, "Suraj", "Hyderabad", 10),
    (12, "Altaf", "Bangaluru", 40),
    (13, "Ravi", "Indore", 20),
    (14, "Verma", "Delhi", 20),
    (15, "Sharma", "Vizag", 10),
]

with sqlite3.connect("university.db") as conn:
    cursor = conn.cursor()

    # Insert departments data
    cursor.executemany(
        """
        INSERT OR REPLACE INTO Departments (depno, name)
        VALUES (?, ?);
        """,
        departments,
    )

    # Insert students data
    cursor.executemany(
        """
        INSERT OR REPLACE INTO Students (roll, name, city, depno)
        VALUES (?, ?, ?, ?);
        """,
        students,
    )

print(f"{len(departments)} department records inserted.")
print(f"{len(students)} student records inserted.")

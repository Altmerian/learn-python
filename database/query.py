import sqlite3


with sqlite3.connect("university.db") as conn:
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Students")
    print(cursor.fetchone(), end="\n\n")
    print(cursor.fetchmany(4), end="\n\n")
    print(cursor.fetchall(), end="\n\n")

    cursor.execute("SELECT DISTINCT name FROM Students")
    for row in cursor:
        print(row[0])
    print()

    cursor.execute("SELECT name FROM Students WHERE name like 'a%'")
    print([t[0] for t in cursor.fetchall()], end="\n\n")

    cursor.execute("SELECT roll, name FROM Students WHERE city NOT IN ('Delhi', 'Mumbai')")
    print(cursor.fetchall(), end="\n\n")

    cursor.execute("""
        SELECT 
            S.roll,
            S.name,
            D.name
        FROM Students S
        JOIN Departments D ON S.depno = D.depno;
    """)
    print(cursor.fetchall(), end="\n\n")

    cursor.execute("""
        SELECT 
            city,
            COUNT(*)
        FROM Students
        GROUP BY city
        HAVING COUNT(*) > 1;
    """)
    print(cursor.fetchall(), end="\n\n")

    cursor.execute("""
        SELECT
            name
        FROM Students
        WHERE city IN (SELECT city FROM Students WHERE name = 'Verma');
    """)
    print(cursor.fetchall(), end="\n\n")

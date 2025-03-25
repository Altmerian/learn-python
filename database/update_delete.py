import sqlite3


with sqlite3.connect("university.db") as conn:
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("UPDATE Departments SET name = 'Chem' where name = 'Mech'")
    print(cursor.execute("SELECT * FROM Departments").fetchall())

    cursor.execute("DELETE FROM Students WHERE roll = 15")
    print(cursor.execute("SELECT COUNT(*) FROM Students").fetchall()[0][0])

    cursor.execute("DELETE FROM Departments WHERE depno = 40")  # now this should throw an error if constraints exist
    print(cursor.execute("SELECT COUNT(*) FROM Departments").fetchall()[0][0])

import sqlite3


with sqlite3.connect("university.db") as conn:
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Departments (
            depno INTEGER PRIMARY KEY, 
            name TEXT NOT NULL
        );
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Students (
            roll INTEGER PRIMARY KEY, 
            name TEXT NOT NULL, 
            city TEXT, 
            depno INTEGER, 
            FOREIGN KEY (depno) REFERENCES Departments(depno)
        );
        """
    )

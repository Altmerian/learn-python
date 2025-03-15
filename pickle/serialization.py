import pickle
from Student import Student

students = [
    Student("John", 20, "CSE"),
    Student("Jane", 21, "ECE"),
    Student("Jim", 22, "MECH"),
]

with open("./pickle/students.pkl", "wb") as f:
    for student in students:
        pickle.dump(student, f)

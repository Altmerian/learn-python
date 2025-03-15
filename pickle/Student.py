class Student:
    def __init__(self, name, age, dept):
        self.name = name
        self.age = age
        self.dept = dept

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Department: {self.dept}"

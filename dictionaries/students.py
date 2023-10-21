students = {}

for i in range(3):
    name = input("Enter student name: ")
    roll_no = int(input("Enter roll number: "))
    dept_name = input("Enter department name: ")

    students[name] = {'Roll no': roll_no, 'Name': name, 'Department': dept_name}

print(students)

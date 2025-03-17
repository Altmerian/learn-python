class Employee:
    employee_count = 101

    @classmethod
    def total_employees(cls):
        return cls.employee_count - 100

    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation
        self.employee_id = "e" + str(Employee.employee_count)
        Employee.employee_count += 1

    def show_details(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: {self.salary}, Designation: {self.designation}"


if __name__ == "__main__":
    emp1 = Employee("John", 50000, "Manager")
    emp2 = Employee("Jane", 60000, "Developer")
    emp3 = Employee("Jim", 70000, "Designer")
    print(emp1.show_details())
    print(emp2.show_details())
    print(emp3.show_details())
    print("Total employees: ", Employee.total_employees())

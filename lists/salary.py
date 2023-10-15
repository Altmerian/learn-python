work_hours = [int(x) for x in input("Enter your work hours separated by space: ").split()]
hourly_rate = int(input("Enter your hourly rate: "))

salary = sum(work_hours) * hourly_rate

print(f"Your salary is: {salary}")

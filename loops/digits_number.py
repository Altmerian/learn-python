n = int(input("Enter a positive number: "))
counter = 0

while n > 0:
    n = n // 10
    counter += 1

print("Number of digits:", counter)

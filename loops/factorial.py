# factorial of a number is the product of all the integers
# from 1 to that number
n = int(input("Enter a number: "))
factorial = 1

for counter in range(1, n + 1):
    factorial *= counter
    counter += 1

print(str(n) + "!", "=", factorial)

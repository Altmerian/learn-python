n = int(input("Enter a positive number: "))
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10

print("Reversed number:", rev)

n = int(input("Enter a positive number: "))
m = n
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10

if m == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")

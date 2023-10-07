# The Fibonacci sequence is a sequence of numbers
# where each number is the sum of the two previous numbers.
n = int(input("Enter the number of terms: "))
a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c

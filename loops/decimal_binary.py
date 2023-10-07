number = int(input("Enter a number: "))
n = number
binary = ''

while n > 0:
    r = n % 2
    n >>= 1
    binary = str(r) + binary

print(number, "to binary:", binary)

integers = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]

number = ''

for x in integers:
    number += str(x)

print(int(number))

# ''.join([str(x) for x in integers])

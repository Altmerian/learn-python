def max3(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

print(max3(n1, n2, n3))

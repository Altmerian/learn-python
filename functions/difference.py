def diff(a, b):
    if abs(a - b) <= 5:
        return True
    else:
        return False


n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

print(diff(n1, n2))

def diff(a, b) -> bool:
    if abs(a - b) <= 5:
        return True
    else:
        return False


if __name__ == "__main__":
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))

    print(diff(n1, n2))

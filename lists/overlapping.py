l1 = [int(x) for x in input("Enter first list of numbers separated by space: ").split()]
l2 = [int(x) for x in input("Enter second list of numbers separated by space: ").split()]

print([x for x in l1 if x in l2])

l1 = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]
l2 = []

for x in l1:
    if x not in l2:
        l2.append(x)

print(l2)

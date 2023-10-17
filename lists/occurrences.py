l1 = input("Enter the list of characters separated by space: ").split()

result = []

for x in l1:
    if x not in result:
        result.append(x)
        result.append(l1.count(x))

print(result)

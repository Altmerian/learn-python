l1 = [int(x) for x in input("Enter first list of numbers separated by space: ").split()]
l2 = [
    int(x) for x in input("Enter second list of numbers separated by space: ").split()
]

print([x for x in l1 if x in l2])

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

list3 = list1 + list2

list1.append(11)

print(list1)
print(list2)
print(list3)

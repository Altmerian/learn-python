def pascal(n):
    row = [1]
    for r in range(n):
        print(row)
        row1 = row + [0]
        row2 = [0] + row
        row = [t1 + t2 for t1, t2 in zip(row1, row2)]


num = int(input("Enter the number of rows: "))
pascal(num)

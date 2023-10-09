name = input("Enter item name: ")
price = float(input("Enter item price: "))

dots = "." * (25 - len(name) - len(str(price)))
print(name + dots + str(price))

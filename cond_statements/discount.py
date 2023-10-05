amount = float(input("Enter amount: "))

discount = 0

if 0 < amount <= 1000:
    discount = 10/100 * amount
elif 1000 < amount <= 5000:
    discount = 20/100 * amount
elif 5000 < amount <= 10000:
    discount = 30/100 * amount
elif amount > 10000:
    discount = 50/100 * amount

print("Discounted amount:", amount - discount)

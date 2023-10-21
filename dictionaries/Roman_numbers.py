roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

s = input("Enter a roman number: ")
result = 0
prev = 0

for i in s:
    if i not in roman:
        print("Invalid roman digit:", i)
        result = None
        break
    if roman[i] > prev:
        result += roman[i] - 2 * prev
    else:
        result += roman[i]
    prev = roman[i]

print("Decimal equivalent:", result)

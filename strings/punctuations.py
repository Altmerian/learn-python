s = input("Enter a string: ")

result = ""

for ch in s:
    if ch.isalnum():
        result += ch

print(result)

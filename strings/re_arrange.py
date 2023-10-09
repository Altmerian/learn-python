s = input("Enter a string: ")

lower = ""
upper = ""
special = ""

for ch in s:
    if ch.islower():
        lower += ch
    elif ch.isupper():
        upper += ch
    else:
        special += ch

print(lower + upper + special)

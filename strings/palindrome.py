s = input("Enter a string: ")

rev = s[::-1]

if s == rev:
    print(s, "is a palindrome.")
else:
    print(s, "is not a palindrome.")
    print("Palindrome from", s, "would be:", s + rev)

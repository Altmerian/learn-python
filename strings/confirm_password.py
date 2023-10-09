pass1 = input("Enter a password: ")
pass2 = input("Confirm password: ")

if pass1 == pass2:
    print("Password confirmed.")
elif pass1.casefold() == pass2.casefold():
    print("Please check the cases and try again key.")
else:
    print("Passwords do not match.")

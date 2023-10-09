email = input("Enter your email address: ")
at_index = email.find("@")

if at_index == -1:
    print("Invalid email address.")
else:
    domain = email[at_index + 1:]
    print("User id:", email[:at_index])
    print("Domain:", domain)

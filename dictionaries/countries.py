countries = {}

for i in range(6):
    country = input("Enter a country: ")
    first_char = country[0].upper()
    countries.setdefault(first_char, []).append(country)

for key, value in countries.items():
    print(f"{key}: {value}")

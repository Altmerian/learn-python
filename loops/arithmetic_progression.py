a = int(input("Enter the first term: "))
d = int(input("Enter the common difference: "))
n = int(input("Enter the number of terms: "))

for term in range(a, a + n * d, d):
    print(term)

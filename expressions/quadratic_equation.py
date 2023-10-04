import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# calculate the discriminant
d = (b**2) - (4*a*c)

# throw an error if discriminant is negative
if d < 0:
    print("This equation has no real solution")
else:
    root1 = (-b - math.sqrt(d)) / (2 * a)
    root2 = (-b + math.sqrt(d)) / (2 * a)
    print("The roots are", root1, "and", root2)

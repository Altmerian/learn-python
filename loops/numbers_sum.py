num_of_numbers = int(input("Enter the number of numbers: "))
sum_positive = 0
sum_negative = 0
counter = 0

while counter < num_of_numbers:
    n = int(input("Enter a number: "))
    if n >= 0:
        sum_positive += n
    else:
        sum_negative += n
    counter += 1

print("Sum of positive numbers:", sum_positive)
print("Sum of negative numbers:", sum_negative)

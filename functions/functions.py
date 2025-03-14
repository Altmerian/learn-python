from difference import diff

numbers = [1, 2, 3, 4, 5]

iter_numbers = iter(numbers)

print(next(iter_numbers))
print(next(iter_numbers))
print(next(iter_numbers))
print(next(iter_numbers))

diff(numbers[0], numbers[1])

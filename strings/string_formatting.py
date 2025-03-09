"""
This file demonstrates the differences between f-strings and string.format() method in Python.
"""

# Variables to use in our examples
name = "Alice"
age = 30
pi = 3.14159

print("1. Basic String Formatting")
print("-" * 30)

# Using string.format() method
print("Hello, {}. You are {} years old.".format(name, age))

# Using f-strings (Python 3.6+)
print(f"Hello, {name}. You are {age} years old.")

print("\n2. Accessing Arguments by Position")
print("-" * 30)

# Using string.format() with positional arguments
print(
    "The value of pi is {0} and {0} rounded to 2 decimal places is {0:.2f}".format(pi)
)

# Using f-strings
print(f"The value of pi is {pi} and {pi} rounded to 2 decimal places is {pi:.2f}")

print("\n3. Accessing Arguments by Name")
print("-" * 30)

# Using string.format() with named arguments
print(
    "Hello, {name}. Next year, you'll be {new_age}.".format(name=name, new_age=age + 1)
)

# Using f-strings with expressions
print(f"Hello, {name}. Next year, you'll be {age + 1}.")

print("\n4. Formatting Numbers")
print("-" * 30)

# Using string.format()
print("Pi with 2 decimal places: {:.2f}".format(pi))
print("Pi with 2 decimal places and right-aligned in 10 spaces: {:>10.2f}".format(pi))

# Using f-strings
print(f"Pi with 2 decimal places: {pi:.2f}")
print(f"Pi with 2 decimal places and right-aligned in 10 spaces: {pi:>10.2f}")

print("\n5. Performance Comparison")
print("-" * 30)

import timeit

# Setup code
setup = """
name = "Alice"
age = 30
pi = 3.14159
"""

# Test string.format() performance
format_time = timeit.timeit(
    'msg = "Hello, {}. You are {} years old. Pi is {:.2f}".format(name, age, pi)',
    setup=setup,
    number=1000000,
)

# Test f-string performance
fstring_time = timeit.timeit(
    'msg = f"Hello, {name}. You are {age} years old. Pi is {pi:.2f}"',
    setup=setup,
    number=1000000,
)

print(f"string.format() time: {format_time:.6f} seconds")
print(f"f-string time: {fstring_time:.6f} seconds")
print(f"f-strings are approximately {format_time / fstring_time:.2f}x faster")

print("\n6. Key Differences Summary")
print("-" * 30)
print("- f-strings were introduced in Python 3.6")
print("- f-strings are generally more readable and concise")
print("- f-strings are evaluated at runtime, not when defined")
print("- f-strings are faster than string.format()")
print("- f-strings allow direct embedding of expressions like {age+1}")
print(
    "- string.format() can be useful when the format string is defined separately from the values"
)

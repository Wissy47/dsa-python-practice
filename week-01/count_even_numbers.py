# Problem 1 — Count Even Numbers

# Write a function that accepts a list of integers and returns the number of even integers.
# Example

# numbers = [3, 8, 12, 5, 7, 10]

# Expected output: 3

# Requirements: Don't use list comprehensions or built-in counting functions. Use a straightforward loop.


def count_even(numbers):
    count = 0

    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count


print(count_even([3, 8, 12, 5, 7, 10]))

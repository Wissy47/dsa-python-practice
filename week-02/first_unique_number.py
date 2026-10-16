# Coding Challenge — First Non-Repeating Number
# Easy · Hash Map

# Problem statement
# Given a list of integers, return the first number in the original list that appears exactly once.
# If no number appears exactly once, return None.
# Your function should preserve the meaning of first based on the original input order.

# Test cases
# Input	Expected output
# [4, 5, 4, 7, 5, 9]	7
# [2, 2, 3, 3, 4]	4
# [8, 8, 8]	None
# [1, 2, 3]	1
# [-2, -1, -2, 5]	-1
# []	None
# Requirements
# - Use a dictionary for frequency counting.
# - Return the number itself, not its index.
# - Do not modify the original list.
# - Do not use collections.Counter.
# - Aim for O(n) expected time and O(n) worst-case auxiliary space.


def first_unique_number(numbers):
    if not numbers:
        return
    counter = {}

    for number in numbers:
        counter[number] = counter.get(number, 0) + 1
    for number, count in counter.items():
        if count == 1:
            return number

    return None


print(first_unique_number([5, 5, 5, 5, -3]))

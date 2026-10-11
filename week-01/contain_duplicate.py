# Problem 1 — Contains Duplicate
# Easy

# Given a list of integers, return True if any value appears at least twice, and False if every value is unique.

# Examples
# Input	Output
# [1, 2, 3, 1]	True
# [1, 2, 3, 4]	False
# []	False
# [-1, -2, -1]	True
# [5]	False
# Constraints: Do not use collections.Counter, sorting, or third-party libraries. Do not modify the original list.
# Your assignment has two stages:
# Stage A — Brute force: Implement a straightforward solution that compares pairs of elements.
# Stage B — Optimization: Implement a more efficient solution using a suitable Python data structure.
# For each stage, explain time complexity, auxiliary-space complexity, and why the solution is correct.

# Stage A — Brute-force implementation


def contains_duplicate_brute(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                return True
    return False


def contains_duplicate_optimized(numbers):
    seen = set()

    for number in numbers:
        if number in seen:
            return True
        seen.add(number)
    return False


# print(contains_duplicate_brute([5]))
print(contains_duplicate_optimized([1, 2, 3, 3, 1]))

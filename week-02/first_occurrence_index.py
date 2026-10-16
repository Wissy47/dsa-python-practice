# First Occurrence Index

# Write a function that accepts a list of integers and a target integer.
# Return the index of the target's first occurrence. If the target is absent, return -1.
# For this exercise, use a dictionary to record the first index at which each distinct number appears.

# Test cases
# Input	Target	Expected
# [10, 20, 30, 20, 40]	20	1
# [5, 5, 5]	5	0
# [7, 8, 9]	9	2
# [3, 4, 5]	8	-1
# [-2, -1, -2]	-2	0
# []	10	-1
# Requirements: Use a dictionary, preserve the earliest index of each value, and aim for O(n) expected time.


def first_occurrence_index(numbers, target):
    if not numbers:
        return -1
    counter = {}
    for i in range(len(numbers)):
        if numbers[i] not in counter:
            counter[numbers[i]] = i
    if target in counter:
        return counter[target]
    return -1


print(first_occurrence_index([10, 20, 30, 20, 40], 40))

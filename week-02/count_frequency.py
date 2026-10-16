# Count Occurrences of a Target
# Easy · Coding

# Problem statement
# Write a Python function that accepts a list of integers and a target integer.
# Use a dictionary to count how many times each number appears, then return the frequency of the target.
# If the target does not exist, return 0.

# Requirements
# - Use a dictionary to store counts for the numbers.
# - Return the target's frequency as an integer.
# - If the target is absent, return 0.
# - Do not modify the original list.
# - Do not use collections.Counter or numbers.count().
# - Aim for O(n) expected time.
# Test cases
# Input	                Target	Expected
# [2, 3, 2, 5, 3, 2]	2	    3
# [1, 1, 1, 1]	        1	    4
# [4, 5, 6]	            2	    0
# [-1, -1, 3]	        -1	    2
# [7]	                7	    1
# []	                5	    0


def count_target(numbers, target):
    if not numbers:
        return 0
    scores = {}

    for number in numbers:
        if number in scores:
            scores[number] += 1
        else:
            scores[number] = 1
    if target in scores:
        return scores[target]
    return 0


print(count_target([2, 3, 2, 5, 3, 2], 5))

# Longest Consecutive Run
# Algorithmic Optimization · Array Traversal

# Now we're moving to a problem that tests your ability to identify repeated work and improve an algorithm.
# Unlike Problems 1 and 2, this exercise requires you to develop both a brute-force solution and an optimized approach.
# I won't tell you which data structure or optimization pattern to use.
# Problem statement
# Given a list of integers, return the length of the longest run of equal values appearing next to one another.
# A run is a group of consecutive positions containing the same value.

# Requirements: Return the length of the longest consecutive run of equal integers. An empty list returns 0. A non-empty list has a minimum run length of 1. Do not sort or modify the input. Aim to improve your initial approach if it performs unnecessary repeated work.
# Test cases
# Input	Expected output
# [1, 1, 2, 2, 2, 3]	3
# [4, 4, 4, 4]	4
# [1, 2, 1, 2]	1
# [-2, -2, 0, 0, 0]	3
# [5]	1
# []	0
# [7, 7, 3, 3]	2

# initailize a runner to first element and count to 0
# if previous item is same as the current item increase count else reset count to 1 while keeping track of higest count


def longest_run(numbers):
    if not numbers:
        return 0
    highest_count = 0
    count = 1
    run = numbers[0]

    for i in range(1, len(numbers)):
        if run == numbers[i]:
            count += 1
        else:
            highest_count = max(highest_count, count)
            count = 1
            run = numbers[i]
    highest_count = max(highest_count, count)
    return highest_count


print(longest_run([1, 1, 2, 2, 2, 3]))

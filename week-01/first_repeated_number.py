# First Repeated Value
# Medium · Optimization

# Given a list of integers, return the first value encountered for the second time while scanning from left to right.
# If no value repeats, return None.

# def first_repeated(numbers):
#     for i in range(len(numbers)):
#         for j in range(i):
#             if numbers[i] == numbers[j]:
#                 return numbers[i]
#     return None

#   Your task is to analyze the implementation, trace it, and design a more efficient solution.
# Requirements
# - Return the first value encountered for the second time, not the value with the smallest first-occurrence index.
# - Return None when no duplicates exist.
# - Preserve the original list.
# - Do not sort the list.
# - Your optimized implementation should aim for O(n) expected time.
# - Explain any additional memory required.
# Test cases
# Input	Expected result
# [4, 2, 7, 2, 4, 9]	2
# [5, 1, 5, 1]	5
# [3, 2, 1]	None
# [8, 8, 8]	8
# [-1, 3, -1, 3]	-1
# [1]	None
# []	None
# [2, 1, 1, 2]	1
# The last example is especially useful: the answer is 1, even though 2 was encountered first.


def first_repeated(numbers):
    for i in range(len(numbers)):
        count = 0
        for j in range(i):
            print(numbers[i], numbers[j])
            if numbers[i] == numbers[j]:
                return numbers[i]
            count += 1
    return count


def first_repeated_optimized(numbers):
    seen = set()
    for i in range(len(numbers)):
        if numbers[i] in seen:
            return numbers[i]
        seen.add(numbers[i])
    return None


print(first_repeated_optimized([]))
# print(first_repeated([4, 2, 7, 1, 9, 2]))

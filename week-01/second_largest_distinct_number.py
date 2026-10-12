# Second Largest Distinct Number
# Easy → Medium

# Problem statement
# Given a list of integers, return the second-largest distinct number.
# Distinct means the second-largest value must be different from the largest value.

# Requirements
# - The input is a list of integers.
# - Return the second-largest distinct integer.
# - Return None if fewer than two distinct values exist.
# - The input may contain negative numbers, zero, and duplicates.
# - Do not modify the original list.
# - Do not use sort(), sorted(), or max().
# - Aim for O(n) time and O(1) auxiliary space.
# Test cases
# Input	Expected output
# [12, 5, 27, 8, 19]	19
# [10, 10, 8, 7]	8
# [-5, -2, -9, -3]	-3
# [4, 4, 4]	None
# [7]	None
# []	None
# [2, 1]	1
# [1, 2]	1

# Before writing code — Interview reasoning
# In a real interview, I'd expect you to think about the problem before implementing it.
# For this problem, consider:
# - What information must be maintained while traversing the list?
# - How will you distinguish the largest value from the second-largest distinct value?
# - What happens if the list contains only negative numbers?
# - What happens if the largest number appears several times?
# - How will you recognize that no second-largest distinct value exists?
# [12, 5, 27, 8, 19]	19
def second_largest(numbers):
    if not numbers or len(numbers) == 1:
        return None

    largest_num = numbers[0]
    second_largest_num = None

    for i in range(1, len(numbers)):
        if numbers[i] > largest_num:
            second_largest_num = largest_num
            largest_num = numbers[i]
        if (
            numbers[i] < largest_num
            and second_largest_num is None
            or second_largest_num is not None
            and largest_num > numbers[i] > second_largest_num
        ):
            second_largest_num = numbers[i]
    return second_largest_num


print(second_largest([12, 5, 27, 8, 19]), "-->expected 19")
print(second_largest([10, 10, 8, 7]), "-->expected 8")
print(second_largest([-5, -2, -9, -3]), "-->expected -3")
print(second_largest([4, 4, 4]), "-->expectec None")
print(second_largest([2, 1]), "-->expected 1")
print(second_largest([1, 2]), "-->expected 1")
print(second_largest([7]), "-->expected None")
print(second_largest([]), "-->expected None")

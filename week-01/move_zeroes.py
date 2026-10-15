# Move Zeroes
# Easy → Medium

# Given a list of integers numbers, move all zeroes to the end of the list while preserving the relative order of all non-zero elements.
# You must modify the original list in place.

# Requirements
# - Modify the input list in place.
# - Preserve the relative order of non-zero elements.
# - Return None (the caller inspects the modified list).
# - Do not create another list containing the elements.
# - Do not use sort() or sorted().
# - Aim for O(n) time and O(1) auxiliary space.
# - Zero is the integer 0; negative numbers are non-zero.
# Test cases
# Input	Expected modified list
# [0, 1, 0, 3, 12]	[1, 3, 12, 0, 0]
# [0, 0, 1]	[1, 0, 0]
# [1, 2, 3]	[1, 2, 3]
# [0, 0, 0]	[0, 0, 0]
# [4, 0, -2, 0, 5]	[4, -2, 5, 0, 0]
# [1]	[1]
# []	[]


def move_zeroes(numbers):
    if not numbers or len(numbers) == 1:
        return
    last_switch_index = 0
    for i in range(len(numbers)):
        if numbers[i] != 0:
            temp = numbers[i]
            numbers[i] = numbers[last_switch_index]
            numbers[last_switch_index] = temp
            last_switch_index += 1


numbers = [1, 2, 3, 4]
print(move_zeroes(numbers))
print(numbers)

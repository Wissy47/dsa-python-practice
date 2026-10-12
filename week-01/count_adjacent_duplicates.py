# Count Adjacent Duplicates
# Your next challenge is to correct this function without creating another list:
# For example, [1, 1, 2, 2, 2, 3] should return 3.
# Think about this: When i reaches the last valid index, what happens when Python evaluates numbers[i + 1]?


def count_adjacent_duplicates(numbers):
    count = 0

    for i in range(len(numbers) - 1):
        if numbers[i] == numbers[i + 1]:
            count += 1

    return count


print(count_adjacent_duplicates([1, 1, 2, 2, 2, 3]))

# Remove All Occurrences
# Now we're moving to the most interesting debugging exercise of Day 5.

# However, modifying a list while iterating over it can cause elements to be skipped.
# Your task: Correct the function so that it removes every occurrence of the target.
# You may create a new list or use an in-place approach,
# def remove_all(numbers, target):
#     for number in numbers:
#         if number == target:
#             numbers.remove(number)

#     return numbers


def remove_all(numbers, target):
    new_list = []
    for number in numbers:
        if number != target:
            new_list.append(number)
            # numbers.remove(number)

    return new_list


print(remove_all([2, 2, 3, 2, 4], 2))

# Find the Smallest Number
# Debugging

# The following function is intended to return the smallest integer in a non-empty list.


def find_smallest(numbers):
    smallest = numbers[0]

    for number in numbers:
        smallest = min(smallest, number)

    return smallest


print(find_smallest([-4, -9, -1]))

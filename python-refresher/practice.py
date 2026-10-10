def sum_even_numbers(numbers):
    total = 0

    for number in numbers:
        if number % 2 == 0:
            total += number

    return total


# Test cases
assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12
assert sum_even_numbers([1, 3, 5]) == 0
assert sum_even_numbers([2, 4, 6]) == 12
assert sum_even_numbers([]) == 0

print("All tests passed!")

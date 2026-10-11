def has_pair_with_sum(numbers, target):
    seen = set()

    for number in numbers:
        complement = target - number

        if complement in seen:
            return True

        seen.add(number)

    return False


numbers = [2, 3, 7, 11, 15]
target = 9
has_pair_with_sum(numbers, target)

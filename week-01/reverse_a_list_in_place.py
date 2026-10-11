# Reverse a List In Place

# Remember the requirements: modify the original list without creating another list, don't use Python's built-in reversal methods or slicing, and aim for O(n) time and O(1) auxiliary space.
# Before coding, think about this question:
# If the first element needs to become the last, and the last needs to become the first, how can you exchange their positions without losing either value?
# Try implementing your idea and explain why your loop stops where it does.


def reverse_list_in_place(numbers):

    temp = None
    length = len(numbers)

    for i in range(length // 2):
        temp = numbers[length - i - 1]
        numbers[length - i - 1] = numbers[i]
        numbers[i] = temp


number = [3, 8, 12, 7, 10]
res = reverse_list_in_place(number)
print(res)
print(number)

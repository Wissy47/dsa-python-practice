# Count Vowels
# We'll remain on Day 4 and continue with the third exercise.
# Problem: Write a Python function that counts the number of vowels (a, e, i, o, u) in a string, ignoring letter case.
# Examples:
# Input	Expected output
# "Hello World"	3
# "PYTHON"	1
# "AEIOU"	5
# "rhythm"	0
# ""	0
# You may use .lower(), but don't use built-in counting functions or external libraries.


def count_vowels(text):
    vowel = ("a", "e", "i", "o", "u")
    count = 0

    for char in text:
        if char.lower() in vowel:
            count += 1

    return count


print(count_vowels("PYTHON"))

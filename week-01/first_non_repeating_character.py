# First Non-Repeating Character
# Easy → Medium

# Given a string text, return the index of the first character that appears exactly once in the entire string.
# If every character is repeated, return -1.

# Requirements
# - Return an integer index, not the character itself.
# - Return -1 if no non-repeating character exists.
# - Treat uppercase and lowercase letters as different characters.
# - Spaces and punctuation are valid characters.
# - Do not modify the original string.
# - Do not use collections.Counter, external libraries, or sorting.
# - Aim for O(n) time, although a correct brute-force attempt is welcome

# 2. Examples and edge cases
# Input	Expected index	Explanation
# "leetcode"	0	l appears once
# "loveleetcode"	2	v is the first unique character
# "aabb"	-1	Every character repeats
# "aabbc"	4	c appears once
# "aAbB"	0	Case-sensitive comparison
# "a b a"	2	The first unique character is b
# "z"	0	A single character is unique
# ""	-1	No characters exist


def first_unique_char(text):
    length = len(text)
    if length == 0:
        return -1

    uniques = {}
    seen = set()

    for i in range(length):
        if text[i] in seen:
            uniques.pop(text[i], "")  # do not throw error if you cannot find key
        else:
            uniques[text[i]] = i
        seen.add(text[i])
    if uniques:
        return next(iter(uniques.values()))

    return -1


print(first_unique_char("leetcode"))
print(first_unique_char("loveleetcode"))
print(first_unique_char("aabb"))
print(first_unique_char("aabbc"))
print(first_unique_char("aAbB"))
print(first_unique_char("a b a"))
print(first_unique_char("z"))
print(first_unique_char(""))

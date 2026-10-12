# Remove Consecutive Duplicates
# Medium · Debugging

# Problem statement
# Given a list of integers, remove consecutive duplicate values, keeping only the first element from each consecutive group.
# Return a new list containing the remaining elements in their original order.

# Important: The function contains a logical error. It does not necessarily raise an exception, but it produces incorrect output for certain valid inputs.
# Your task is to identify the problem, fix it, and explain the correction.
# Requirements
# - Return a new list.
# - Preserve the original order.
# - Remove only adjacent duplicates.
# - Do not modify the input list.
# - Do not use set() or sorting.
# - Aim for O(n) time.

# Test cases
# These tests are designed to expose different situations.
# Input	Expected output
# [1, 1, 2, 2, 3, 1, 1]	[1, 2, 3, 1]
# [1, 2, 3, 4]	[1, 2, 3, 4]
# [5, 5, 5]	[5]
# [1, 2]	[1, 2]
# [9]	[9]
# []	[]
# [2, 2, 3, 3, 2, 2]	[2, 3, 2]
# [-1, -1, 0, 0, -1]	[-1, 0, -1]
# 3. Your debugging assignment
# I want you to approach this as you would in a technical interview.
# Step 1 — Identify the bug
# Explain which statement is causing the incorrect behavior and why.


# Step 2 — Manually trace the buggy implementation
# Use [1, 2, 3, 4]. Determine exactly which iterations execute and what the buggy function returns.


# Step 3 — Correct the implementation
# Make the smallest reasonable change necessary to fix the bug.


# Step 4 — Verify correctness
# Explain why the corrected algorithm preserves the first element of every consecutive run.


# Step 5 — Analyze complexity
# Give time complexity and auxiliary-space complexity, explaining why each applies.


def remove_consecutive_duplicates(numbers):
    if not numbers:
        return []

    result = [numbers[0]]

    for i in range(1, len(numbers)):
        if numbers[i] != numbers[i - 1]:
            result.append(numbers[i])

    return result


print(remove_consecutive_duplicates([1, 1, 2, 2, 3, 1, 1]))

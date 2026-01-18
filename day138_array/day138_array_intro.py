"""
Day 138: Array
Array problems often combine traversal with greedy selection,
prefix sums, or stack-based optimization for efficient solutions.
"""

# Example 1: Finding two maximum values in an array
def find_two_max(arr):
    max1, max2 = 0, 0
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    return max1, max2

print("Output Example 1:", find_two_max([3, 4, 5, 2]))


# Example 2: Running sum computation
def running_sum(arr):
    total = 0
    res = []
    for x in arr:
        total += x
        res.append(total)
    return res

print("Output Example 2:", running_sum([1, 2, 3, 4]))

"""
Day 137: Array
Arrays store elements in contiguous memory, allowing fast access by index.
They are widely used for prefix sums, counting, greedy strategies, and scanning.
"""


# Example 1: Prefix Sum concept
def prefix_sum_example(arr):
    prefix = []
    curr = 0
    for num in arr:
        curr += num
        prefix.append(curr)
    return prefix


print("Output Example 1:", prefix_sum_example([1, 2, 3, 4]))


# Example 2: Greedy traversal on array
def greedy_max_elements(arr):
    arr.sort(reverse=True)
    return arr[:3]


print("Output Example 2:", greedy_max_elements([5, 1, 3, 7, 2]))

"""
Day 148: Prefix Sum
Prefix Sum precomputes cumulative information to answer range queries
or subarray problems efficiently, often reducing O(n²) to O(n).
"""


# Example 1: Prefix sum array for range sum queries
def example_one():
    """
    Build prefix sum:
    prefix[i] = sum of elements from index 0 to i-1
    Range sum [l, r] = prefix[r+1] - prefix[l]
    """
    nums = [2, 4, 6, 8]
    prefix = [0]

    for n in nums:
        prefix.append(prefix[-1] + n)

    # sum from index 1 to 3 -> 4 + 6 + 8 = 18
    return prefix[4] - prefix[1]


print("Output Example 1:", example_one())


# Example 2: Prefix sum with hashmap (counting subarrays)
def example_two():
    """
    Use hashmap to count prefix sums:
    If prefix[j] - prefix[i] == k, then subarray (i+1..j) sums to k
    """
    nums = [1, -1, 1, -1]
    k = 0
    prefix = 0
    count = {0: 1}
    res = 0

    for n in nums:
        prefix += n
        res += count.get(prefix - k, 0)
        count[prefix] = count.get(prefix, 0) + 1

    return res


print("Output Example 2:", example_two())

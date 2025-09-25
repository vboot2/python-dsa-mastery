"""
Day 25: Two Pointers, Greedy, Prefix Sum

- Sum of all odd length subarrays (Prefix sums)
- Product of array except self (Prefix & Suffix products, avoiding division)
"""

# Example 1: Prefix Sum on odd-length subarrays
def example_one():
    arr = [1,4,2,5,3]
    n = len(arr)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + arr[i]
    total = 0
    for i in range(n):
        for j in range(i, n, 2):  # odd length subarrays
            total += prefix[j+1] - prefix[i]
    return total

print("Output Example 1 (Odd length subarrays sum):", example_one())


# Example 2: Product of array except self (without division)
def example_two():
    nums = [1,2,3,4]
    n = len(nums)
    left, right, result = [1]*n, [1]*n, [1]*n
    
    for i in range(1, n):
        left[i] = left[i-1] * nums[i-1]
    for i in range(n-2, -1, -1):
        right[i] = right[i+1] * nums[i+1]
    for i in range(n):
        result[i] = left[i] * right[i]
    return result

print("Output Example 2 (Product except self):", example_two())

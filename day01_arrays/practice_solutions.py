# practice_solutions.py
# Day 1: Arrays - Practice Solutions

# 1. Two Sum (LeetCode 1)
# Hint: Use a dictionary (hashmap) for O(n) solution
def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
    return []

# Test
print(two_sum([2, 7, 11, 15], 9))  # Expected [0, 1]


# 2. Best Time to Buy and Sell Stock (LeetCode 121)
# Hint: Track min price so far, and max profit at each step
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

# Test
print(max_profit([7,1,5,3,6,4]))  # Expected 5


# 3. Contains Duplicate (LeetCode 217)
# Hint: Use a set to track seen numbers
def contains_duplicate(nums):
    return len(nums) != len(set(nums))

# Test
print(contains_duplicate([1,2,3,1]))  # Expected True

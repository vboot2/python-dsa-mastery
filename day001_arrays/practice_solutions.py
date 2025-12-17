# practice_solutions.py
# Day 1: Arrays - Practice Solutions

# 1. Two Sum (LeetCode 1)
def twosum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
    return []

# Test [3,3], target = 6
print(twosum([2, 7, 11, 15], 9))  # Expected [0, 1]
print(twosum([3,2,4], 6))  # Expected [1, 2]
print(twosum([3,3], 6))  # Expected [0, 1]


# 2. Best Time to Buy and Sell Stock (LeetCode 121)
def maxProfit(prices) -> int:
    minprice = float('inf')
    maxprofit = 0
    for price in prices:
        minprice = min(minprice, price)
        maxprofit = max(maxprofit, price - minprice)
    return maxprofit

# Test
print(maxProfit([7,1,5,3,6,4]))  # Expected 5
print(maxProfit([7,6,4,3,1]))  # Expected 0


# 3. Contains Duplicate (LeetCode 217)
def containsduplicate(nums):
    return len(nums) != len(set(nums))

# Test
print(containsduplicate([1,2,3,1]))  # Expected True
print(containsduplicate([1,2,3,4]))  # Expected False
print(containsduplicate([1,1,1,3,3,4,3,2,4,2]))  # Expected True

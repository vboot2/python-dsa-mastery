"""
Day 68: Binary Search (on Answer)

Typical pattern:
1. Define the search space of possible answers (low, high).
2. Use binary search to check feasibility (using a helper `canDo()` function).
3. Adjust search range based on whether the current guess works.
"""


# -------------------------------------------------------
# Example 1: Allocate Books / Split Array Problem
# -------------------------------------------------------
def example_one(nums: list[int], k: int) -> int:
    def canSplit(mid):
        # Count how many subarrays we can form without exceeding mid sum
        count, curr_sum = 1, 0
        for n in nums:
            if curr_sum + n > mid:
                count += 1
                curr_sum = n
            else:
                curr_sum += n
        return count <= k

    low, high = max(nums), sum(nums)
    res = high
    while low <= high:
        mid = (low + high) // 2
        if canSplit(mid):
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res


print("Example 1 (Split Array):", example_one([7, 2, 5, 10, 8], 2))


# -------------------------------------------------------
# Example 2: Capacity to Ship Packages within D Days
# -------------------------------------------------------
def example_two(weights: list[int], days: int) -> int:
    def canShip(cap):
        ships, curr = 1, 0
        for w in weights:
            if curr + w > cap:
                ships += 1
                curr = w
            else:
                curr += w
        return ships <= days

    low, high = max(weights), sum(weights)
    while low < high:
        mid = (low + high) // 2
        if canShip(mid):
            high = mid
        else:
            low = mid + 1
    return low


print("Example 2 (Ship Packages):", example_two([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))


# -------------------------------------------------------
# Example 3: Koko Eating Bananas
# -------------------------------------------------------
import math


def example_three(piles: list[int], h: int) -> int:
    def canEat(speed):
        time = 0
        for pile in piles:
            time += math.ceil(pile / speed)
        return time <= h

    low, high = 1, max(piles)
    while low < high:
        mid = (low + high) // 2
        if canEat(mid):
            high = mid
        else:
            low = mid + 1
    return low


print("Example 3 (Koko Eating Bananas):", example_three([3, 6, 7, 11], 8))

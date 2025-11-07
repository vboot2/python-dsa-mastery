"""
Day 68: Binary Search (on Answer) - LeetCode Practice Solutions
"""

import math

# ---------------------------------------------------------
# Problem 1: Split Array Largest Sum (LeetCode 410, Hard)
# Link: https://leetcode.com/problems/split-array-largest-sum/
# ---------------------------------------------------------


class SolutionSplitArray:
    def splitArray(self, nums: list[int], k: int) -> int:
        def canSplit(mid):
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


# ---------------------------------------------------------
# Problem 2: Capacity To Ship Packages Within D Days (LeetCode 1011, Medium)
# Link: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
# ---------------------------------------------------------


class SolutionShipPackages:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
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


# ---------------------------------------------------------
# Problem 3: Koko Eating Bananas (LeetCode 875, Medium)
# Link: https://leetcode.com/problems/koko-eating-bananas/
# ---------------------------------------------------------


class SolutionKokoBananas:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
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


# ---------------------------------------------------------
# Example usage
# ---------------------------------------------------------
if __name__ == "__main__":
    print(
        "Split Array Largest Sum:", SolutionSplitArray().splitArray([7, 2, 5, 10, 8], 2)
    )
    print(
        "Ship Packages:",
        SolutionShipPackages().shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5),
    )
    print(
        "Koko Eating Bananas:", SolutionKokoBananas().minEatingSpeed([3, 6, 7, 11], 8)
    )

"""
Day 138: Array - LeetCode Problem Solutions
"""

from typing import List


# ---------------------------------------------------------
# Problem: Maximum Product of Two Elements in an Array (LeetCode 1464)
# Link: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
# ---------------------------------------------------------
class Solution1:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = 0
        max2 = 0
        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num

        return (max1 - 1) * (max2 - 1)


# ---------------------------------------------------------
# Problem: Shuffle the Array (LeetCode 1470)
# Link: https://leetcode.com/problems/shuffle-the-array/
# ---------------------------------------------------------
class Solution2:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i + n])
        return res


# ---------------------------------------------------------
# Problem: Final Prices With a Special Discount in a Shop (LeetCode 1475)
# Link: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
# ---------------------------------------------------------
class Solution3:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = prices[:]
        stack: List[int] = []

        for i, cur_price in enumerate(prices):
            while stack and prices[stack[-1]] >= cur_price:
                idx = stack.pop()
                result[idx] = prices[idx] - cur_price
            stack.append(i)
        return result


# ---------------------------------------------------------
# Problem: Running Sum of 1d Array (LeetCode 1480)
# Link: https://leetcode.com/problems/running-sum-of-1d-array/
# ---------------------------------------------------------
class Solution4:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        return [(total := total + x) for x in nums]


# ---------------------------------------------------------
# Problem: Average Salary Excluding the Minimum and Maximum Salary (LeetCode 1491)
# Link: https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
# ---------------------------------------------------------
class Solution5:
    def average(self, salary: List[int]) -> float:
        mn, mx = min(salary), max(salary)
        return (sum(salary) - mn - mx) / (len(salary) - 2)

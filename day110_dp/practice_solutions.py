"""
Day 110: DP - LeetCode Problem Solutions
"""

from typing import List


# ---------------------------------------------------------
# Problem: Maximum Subarray (LeetCode 53, Medium)
# Link: https://leetcode.com/problems/maximum-subarray/
# ---------------------------------------------------------
class SolutionProblemOne:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Kadane's Algorithm:
        Track maximum subarray ending at each index.
        """
        curr = best = nums[0]

        for n in nums[1:]:
            curr = max(n, curr + n)
            best = max(best, curr)

        return best


# ---------------------------------------------------------
# Problem: Best Time to Buy and Sell Stock II (LeetCode 122, Medium)
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Greedy / DP intuition:
        Take all increasing price differences.
        """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


# ---------------------------------------------------------
# Problem: Ugly Number II (LeetCode 264, Medium)
# Link: https://leetcode.com/problems/ugly-number-ii/
# ---------------------------------------------------------
class SolutionProblemThree:
    def nthUglyNumber(self, n: int) -> int:
        """
        DP with pointers:
        dp[i] = min(dp[p2]*2, dp[p3]*3, dp[p5]*5)
        """
        dp = [1] * n
        p2 = p3 = p5 = 0

        for i in range(1, n):
            next_val = min(dp[p2]*2, dp[p3]*3, dp[p5]*5)
            dp[i] = next_val

            if next_val == dp[p2]*2:
                p2 += 1
            if next_val == dp[p3]*3:
                p3 += 1
            if next_val == dp[p5]*5:
                p5 += 1

        return dp[-1]


# ---------------------------------------------------------
# Problem: Perfect Squares (LeetCode 279, Medium)
# Link: https://leetcode.com/problems/perfect-squares/
# ---------------------------------------------------------
class SolutionProblemFour:
    def numSquares(self, n: int) -> int:
        """
        Classic DP:
        dp[i] = min(dp[i - square] + 1)
        """
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1

        return dp[n]


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem One Example:", SolutionProblemOne().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print("Problem Two Example:", SolutionProblemTwo().maxProfit([7,1,5,3,6,4]))
    print("Problem Three Example:", SolutionProblemThree().nthUglyNumber(10))
    print("Problem Four Example:", SolutionProblemFour().numSquares(12))

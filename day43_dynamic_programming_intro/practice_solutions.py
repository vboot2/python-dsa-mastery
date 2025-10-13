"""
Day 43: Dynamic Programming - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Climbing Stairs (LeetCode 70, Easy)
# Link: https://leetcode.com/problems/climbing-stairs/
# ---------------------------------------------------------
class SolutionClimbingStairs:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b


# ---------------------------------------------------------
# Problem 2: House Robber (LeetCode 198, Medium)
# Link: https://leetcode.com/problems/house-robber/
# ---------------------------------------------------------
class SolutionHouseRobber:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            # Choose max of robbing this house or skipping it
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]


# ---------------------------------------------------------
# Problem 3: Min Cost Climbing Stairs (LeetCode 746, Easy)
# Link: https://leetcode.com/problems/min-cost-climbing-stairs/
# ---------------------------------------------------------
class SolutionMinCostClimbingStairs:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[n]


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Climbing Stairs Example:", SolutionClimbingStairs().climbStairs(5))
    print("House Robber Example:", SolutionHouseRobber().rob([2,7,9,3,1]))
    print("Min Cost Climbing Stairs Example:",
          SolutionMinCostClimbingStairs().minCostClimbingStairs([10,15,20]))

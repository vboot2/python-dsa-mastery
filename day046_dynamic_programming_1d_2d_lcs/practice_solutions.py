"""
Day 46: Dynamic Programming (1D, 2D, LCS) - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Word Break (LeetCode 139, Medium)
# Link: https://leetcode.com/problems/word-break/
# ---------------------------------------------------------
class SolutionWordBreak:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for w in wordSet:
                if i >= len(w) and dp[i - len(w)] and s[i - len(w):i] == w:
                    dp[i] = True
                    break
        return dp[-1]


# ---------------------------------------------------------
# Problem 2: Target Sum (LeetCode 494, Medium)
# Link: https://leetcode.com/problems/target-sum/
# ---------------------------------------------------------
class SolutionTargetSum:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total = sum(nums)
        if (target + total) % 2 != 0 or abs(target) > total:
            return 0

        subset_sum = (target + total) // 2

        if subset_sum < 0:
            return 0

        dp = [0] * (subset_sum + 1)
        dp[0] = 1

        for num in nums:
            for s in range(subset_sum, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[-1]


# ---------------------------------------------------------
# Problem 3: Coin Change II (LeetCode 518, Medium)
# Link: https://leetcode.com/problems/coin-change-ii/
# ---------------------------------------------------------
class SolutionCoinChange2:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Word Break Example:", SolutionWordBreak().wordBreak("leetcode", ["leet", "code"]))
    print("Target Sum Example:", SolutionTargetSum().findTargetSumWays([1,1,1,1,1], 3))
    print("Coin Change II Example:", SolutionCoinChange2().change(5, [1,2,5]))

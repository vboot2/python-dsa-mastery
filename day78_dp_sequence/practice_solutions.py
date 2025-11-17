"""
Day 78: DP Sequence - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Number of Longest Increasing Subsequence (LeetCode 673, Medium)
# Link: https://leetcode.com/problems/number-of-longest-increasing-subsequence/
# ---------------------------------------------------------
class SolutionLISCount:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        dp = [1] * n
        count = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]

        max_len = max(dp)
        return sum(c for l, c in zip(dp, count) if l == max_len)


# ---------------------------------------------------------
# Problem 2: Arithmetic Slices (LeetCode 413, Medium)
# Link: https://leetcode.com/problems/arithmetic-slices/
# ---------------------------------------------------------
class SolutionArithmeticSlices:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0

        total = 0
        curr = 0

        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                curr += 1
                total += curr
            else:
                curr = 0

        return total


# ---------------------------------------------------------
# Problem 3: Russian Doll Envelopes (LeetCode 354, Hard)
# Link: https://leetcode.com/problems/russian-doll-envelopes/
# ---------------------------------------------------------
class SolutionRussianDolls:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        """
        Sort by width ASC, height DESC.
        Then find LIS on heights.
        """
        if not envelopes:
            return 0

        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # extract heights
        heights = [h for _, h in envelopes]

        # LIS on heights using binary search
        import bisect
        lis = []

        for h in heights:
            idx = bisect.bisect_left(lis, h)
            if idx == len(lis):
                lis.append(h)
            else:
                lis[idx] = h

        return len(lis)


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("LIS Count:", SolutionLISCount().findNumberOfLIS([1,3,5,4,7]))
    print("Arithmetic Slices:", SolutionArithmeticSlices().numberOfArithmeticSlices([1,2,3,4]))
    print("Russian Doll Envelopes:", SolutionRussianDolls().maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))

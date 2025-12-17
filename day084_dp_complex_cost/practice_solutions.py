"""
Day 84: DP – Complex Cost – LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Uncrossed Lines (LeetCode 1035, Medium)
# Link: https://leetcode.com/problems/uncrossed-lines/
# ---------------------------------------------------------
class SolutionProblemOne:
    def solve(self, nums1, nums2):
        # This is simply LCS DP
        m, n = len(nums1), len(nums2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

        return dp[m][n]


# ---------------------------------------------------------
# Problem 2: Max Dot Product of Two Subsequences (LeetCode 1458, Hard)
# Link: https://leetcode.com/problems/max-dot-product-of-two-subsequences/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def solve(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        dp = [[float('-inf')] * (n+1) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                prod = nums1[i] * nums2[j]
                # transitions:
                # 1. take this pair alone
                # 2. extend previous pair chain
                # 3. skip from nums1 or nums2
                dp[i+1][j+1] = max(
                    prod,
                    dp[i][j] + prod,
                    dp[i][j+1],
                    dp[i+1][j]
                )
        return dp[m][n]


# ---------------------------------------------------------
# Problem 3: Minimum Cost to Cut a Stick (LeetCode 1547, Hard)
# Link: https://leetcode.com/problems/minimum-cost-to-cut-a-stick/
# ---------------------------------------------------------
class SolutionProblemThree:
    def solve(self, n, cuts):
        cuts = sorted(cuts)
        arr = [0] + cuts + [n]
        m = len(arr)

        from functools import lru_cache

        @lru_cache(None)
        def dp(i, j):
            # no cut between (i,j)
            if j - i == 1:
                return 0

            best = float("inf")
            for k in range(i+1, j):
                cost = dp(i, k) + dp(k, j) + arr[j] - arr[i]
                best = min(best, cost)
            return best

        return dp(0, m-1)


# ---------------------------------------------------------
# Example usage
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem One Example:",
          SolutionProblemOne().solve([1,4,2], [1,2,4]))

    print("Problem Two Example:",
          SolutionProblemTwo().solve([2,1,-2,5], [3,0,-6]))

    print("Problem Three Example:",
          SolutionProblemThree().solve(7, [1,3,4,5]))

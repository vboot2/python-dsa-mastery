"""
Day 77: DP String/Subarray - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem: Regular Expression Matching (LeetCode 10, Hard)
# Link: https://leetcode.com/problems/regular-expression-matching/
# ---------------------------------------------------------
class SolutionProblemOne:
    def solve(self, s: str, p: str) -> bool:
        # DP table
        dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
        dp[0][0] = True

        # Handle prefixes like a*, a*b*, etc.
        for j in range(2, len(p)+1):
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-2]

        # Transition rules
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):

                if p[j-1] == "." or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]

                elif p[j-1] == "*":
                    # zero of previous
                    dp[i][j] = dp[i][j-2]
                    # one or more of previous
                    if p[j-2] == "." or p[j-2] == s[i-1]:
                        dp[i][j] = dp[i][j] or dp[i-1][j]

        return dp[-1][-1]


# ---------------------------------------------------------
# Problem: Wildcard Matching (LeetCode 44, Hard)
# Link: https://leetcode.com/problems/wildcard-matching/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def solve(self, s: str, p: str) -> bool:

        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True

        # Leading '*' matches empty string
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        # DP filling
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):

                if p[j - 1] == "*":
                    # (1) '*' matches empty  => dp[i][j-1]
                    # (2) '*' consumes char => dp[i-1][j]
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

                elif p[j - 1] == "?" or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[-1][-1]


# ---------------------------------------------------------
# Problem: Maximum Sum of 3 Non-Overlapping Subarrays (689, Hard)
# Link: https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/
# ---------------------------------------------------------
class SolutionProblemThree:
    def solve(self, nums, k):
        n = len(nums)
        if n < 3 * k:
            return []

        W = [0] * (n - k + 1)
        cur = sum(nums[:k])
        W[0] = cur
        for i in range(1, n - k + 1):
            cur += nums[i + k - 1] - nums[i - 1]
            W[i] = cur

        left = [0] * len(W)
        best = 0
        for i in range(len(W)):
            if W[i] > W[best]:
                best = i
            left[i] = best

        right = [0] * len(W)
        best = len(W) - 1
        for i in range(len(W) - 1, -1, -1):
            if W[i] >= W[best]:
                best = i
            right[i] = best

        best_total = -1
        ans = None

        for j in range(k, len(W) - k):
            i = left[j - k]
            t = right[j + k]
            total = W[i] + W[j] + W[t]

            candidate = [i, j, t]

            if total > best_total:
                best_total = total
                ans = candidate
            elif total == best_total and candidate < ans:
                ans = candidate

        return ans


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem One Example:", SolutionProblemOne().solve("aab", "c*a*b"))
    print("Problem Two Example:", SolutionProblemTwo().solve("adceb", "*a*b"))
    print("Problem Three Example:", SolutionProblemThree().solve([1,2,1,2,6,7,5,1], 2))

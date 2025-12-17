"""
Day 76: DP Palindromic / Sequence - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Palindrome Partitioning II (LeetCode 132, Hard)
# Link: https://leetcode.com/problems/palindrome-partitioning-ii/
# ---------------------------------------------------------

class SolutionMinCut:
    def minCut(self, s: str) -> int:
        n = len(s)
        pal = [[False]*n for _ in range(n)]

        # Precompute palindromes
        for r in range(n):
            for l in range(r+1):
                if s[l] == s[r] and (r-l < 2 or pal[l+1][r-1]):
                    pal[l][r] = True

        dp = [float('inf')] * n

        for i in range(n):
            if pal[0][i]:
                dp[i] = 0
            else:
                for j in range(i):
                    if pal[j+1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]


# ---------------------------------------------------------
# Problem 2: Minimum Insertions to Make a String Palindrome (LeetCode 1312, Hard)
# Link: https://leetcode.com/problems/minimum-insertions-to-make-a-string-palindrome/
# ---------------------------------------------------------

class SolutionMinInsertions:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]

        # classic DP on intervals
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])

        return dp[0][n-1]


# ---------------------------------------------------------
# Problem 3: Distinct Subsequences (LeetCode 115, Hard)
# Link: https://leetcode.com/problems/distinct-subsequences/
# ---------------------------------------------------------

class SolutionDistinctSubseq:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0]*(n+1) for _ in range(m+1)]

        # Empty t can always be formed in 1 way
        for i in range(m+1):
            dp[i][0] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[m][n]


# ---------------------------------------------------------
# Example Usage
# ---------------------------------------------------------

if __name__ == "__main__":
    print("Min Cut:", SolutionMinCut().minCut("aab"))                 # 1
    print("Min Insertions:", SolutionMinInsertions().minInsertions("mbadm"))  # 2
    print("Distinct Subsequences:", SolutionDistinctSubseq().numDistinct("rabbbit", "rabbit"))  # 3

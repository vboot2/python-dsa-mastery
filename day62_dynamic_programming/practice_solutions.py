"""
Day 62: 1D / 2D Dynamic Programming - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem: Longest Palindromic Substring (LeetCode 5, Medium)
# Link: https://leetcode.com/problems/longest-palindromic-substring/
# ---------------------------------------------------------


class Solution5:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start, max_len = 0, 1

        for i in range(n):
            dp[i][i] = True

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if s[i] == s[j] and (l == 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if l > max_len:
                        start, max_len = i, l

        return s[start : start + max_len]


# ---------------------------------------------------------
# Problem: Longest Increasing Path in a Matrix (LeetCode 329, Hard)
# Link: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# ---------------------------------------------------------


class Solution329:
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]
            val = 1
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    val = max(val, 1 + dfs(ni, nj))
            dp[i][j] = val
            return val

        return max(dfs(i, j) for i in range(m) for j in range(n))


# ---------------------------------------------------------
# Problem: Palindromic Substrings (LeetCode 647, Medium)
# Link: https://leetcode.com/problems/palindromic-substrings/
# ---------------------------------------------------------


class Solution647:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 1 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    count += 1
        return count


# ---------------------------------------------------------
# Example usage
# ---------------------------------------------------------
if __name__ == "__main__":
    print("LeetCode 5 Example:", Solution5().longestPalindrome("babad"))
    print(
        "LeetCode 329 Example:",
        Solution329().longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]),
    )
    print("LeetCode 647 Example:", Solution647().countSubstrings("aaa"))

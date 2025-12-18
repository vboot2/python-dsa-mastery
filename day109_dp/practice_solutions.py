"""
Day 109: DP - LeetCode Problem Solutions
"""

from typing import List


# ---------------------------------------------------------
# Problem: Divisor Game (LeetCode 1025, Easy)
# Link: https://leetcode.com/problems/divisor-game/
# ---------------------------------------------------------
class SolutionProblemOne:
    def divisorGame(self, n: int) -> bool:
        """
        DP observation:
        Alice wins iff n is even.
        """
        return n % 2 == 0


# ---------------------------------------------------------
# Problem: N-th Tribonacci Number (LeetCode 1137, Easy)
# Link: https://leetcode.com/problems/n-th-tribonacci-number/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def tribonacci(self, n: int) -> int:
        """
        DP with constant space.
        """
        if n == 0:
            return 0
        if n <= 2:
            return 1

        a, b, c = 0, 1, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c


# ---------------------------------------------------------
# Problem: Maximum Repeating Substring (LeetCode 1668, Easy)
# Link: https://leetcode.com/problems/maximum-repeating-substring/
# ---------------------------------------------------------
class SolutionProblemThree:
    def maxRepeating(self, sequence: str, word: str) -> int:
        """
        DP:
        dp[i] = number of repeats ending at index i
        """
        n = len(sequence)
        m = len(word)
        dp = [0] * (n + 1)
        ans = 0

        for i in range(m, n + 1):
            if sequence[i - m:i] == word:
                dp[i] = dp[i - m] + 1
                ans = max(ans, dp[i])

        return ans


# ---------------------------------------------------------
# Problem: Longest Unequal Adjacent Groups Subsequence I
# (LeetCode 2900, Easy)
# Link: https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/
# ---------------------------------------------------------
class SolutionProblemFour:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        """
        Greedy + DP intuition:
        Pick words whenever group changes.
        """
        result = [words[0]]

        for i in range(1, len(words)):
            if groups[i] != groups[i - 1]:
                result.append(words[i])

        return result


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem One Example:", SolutionProblemOne().divisorGame(4))
    print("Problem Two Example:", SolutionProblemTwo().tribonacci(6))
    print("Problem Three Example:", SolutionProblemThree().maxRepeating("ababc", "ab"))
    print(
        "Problem Four Example:",
        SolutionProblemFour().getLongestSubsequence(
            ["a", "b", "c", "d"], [1, 0, 1, 0]
        ),
    )

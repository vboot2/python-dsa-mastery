"""
practice_solutions.py
Day 02 - Strings
This file contains clean, well-documented solutions to selected LeetCode string problems.
"""

from typing import List


# ---------------------------------------------------------
# Problem: Valid Anagram (LeetCode 242, Easy)
# Link: https://leetcode.com/problems/valid-anagram/
# ---------------------------------------------------------
class SolutionValidAnagram:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


# ---------------------------------------------------------
# Problem: Valid Palindrome (LeetCode 125, Easy)
# Link: https://leetcode.com/problems/valid-palindrome/
# ---------------------------------------------------------
class SolutionValidPalindrome:
    def isPalindrome(self, s: str) -> bool:
        alpha_numeric_lower = [c.lower() for c in s if c.isalnum()]
        l, r = 0 , len(alpha_numeric_lower) - 1
        while l < r:
            if alpha_numeric_lower[l] != alpha_numeric_lower[r]:
                return False
            l += 1
            r -= 1
        return True


# ---------------------------------------------------------
# Problem: Longest Common Prefix (LeetCode 14, Easy)
# Link: https://leetcode.com/problems/longest-common-prefix/
# ---------------------------------------------------------
class SolutionLongestCommonPrefix:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


# ---------------------------------------------------------
# Example usage (for local testing only, not required on LeetCode)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Valid Anagram Example 1:", SolutionValidAnagram().isAnagram("anagram", "nagaram"))
    print("Valid Anagram Example 2:", SolutionValidAnagram().isAnagram("rat", "car"))
    print("Valid Palindrome Example 1:", SolutionValidPalindrome().isPalindrome("A man, a plan, a canal: Panama"))
    print("Valid Palindrome Example 2:", SolutionValidPalindrome().isPalindrome("race a car"))
    print("Valid Palindrome Example 3:", SolutionValidPalindrome().isPalindrome(""))
    print("Longest Common Prefix Example 1:", SolutionLongestCommonPrefix().longestCommonPrefix(["flower", "flow", "flight"]))
    print("Longest Common Prefix Example 2:", SolutionLongestCommonPrefix().longestCommonPrefix(["dog","racecar","car"]))

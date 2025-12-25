""" Day 116: String - LeetCode Problem Solutions """

from typing import List


# ---------------------------------------------------------
# Problem: Roman to Integer (LeetCode 13, Easy)
# Link: https://leetcode.com/problems/roman-to-integer/
# ---------------------------------------------------------
class SolutionProblemOne:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100,
            "D": 500, "M": 1000
        }

        total = 0
        for i in range(len(s)):
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total


# ---------------------------------------------------------
# Problem: Find the Index of the First Occurrence in a String (LeetCode 28, Easy)
# Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


# ---------------------------------------------------------
# Problem: Length of Last Word (LeetCode 58, Easy)
# Link: https://leetcode.com/problems/length-of-last-word/
# ---------------------------------------------------------
class SolutionProblemThree:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()
        return len(words[-1])


# ---------------------------------------------------------
# Problem: Excel Sheet Column Title (LeetCode 168, Easy)
# Link: https://leetcode.com/problems/excel-sheet-column-title/
# ---------------------------------------------------------
class SolutionProblemFour:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []

        while columnNumber > 0:
            columnNumber -= 1
            result.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26

        return "".join(reversed(result))


# ---------------------------------------------------------
# Problem: Excel Sheet Column Number (LeetCode 171, Easy)
# Link: https://leetcode.com/problems/excel-sheet-column-number/
# ---------------------------------------------------------
class SolutionProblemFive:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for c in columnTitle:
            result = result * 26 + (ord(c) - ord('A') + 1)
        return result


# ---------------------------------------------------------
# Problem: Isomorphic Strings (LeetCode 205, Easy)
# Link: https://leetcode.com/problems/isomorphic-strings/
# ---------------------------------------------------------
class SolutionProblemSix:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_st = {}
        map_ts = {}

        for a, b in zip(s, t):
            if a in map_st and map_st[a] != b:
                return False
            if b in map_ts and map_ts[b] != a:
                return False
            map_st[a] = b
            map_ts[b] = a

        return True


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem One Example:", SolutionProblemOne().romanToInt("MCMXCIV"))
    print("Problem Two Example:", SolutionProblemTwo().strStr("sadbutsad", "sad"))
    print("Problem Three Example:", SolutionProblemThree().lengthOfLastWord("Hello World"))
    print("Problem Four Example:", SolutionProblemFour().convertToTitle(28))
    print("Problem Five Example:", SolutionProblemFive().titleToNumber("AB"))
    print("Problem Six Example:", SolutionProblemSix().isIsomorphic("egg", "add"))

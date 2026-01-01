"""Day 121: Two Pointers - LeetCode Problem Solutions"""

from typing import List


# ---------------------------------------------------------
# Problem: Shortest Distance to a Character (LeetCode 821, Easy)
# Link: https://leetcode.com/problems/shortest-distance-to-a-character/
# ---------------------------------------------------------
class SolutionProblemOne:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        """
        Two-pass technique:
        - Left to right
        - Right to left
        """
        n = len(s)
        result = [0] * n
        prev = -n

        for i in range(n):
            if s[i] == c:
                prev = i
            result[i] = i - prev

        prev = 2 * n
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            result[i] = min(result[i], prev - i)

        return result


# ---------------------------------------------------------
# Problem: Reverse Only Letters (LeetCode 917, Easy)
# Link: https://leetcode.com/problems/reverse-only-letters/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def reverseOnlyLetters(self, s: str) -> str:
        res = list(s)
        left, right = 0, len(res) - 1

        while left < right:
            if not res[left].isalpha():
                left += 1
            elif not res[right].isalpha():
                right -= 1
            else:
                res[left], res[right] = res[right], res[left]
                left += 1
                right -= 1

        return "".join(res)


# ---------------------------------------------------------
# Problem: Long Pressed Name (LeetCode 925, Easy)
# Link: https://leetcode.com/problems/long-pressed-name/
# ---------------------------------------------------------
class SolutionProblemThree:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0

        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False

        return i == len(name)


# ---------------------------------------------------------
# Problem: DI String Match (LeetCode 942, Easy)
# Link: https://leetcode.com/problems/di-string-match/
# ---------------------------------------------------------
class SolutionProblemFour:
    def diStringMatch(self, s: str) -> List[int]:
        """
        Two pointers (low & high):
        - 'I' → take low
        - 'D' → take high
        """
        low, high = 0, len(s)
        result = []

        for ch in s:
            if ch == "I":
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1

        result.append(low)
        return result


# ---------------------------------------------------------
# Problem: Remove Palindromic Subsequences (LeetCode 1332, Easy)
# Link: https://leetcode.com/problems/remove-palindromic-subsequences/
# ---------------------------------------------------------
class SolutionProblemFive:
    def removePalindromeSub(self, s: str) -> int:
        """
        Observation:
        - Empty string → 0
        - Palindrome → 1
        - Else → 2 (remove all 'a', then 'b')
        """
        if not s:
            return 0

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return 2
            left += 1
            right -= 1

        return 1


# ---------------------------------------------------------
# Problem: Check If a Word Occurs As a Prefix of Any Word in a Sentence (LeetCode 1455, Easy)
# Link: https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
# ---------------------------------------------------------
class SolutionProblemSix:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()

        for i, word in enumerate(words):
            if word.startswith(searchWord):
                return i + 1

        return -1


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("821 Example:", SolutionProblemOne().shortestToChar("loveleetcode", "e"))
    print("917 Example:", SolutionProblemTwo().reverseOnlyLetters("a-bC-dEf-ghIj"))
    print("925 Example:", SolutionProblemThree().isLongPressedName("alex", "aaleex"))
    print("942 Example:", SolutionProblemFour().diStringMatch("IDID"))
    print("1332 Example:", SolutionProblemFive().removePalindromeSub("ababa"))
    print(
        "1455 Example:",
        SolutionProblemSix().isPrefixOfWord("i love eating burger", "burg"),
    )

""" Day 120: String - LeetCode Problem Solutions """

from typing import List, Optional

# ---------------------------------------------------------
# Problem: Robot Return to Origin (LeetCode 657, Easy)
# Link: https://leetcode.com/problems/robot-return-to-origin/
# ---------------------------------------------------------
class SolutionProblemOne:
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0
        for m in moves:
            if m == 'U':
                y += 1
            elif m == 'D':
                y -= 1
            elif m == 'L':
                x -= 1
            elif m == 'R':
                x += 1
        return x == 0 and y == 0


# ---------------------------------------------------------
# Problem: Valid Palindrome II (LeetCode 680, Easy)
# Link: https://leetcode.com/problems/valid-palindrome-ii/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return is_pal(left + 1, right) or is_pal(left, right - 1)
            left += 1
            right -= 1
        return True


# ---------------------------------------------------------
# Problem: Count Binary Substrings (LeetCode 696, Easy)
# Link: https://leetcode.com/problems/count-binary-substrings/
# ---------------------------------------------------------
class SolutionProblemThree:
    def countBinarySubstrings(self, s: str) -> int:
        """
        Count lengths of consecutive groups.
        Answer is sum of min(prev_group, curr_group).
        """
        groups = []
        count = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1

        groups.append(count)

        result = 0
        for i in range(1, len(groups)):
            result += min(groups[i - 1], groups[i])

        return result


# ---------------------------------------------------------
# Problem: To Lower Case (LeetCode 709, Easy)
# Link: https://leetcode.com/problems/to-lower-case/
# ---------------------------------------------------------
class SolutionProblemFour:
    def toLowerCase(self, s: str) -> str:
        result = []

        for c in s:
            if 'A' <= c <= 'Z':
                result.append(chr(ord(c) + 32))
            else:
                result.append(c)

        return "".join(result)


# ---------------------------------------------------------
# Problem: Shortest Completing Word (LeetCode 748, Easy)
# Link: https://leetcode.com/problems/shortest-completing-word/
# ---------------------------------------------------------
class SolutionProblemFive:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        from collections import Counter

        freq = Counter(c.lower() for c in licensePlate if c.isalpha())

        def completes(word):
            wf = Counter(word.lower())
            for c in freq:
                if wf[c] < freq[c]:
                    return False
            return True

        result = None
        for w in words:
            if completes(w):
                if result is None or len(w) < len(result):
                    result = w

        return result


# ---------------------------------------------------------
# Problem: Jewels and Stones (LeetCode 771, Easy)
# Link: https://leetcode.com/problems/jewels-and-stones/
# ---------------------------------------------------------
class SolutionProblemSix:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        return sum(1 for c in stones if c in jewel_set)


# ---------------------------------------------------------
# Problem: Rotate String (LeetCode 796, Easy)
# Link: https://leetcode.com/problems/rotate-string/
# ---------------------------------------------------------
class SolutionProblemSeven:
    def rotateString(self, s: str, goal: str) -> bool:
        """
        Rotation check:
        goal must be substring of s+s
        """
        if len(s) != len(goal):
            return False
        return goal in (s + s)


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("657 Example:", SolutionProblemOne().judgeCircle("UD"))
    print("680 Example:", SolutionProblemTwo().validPalindrome("abca"))
    print("696 Example:", SolutionProblemThree().countBinarySubstrings("00110011"))
    print("709 Example:", SolutionProblemFour().toLowerCase("Hello"))
    print("748 Example:", SolutionProblemFive().shortestCompletingWord(
        "1s3 PSt", ["step", "steps", "stripe", "stepple"]
    ))
    print("771 Example:", SolutionProblemSix().numJewelsInStones("aA", "aAAbbbb"))
    print("796 Example:", SolutionProblemSeven().rotateString("abcde", "cdeab"))

""" Day 118: String - LeetCode Problem Solutions """

from typing import List

# ---------------------------------------------------------
# Problem: Longest Palindrome (LeetCode 409, Easy)
# Link: https://leetcode.com/problems/longest-palindrome/
# ---------------------------------------------------------
class SolutionProblemOne:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        freq = Counter(s)
        length = 0
        odd = False

        for c in freq.values():
            if c % 2 == 0:
                length += c
            else:
                length += c - 1
                odd = True

        return length + (1 if odd else 0)


# ---------------------------------------------------------
# Problem: Fizz Buzz (LeetCode 412, Easy)
# Link: https://leetcode.com/problems/fizz-buzz/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        for i in range(1, n + 1):
            if i % 15 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))

        return result


# ---------------------------------------------------------
# Problem: Add Strings (LeetCode 415, Easy)
# Link: https://leetcode.com/problems/add-strings/
# ---------------------------------------------------------
class SolutionProblemThree:
    def addStrings(self, num1: str, num2: str) -> str:
        """
        Manual addition without converting to integers.
        """
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            x = ord(num1[i]) - ord('0') if i >= 0 else 0
            y = ord(num2[j]) - ord('0') if j >= 0 else 0

            total = x + y + carry
            result.append(str(total % 10))
            carry = total // 10

            i -= 1
            j -= 1

        return "".join(reversed(result))


# ---------------------------------------------------------
# Problem: Number of Segments in a String (LeetCode 434, Easy)
# Link: https://leetcode.com/problems/number-of-segments-in-a-string/
# ---------------------------------------------------------
class SolutionProblemFour:
    def countSegments(self, s: str) -> int:
        """
        Count transitions from space to non-space.
        """
        count = 0
        in_word = False

        for c in s:
            if c != ' ' and not in_word:
                count += 1
                in_word = True
            elif c == ' ':
                in_word = False

        return count


# ---------------------------------------------------------
# Problem: Repeated Substring Pattern (LeetCode 459, Easy)
# Link: https://leetcode.com/problems/repeated-substring-pattern/
# ---------------------------------------------------------
class SolutionProblemFive:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]


# ---------------------------------------------------------
# Problem: License Key Formatting (LeetCode 482, Easy)
# Link: https://leetcode.com/problems/license-key-formatting/
# ---------------------------------------------------------
class SolutionProblemSix:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        groups = []

        while s:
            groups.append(s[-k:])
            s = s[:-k]

        return "-".join(reversed(groups))


# ---------------------------------------------------------
# Problem: Base 7 (LeetCode 504, Easy)
# Link: https://leetcode.com/problems/base-7/
# ---------------------------------------------------------
class SolutionProblemSeven:
    def convertToBase7(self, num: int) -> str:
        x = num
        result = ""
        ctrl = 0
        if num < 0:
            ctrl = 1
            num *= -1
        while num > 1:
            result += str(num % 7)
            num = num // 7
        if num != 0:
            result += str(num)
        if ctrl == 1:
            result += "-"
        if x == 0:
            return "0"

        return result[::-1]


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("409 Example:", SolutionProblemOne().longestPalindrome("abccccdd"))
    print("412 Example:", SolutionProblemTwo().fizzBuzz(15))
    print("415 Example:", SolutionProblemThree().addStrings("456", "77"))
    print("434 Example:", SolutionProblemFour().countSegments("Hello, my name is John"))
    print("459 Example:", SolutionProblemFive().repeatedSubstringPattern("abab"))
    print("482 Example:", SolutionProblemSix().licenseKeyFormatting("5F3Z-2e-9-w", 4))
    print("504 Example:", SolutionProblemSeven().convertToBase7(100))

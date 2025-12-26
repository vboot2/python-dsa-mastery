""" Day 117: String - LeetCode Problem Solutions """

from typing import List
from collections import Counter

# ---------------------------------------------------------
# Problem: Word Pattern (LeetCode 290, Easy)
# Link: https://leetcode.com/problems/word-pattern/
# ---------------------------------------------------------
class SolutionProblemOne:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Use two hash maps to ensure one-to-one mapping
        between pattern characters and words.
        """
        words = s.split()
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for c, w in zip(pattern, words):
            if c in char_to_word and char_to_word[c] != w:
                return False
            if w in word_to_char and word_to_char[w] != c:
                return False
            char_to_word[c] = w
            word_to_char[w] = c

        return True


# ---------------------------------------------------------
# Problem: Reverse String (LeetCode 344, Easy)
# Link: https://leetcode.com/problems/reverse-string/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def reverseString(self, s: List[str]) -> None:
        """
        In-place two-pointer swap.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


# ---------------------------------------------------------
# Problem: Reverse Vowels of a String (LeetCode 345, Easy)
# Link: https://leetcode.com/problems/reverse-vowels-of-a-string/
# ---------------------------------------------------------
class SolutionProblemThree:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        chars: List[str] = list(s)
        left, right = 0, len(chars) - 1

        while left < right:
            if chars[left] not in vowels:
                left += 1
            elif chars[right] not in vowels:
                right -= 1
            else:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        return "".join(chars)


# ---------------------------------------------------------
# Problem: Ransom Note (LeetCode 383, Easy)
# Link: https://leetcode.com/problems/ransom-note/
# ---------------------------------------------------------
class SolutionProblemFour:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Count characters in magazine and consume for ransomNote.
        """
        freq = Counter(magazine)

        for c in ransomNote:
            if freq[c] == 0:
                return False
            freq[c] -= 1

        return True


# ---------------------------------------------------------
# Problem: First Unique Character in a String (LeetCode 387, Easy)
# Link: https://leetcode.com/problems/first-unique-character-in-a-string/
# ---------------------------------------------------------
class SolutionProblemFive:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)

        for i, c in enumerate(s):
            if freq[c] == 1:
                return i

        return -1


# ---------------------------------------------------------
# Problem: Find the Difference (LeetCode 389, Easy)
# Link: https://leetcode.com/problems/find-the-difference/
# ---------------------------------------------------------
class SolutionProblemSix:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        XOR trick:
        a ^ a = 0, 0 ^ b = b
        """
        res = 0
        for c in s + t:
            res ^= ord(c)
        return chr(res)


# ---------------------------------------------------------
# Problem: Convert a Number to Hexadecimal (LeetCode 405, Easy)
# Link: https://leetcode.com/problems/convert-a-number-to-hexadecimal/
# ---------------------------------------------------------
class SolutionProblemSeven:
    def toHex(self, num: int) -> str:
        """
        Bit manipulation:
        - Handle negative numbers using 32-bit mask
        """
        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"
        num &= 0xFFFFFFFF
        result = []

        while num > 0:
            result.append(hex_chars[num % 16])
            num //= 16

        return "".join(reversed(result))


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("290 Example:", SolutionProblemOne().wordPattern("abba", "dog cat cat dog"))
    arr = ["h", "e", "l", "l", "o"]
    SolutionProblemTwo().reverseString(arr)
    print("344 Example:", arr)
    print("345 Example:", SolutionProblemThree().reverseVowels("hello"))
    print("383 Example:", SolutionProblemFour().canConstruct("aa", "aab"))
    print("387 Example:", SolutionProblemFive().firstUniqChar("leetcode"))
    print("389 Example:", SolutionProblemSix().findTheDifference("abcd", "abcde"))
    print("405 Example:", SolutionProblemSeven().toHex(26))

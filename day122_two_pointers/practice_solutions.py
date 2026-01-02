"""Day 122: Two Pointers - LeetCode Problem Solutions"""

from typing import List


# ---------------------------------------------------------
# Problem: Sort Array By Parity (LeetCode 905, Easy)
# Link: https://leetcode.com/problems/sort-array-by-parity/
# ---------------------------------------------------------
class SolutionProblemOne:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] % 2 == 0:
                left += 1
            elif nums[right] % 2 == 1:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return nums


# ---------------------------------------------------------
# Problem: Sort Array By Parity II (LeetCode 922, Easy)
# Link: https://leetcode.com/problems/sort-array-by-parity-ii/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd = 0, 1
        n = len(nums)

        while even < n and odd < n:
            if nums[even] % 2 == 0:
                even += 2
            elif nums[odd] % 2 == 1:
                odd += 2
            else:
                nums[even], nums[odd] = nums[odd], nums[even]

        return nums


# ---------------------------------------------------------
# Problem: Duplicate Zeros (LeetCode 1089, Easy)
# Link: https://leetcode.com/problems/duplicate-zeros/
# ---------------------------------------------------------
class SolutionProblemThree:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Two pointers from end:
        - Count zeros
        - Shift elements from back
        """
        zeros = arr.count(0)
        n = len(arr)
        i = n - 1
        j = n + zeros - 1

        while i < j:
            if j < n:
                arr[j] = arr[i]
            if arr[i] == 0:
                j -= 1
                if j < n:
                    arr[j] = 0
            i -= 1
            j -= 1


# ---------------------------------------------------------
# Problem: Merge Strings Alternately (LeetCode 1768, Easy)
# Link: https://leetcode.com/problems/merge-strings-alternately/
# ---------------------------------------------------------
class SolutionProblemFour:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        result = []

        while i < len(word1) or j < len(word2):
            if i < len(word1):
                result.append(word1[i])
                i += 1
            if j < len(word2):
                result.append(word2[j])
                j += 1

        return "".join(result)


# ---------------------------------------------------------
# Problem: Check If String Is a Prefix of Array (LeetCode 1961, Easy)
# Link: https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/
# ---------------------------------------------------------
class SolutionProblemFive:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        built = ""
        for w in words:
            built += w
            if built == s:
                return True
            if len(built) > len(s):
                return False
        return False


# ---------------------------------------------------------
# Problem: Reverse Prefix of Word (LeetCode 2000, Easy)
# Link: https://leetcode.com/problems/reverse-prefix-of-word/
# ---------------------------------------------------------
class SolutionProblemSix:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        if idx == -1:
            return word
        return word[: idx + 1][::-1] + word[idx + 1 :]


# ---------------------------------------------------------
# Problem: First Palindromic String in the Array (LeetCode 2108, Easy)
# Link: https://leetcode.com/problems/first-palindromic-string-in-the-array/
# ---------------------------------------------------------
class SolutionProblemSeven:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_pal(s):
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        for w in words:
            if is_pal(w):
                return w
        return ""


# ---------------------------------------------------------
# Problem: Find All K-Distant Indices in an Array (LeetCode 2200, Easy)
# Link: https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/
# ---------------------------------------------------------
class SolutionProblemEight:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        """
        Two pointers / window expansion around key indices.
        """
        result = set()
        n = len(nums)

        for i in range(n):
            if nums[i] == key:
                left = max(0, i - k)
                right = min(n - 1, i + k)
                for j in range(left, right + 1):
                    result.add(j)

        return sorted(result)


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("905 Example:", SolutionProblemOne().sortArrayByParity([3, 1, 2, 4]))
    print("922 Example:", SolutionProblemTwo().sortArrayByParityII([4, 2, 5, 7]))
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    SolutionProblemThree().duplicateZeros(arr)
    print("1089 Example:", arr)
    print("1768 Example:", SolutionProblemFour().mergeAlternately("ab", "pqrs"))
    print(
        "1961 Example:",
        SolutionProblemFive().isPrefixString(
            "iloveleetcode", ["i", "love", "leetcode"]
        ),
    )
    print("2000 Example:", SolutionProblemSix().reversePrefix("abcdefd", "d"))
    print(
        "2108 Example:",
        SolutionProblemSeven().firstPalindrome(["abc", "car", "ada", "racecar"]),
    )
    print(
        "2200 Example:",
        SolutionProblemEight().findKDistantIndices([3, 4, 9, 1, 3, 9, 5], 9, 1),
    )

"""Day 125: Hash Table - LeetCode Problem Solutions"""

from typing import List
from collections import Counter, defaultdict


# ---------------------------------------------------------
# Problem: Set Mismatch (LeetCode 645, Easy)
# Link: https://leetcode.com/problems/set-mismatch/
# ---------------------------------------------------------
class SolutionProblemOne:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        duplicate = missing = -1

        for i in range(1, len(nums) + 1):
            if count[i] == 2:
                duplicate = i
            elif count[i] == 0:
                missing = i

        return [duplicate, missing]


# ---------------------------------------------------------
# Problem: Two Sum IV - Input is a BST (LeetCode 653, Easy)
# Link: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def findTarget(self, root, k: int) -> bool:
        """
        Use hash set to track visited values
        while traversing the tree.
        """
        seen = set()

        def dfs(node):
            if not node:
                return False
            if k - node.val in seen:
                return True
            seen.add(node.val)
            return dfs(node.left) or dfs(node.right)

        return dfs(root)


# ---------------------------------------------------------
# Problem: Degree of an Array (LeetCode 697, Easy)
# Link: https://leetcode.com/problems/degree-of-an-array/
# ---------------------------------------------------------
class SolutionProblemThree:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums)
        degree = max(count.values())

        left = {}
        right = {}

        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i

        min_len = len(nums)
        for num in count:
            if count[num] == degree:
                min_len = min(min_len, right[num] - left[num] + 1)

        return min_len


# ---------------------------------------------------------
# Problem: Unique Morse Code Words (LeetCode 804, Easy)
# Link: https://leetcode.com/problems/unique-morse-code-words/
# ---------------------------------------------------------
class SolutionProblemFour:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]

        transformations = set()
        for word in words:
            code = "".join(morse[ord(c) - ord("a")] for c in word)
            transformations.add(code)

        return len(transformations)


# ---------------------------------------------------------
# Problem: Most Common Word (LeetCode 819, Easy)
# Link: https://leetcode.com/problems/most-common-word/
# ---------------------------------------------------------
class SolutionProblemFive:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        words = []
        word = ""

        for ch in paragraph.lower():
            if ch.isalpha():
                word += ch
            else:
                if word:
                    words.append(word)
                    word = ""
        if word:
            words.append(word)

        count = Counter(words)
        for w in banned_set:
            count.pop(w, None)

        return count.most_common(1)[0][0]


# ---------------------------------------------------------
# Problem: Buddy Strings (LeetCode 859, Easy)
# Link: https://leetcode.com/problems/buddy-strings/
# ---------------------------------------------------------
class SolutionProblemSix:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            return len(set(s)) < len(s)

        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append((s[i], goal[i]))

        return len(diff) == 2 and diff[0] == diff[1][::-1]


# ---------------------------------------------------------
# Problem: Uncommon Words from Two Sentences (LeetCode 884, Easy)
# Link: https://leetcode.com/problems/uncommon-words-from-two-sentences/
# ---------------------------------------------------------
class SolutionProblemSeven:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = Counter(s1.split()) + Counter(s2.split())
        return [word for word, freq in count.items() if freq == 1]


# ---------------------------------------------------------
# Problem: Fair Candy Swap (LeetCode 888, Easy)
# Link: https://leetcode.com/problems/fair-candy-swap/
# ---------------------------------------------------------
class SolutionProblemEight:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]):
        diff = (sum(aliceSizes) - sum(bobSizes)) // 2
        bob_set = set(bobSizes)

        for a in aliceSizes:
            if a - diff in bob_set:
                return [a, a - diff]


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("645 Example:", SolutionProblemOne().findErrorNums([1, 2, 2, 4]))
    print("697 Example:", SolutionProblemThree().findShortestSubArray([1, 2, 2, 3, 1]))
    print(
        "804 Example:",
        SolutionProblemFour().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]),
    )
    print(
        "819 Example:",
        SolutionProblemFive().mostCommonWord(
            "Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]
        ),
    )
    print("859 Example:", SolutionProblemSix().buddyStrings("ab", "ba"))
    print(
        "884 Example:",
        SolutionProblemSeven().uncommonFromSentences(
            "this apple is sweet", "this apple is sour"
        ),
    )
    print("888 Example:", SolutionProblemEight().fairCandySwap([1, 1], [2, 2]))

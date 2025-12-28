""" Day 119: String - LeetCode Problem Solutions """

from typing import List

# ---------------------------------------------------------
# Problem: Detect Capital (LeetCode 520, Easy)
# Link: https://leetcode.com/problems/detect-capital/
# ---------------------------------------------------------
class SolutionProblemOne:
    def detectCapitalUse(self, word: str) -> bool:
        """
        Check all valid capitalization patterns.
        """
        return word.isupper() or word.islower() or (
            word[0].isupper() and word[1:].islower()
        )


# ---------------------------------------------------------
# Problem: Longest Uncommon Subsequence I (LeetCode 521, Easy)
# Link: https://leetcode.com/problems/longest-uncommon-subsequence-i/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def findLUSlength(self, a: str, b: str) -> int:
        """
        If strings are equal, no uncommon subsequence.
        Otherwise, the longer string itself is uncommon.
        """
        return -1 if a == b else max(len(a), len(b))


# ---------------------------------------------------------
# Problem: Reverse String II (LeetCode 541, Easy)
# Link: https://leetcode.com/problems/reverse-string-ii/
# ---------------------------------------------------------
class SolutionProblemThree:
    def reverseStr(self, s: str, k: int) -> str:
        """
        For every 2k characters:
        - Reverse first k characters
        """
        st = list(s)

        for i in range(0, len(st), 2 * k):
            st[i:i + k] = reversed(st[i:i + k])

        return "".join(st)


# ---------------------------------------------------------
# Problem: Student Attendance Record I (LeetCode 551, Easy)
# Link: https://leetcode.com/problems/student-attendance-record-i/
# ---------------------------------------------------------
class SolutionProblemFour:
    def checkRecord(self, s: str) -> bool:
        """
        Conditions:
        - No more than one 'A'
        - No three consecutive 'L'
        """
        if s.count('A') >= 2:
            return False

        return "LLL" not in s


# ---------------------------------------------------------
# Problem: Reverse Words in a String III (LeetCode 557, Easy)
# Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/
# ---------------------------------------------------------
class SolutionProblemFive:
    def reverseWords(self, s: str) -> str:
        """
        Reverse each word while preserving word order.
        """
        return " ".join(word[::-1] for word in s.split())


# ---------------------------------------------------------
# Problem: Minimum Index Sum of Two Lists (LeetCode 599, Easy)
# Link: https://leetcode.com/problems/minimum-index-sum-of-two-lists/
# ---------------------------------------------------------
class SolutionProblemSix:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        """
        Use hash map to store indices of list1.
        Track minimum index sum.
        """
        index_map = {name: i for i, name in enumerate(list1)}
        min_sum = float("inf")
        result = []

        for j, name in enumerate(list2):
            if name in index_map:
                idx_sum = j + index_map[name]
                if idx_sum < min_sum:
                    min_sum = idx_sum
                    result = [name]
                elif idx_sum == min_sum:
                    result.append(name)

        return result


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("520 Example:", SolutionProblemOne().detectCapitalUse("Google"))
    print("521 Example:", SolutionProblemTwo().findLUSlength("aba", "cdc"))
    print("541 Example:", SolutionProblemThree().reverseStr("abcdefg", 2))
    print("551 Example:", SolutionProblemFour().checkRecord("PPALLP"))
    print("557 Example:", SolutionProblemFive().reverseWords("Let's code"))
    print("599 Example:", SolutionProblemSix().findRestaurant(
        ["Shogun", "Tapioca Express", "Burger King", "KFC"],
        ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    ))

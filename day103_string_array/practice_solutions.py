"""
Day 103: String/Array - LeetCode Problem Solutions
"""

from typing import List


# ---------------------------------------------------------
# Problem: Reverse Words in a String (LeetCode 151, Medium)
# Link: https://leetcode.com/problems/reverse-words-in-a-string/
# ---------------------------------------------------------
class SolutionProblemOne:
    def reverseWords(self, s: str) -> str:
        """
        Approach:
        - strip extra spaces
        - split on whitespace
        - reverse the list
        - join with single spaces
        """
        parts = s.strip().split()
        parts.reverse()
        return " ".join(parts)


# ---------------------------------------------------------
# Problem: Compare Version Numbers (LeetCode 165, Medium)
# Link: https://leetcode.com/problems/compare-version-numbers/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def compareVersion(self, version1: str, version2: str) -> int:
        """
        Split on '.' and compare each revision as integers.
        Missing sections are treated as 0.
        """
        v1 = version1.split('.')
        v2 = version2.split('.')

        n = max(len(v1), len(v2))

        for i in range(n):
            a = int(v1[i]) if i < len(v1) else 0
            b = int(v2[i]) if i < len(v2) else 0

            if a > b:
                return 1
            if a < b:
                return -1

        return 0


# ---------------------------------------------------------
# Problem: Maximum Gap (LeetCode 164, Hard)
# Link: https://leetcode.com/problems/maximum-gap/
# ---------------------------------------------------------
class SolutionProblemThree:
    def maximumGap(self, nums: List[int]) -> int:
        """
        Bucket Sort / Pigeonhole Principle (O(n)):
        - If n < 2 return 0
        - Let bucket size = max(1, (max-min)//(n-1))
        - Create buckets: each stores min and max seen
        - Max gap = max(min_of_current - max_of_previous)
        """
        if len(nums) < 2:
            return 0

        lo, hi = min(nums), max(nums)
        if lo == hi:
            return 0

        n = len(nums)
        bucket_size = max(1, (hi - lo) // (n - 1))
        bucket_count = (hi - lo) // bucket_size + 1

        # each bucket stores: (min_val, max_val, is_empty)
        buckets = [[float('inf'), float('-inf'), True] for _ in range(bucket_count)]

        # fill buckets
        for x in nums:
            idx = (x - lo) // bucket_size
            buckets[idx][0] = min(buckets[idx][0], x)
            buckets[idx][1] = max(buckets[idx][1], x)
            buckets[idx][2] = False

        # compute max gap
        prev_max = lo
        max_gap = 0

        for bmin, bmax, empty in buckets:
            if empty:
                continue
            max_gap = max(max_gap, bmin - prev_max)
            prev_max = bmax

        return max_gap


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem One Example:", SolutionProblemOne().reverseWords("  hello world  "))
    print("Problem Two Example:", SolutionProblemTwo().compareVersion("1.01", "1.001"))
    print("Problem Three Example:", SolutionProblemThree().maximumGap([3,6,9,1]))

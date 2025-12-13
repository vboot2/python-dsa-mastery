"""
Day 104: Array - LeetCode Problem Solutions
"""

from typing import List
from collections import Counter, defaultdict


# ---------------------------------------------------------
# Problem: Largest Number (LeetCode 179, Medium)
# Link: https://leetcode.com/problems/largest-number/
# ---------------------------------------------------------
class SolutionProblemOne:
    def largestNumber(self, nums: List[int]) -> str:
        """
        Greedy + custom sort:
        Sort numbers based on combined value comparison.
        """
        nums = list(map(str, nums))
        nums.sort(key=lambda x: x * 10, reverse=True)

        res = "".join(nums)
        return res if res[0] != '0' else "0"


# ---------------------------------------------------------
# Problem: Majority Element II (LeetCode 229, Medium)
# Link: https://leetcode.com/problems/majority-element-ii/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        Boyer-Moore Voting Algorithm (extended):
        At most two elements can appear more than n/3 times.
        """
        if not nums:
            return []

        cand1 = cand2 = None
        count1 = count2 = 0

        for n in nums:
            if n == cand1:
                count1 += 1
            elif n == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = n, 1
            elif count2 == 0:
                cand2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1

        # verify candidates
        result = []
        for x in (cand1, cand2):
            if x is not None and nums.count(x) > len(nums) // 3:
                result.append(x)
        return result


# ---------------------------------------------------------
# Problem: Subarrays with K Different Integers (LeetCode 992, Hard)
# Link: https://leetcode.com/problems/subarrays-with-k-different-integers/
# ---------------------------------------------------------
class SolutionProblemThree:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """
        Exactly K distinct = atMost(K) - atMost(K-1)
        Sliding window + frequency map.
        """
        def atMost(k):
            freq = defaultdict(int)
            left = 0
            res = 0

            for right in range(len(nums)):
                freq[nums[right]] += 1

                while len(freq) > k:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        del freq[nums[left]]
                    left += 1

                res += right - left + 1

            return res

        return atMost(k) - atMost(k - 1)


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem One Example:",
          SolutionProblemOne().largestNumber([3, 30, 34, 5, 9]))
    print("Problem Two Example:",
          SolutionProblemTwo().majorityElement([1,1,1,3,3,2,2,2]))
    print("Problem Three Example:",
          SolutionProblemThree().subarraysWithKDistinct([1,2,1,2,3], 2))

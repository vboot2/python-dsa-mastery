"""
Day 137: Array - LeetCode Problem Solutions
"""

from typing import List


# ---------------------------------------------------------
# Minimum Subsequence in Non-Increasing Order (LeetCode 1403, Easy)
# Link: https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/
# ---------------------------------------------------------
class Solution1403:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total = sum(nums)
        res = []
        for i in nums:
            if sum(res) > total:
                return res
            total -= i
            res.append(i)
        return nums


# ---------------------------------------------------------
# String Matching in an Array (LeetCode 1408, Easy)
# Link: https://leetcode.com/problems/string-matching-in-an-array/
# ---------------------------------------------------------
class Solution1408:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i, v in enumerate(words):
            for j, w in enumerate(words):
                if i == j:
                    continue
                if v in w:
                    res.append(v)
                    break
        return res


# ---------------------------------------------------------
# Minimum Value to Get Positive Step by Step Sum (LeetCode 1413, Easy)
# Link: https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
# ---------------------------------------------------------
class Solution1413:
    def minStartValue(self, nums: List[int]) -> int:
        cur_sum = 0
        min_sum = 0

        for i in nums:
            cur_sum += i
            min_sum = min(min_sum, cur_sum)

        return max(1, 1 - min_sum)


# ---------------------------------------------------------
# Kids With the Greatest Number of Candies (LeetCode 1431, Easy)
# Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# ---------------------------------------------------------
class Solution1431:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        res = []
        for i in candies:
            res.append(i + extraCandies >= max_candies)
        return res


# ---------------------------------------------------------
# Check If All 1's Are at Least Length K Places Away (LeetCode 1437, Easy)
# Link: https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
# ---------------------------------------------------------
class Solution1437:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -k - 1
        for i, val in enumerate(nums):
            if val == 1:
                if i - prev - 1 < k:
                    return False
                prev = i
        return True


# ---------------------------------------------------------
# Number of Students Doing Homework at a Given Time (LeetCode 1450, Easy)
# Link: https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/
# ---------------------------------------------------------
class Solution1450:
    def busyStudent(
        self, startTime: List[int], endTime: List[int], queryTime: int
    ) -> int:
        count = 0
        for i, endtime in enumerate(endTime):
            if endtime >= queryTime >= startTime[i]:
                count += 1
        return count

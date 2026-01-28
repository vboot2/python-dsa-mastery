"""
Day 148: Prefix Sum - LeetCode Problem Solutions
"""

from collections import defaultdict
from typing import List


# ---------------------------------------------------------
# Problem: Contiguous Array (LeetCode 525, Medium)
# Link: https://leetcode.com/problems/contiguous-array/
# ---------------------------------------------------------
class SolutionProblemOne:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = 0
        index = {0: -1}
        res = 0

        for i, n in enumerate(nums):
            prefix += 1 if n == 1 else -1
            if prefix in index:
                res = max(res, i - index[prefix])
            else:
                index[prefix] = i

        return res


# ---------------------------------------------------------
# Problem: Random Pick with Weight (LeetCode 528, Medium)
# Link: https://leetcode.com/problems/random-pick-with-weight/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0
        for x in w:
            total += x
            self.prefix.append(total)

    def pickIndex(self) -> int:
        import random

        target = random.randint(1, self.prefix[-1])

        l, r = 0, len(self.prefix) - 1
        while l < r:
            m = (l + r) // 2
            if self.prefix[m] < target:
                l = m + 1
            else:
                r = m
        return l


# ---------------------------------------------------------
# Problem: Subarray Product Less Than K (LeetCode 713, Medium)
# Link: https://leetcode.com/problems/subarray-product-less-than-k/
# ---------------------------------------------------------
class SolutionProblemThree:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        prod = 1
        left = 0
        res = 0

        for right in range(len(nums)):
            prod *= nums[right]
            while prod >= k:
                prod //= nums[left]
                left += 1
            res += right - left + 1

        return res


# ---------------------------------------------------------
# Problem: My Calendar II (LeetCode 731, Medium)
# Link: https://leetcode.com/problems/my-calendar-ii/
# ---------------------------------------------------------
class MyCalendarTwo:
    def __init__(self):
        self.diff = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        self.diff[start] += 1
        self.diff[end] -= 1

        active = 0
        for k in sorted(self.diff):
            active += self.diff[k]
            if active > 2:
                self.diff[start] -= 1
                self.diff[end] += 1
                return False
        return True


# ---------------------------------------------------------
# Problem: Largest Sum of Averages (LeetCode 813, Medium)
# Link: https://leetcode.com/problems/largest-sum-of-averages/
# ---------------------------------------------------------
class SolutionProblemFive:
    def largestSumOfAverages(self, nums, k) -> float:
        n = len(nums)
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)

        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][1] = prefix[i] / i

        for j in range(2, k + 1):
            for i in range(j, n + 1):
                for x in range(j - 1, i):
                    dp[i][j] = max(
                        dp[i][j], dp[x][j - 1] + (prefix[i] - prefix[x]) / (i - x)
                    )

        return dp[n][k]


# ---------------------------------------------------------
# Problem: Shifting Letters (LeetCode 848, Medium)
# Link: https://leetcode.com/problems/shifting-letters/
# ---------------------------------------------------------
class SolutionProblemSix:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total = 0
        res = []

        for i in range(len(s) - 1, -1, -1):
            total += shifts[i]
            c = chr((ord(s[i]) - ord("a") + total) % 26 + ord("a"))
            res.append(c)

        return "".join(reversed(res))


# ---------------------------------------------------------
# Problem: Binary Subarrays With Sum (LeetCode 930, Medium)
# Link: https://leetcode.com/problems/binary-subarrays-with-sum/
# ---------------------------------------------------------
class SolutionProblemSeven:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = 0
        count = defaultdict(int)
        count[0] = 1
        res = 0

        for n in nums:
            prefix += n
            res += count[prefix - goal]
            count[prefix] += 1

        return res


# ---------------------------------------------------------
# Problem: Subarray Sums Divisible by K (LeetCode 974, Medium)
# Link: https://leetcode.com/problems/subarray-sums-divisible-by-k/
# ---------------------------------------------------------
class SolutionProblemEight:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = defaultdict(int)
        count[0] = 1
        res = 0

        for n in nums:
            prefix = (prefix + n) % k
            res += count[prefix]
            count[prefix] += 1

        return res


# ---------------------------------------------------------
# Problem: Max Consecutive Ones III (LeetCode 1004, Medium)
# Link: https://leetcode.com/problems/max-consecutive-ones-iii/
# ---------------------------------------------------------
class SolutionProblemNine:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros = 0
        res = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            res = max(res, right - left + 1)

        return res


# ---------------------------------------------------------
# Problem: Stone Game II (LeetCode 1140, Medium)
# Link: https://leetcode.com/problems/stone-game-ii/
# ---------------------------------------------------------
class SolutionProblemEleven:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = piles[:]
        for i in range(n - 2, -1, -1):
            suffix[i] += suffix[i + 1]

        from functools import lru_cache

        @lru_cache(None)
        def dfs(i, m):
            if i + 2 * m >= n:
                return suffix[i]
            return max(suffix[i] - dfs(i + x, max(m, x)) for x in range(1, 2 * m + 1))

        return dfs(0, 1)


# ---------------------------------------------------------
# Problem: Can Make Palindrome from Substring (LeetCode 1177, Medium)
# Link: https://leetcode.com/problems/can-make-palindrome-from-substring/
# ---------------------------------------------------------
class SolutionProblemTwelve:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        prefix = [[0] * 26]
        for c in s:
            curr = prefix[-1][:]
            curr[ord(c) - ord("a")] += 1
            prefix.append(curr)

        res = []
        for l, r, k in queries:
            odd = 0
            for i in range(26):
                if (prefix[r + 1][i] - prefix[l][i]) % 2:
                    odd += 1
            res.append(odd // 2 <= k)

        return res
